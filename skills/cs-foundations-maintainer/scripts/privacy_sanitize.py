#!/usr/bin/env python3
"""
Scan or redact potential sensitive information in a repo.

Default behavior: scan and report matches without modifying files.
Use --redact to replace matches with *** in-place.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from pathlib import Path
from typing import Iterable, List, Tuple

DEFAULT_EXCLUDE_EXTS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".svg",
    ".pdf",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".mp3",
    ".mp4",
    ".mov",
    ".avi",
    ".ico",
    ".woff",
    ".woff2",
    ".ttf",
    ".otf",
}

DEFAULT_EXCLUDE_PATHS = {
    "web/package-lock.json",
}

DEFAULT_PATTERNS = [
    r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}",  # email
    r"\b\d{3}[-.\s]?\d{2}[-.\s]?\d{4}\b",  # US SSN-like
    r"\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b",  # phone
    r"\b\d{1,3}(?:\.\d{1,3}){3}\b",  # IPv4
    r"\b(?:[A-F0-9]{2}:){5}[A-F0-9]{2}\b",  # MAC
    r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b",  # AWS access key
    r"\b[0-9a-f]{32}\b",  # generic 32-hex tokens
    r"\b[0-9a-f]{40}\b",  # generic 40-hex tokens
]


def run_git(args: List[str], cwd: Path) -> str:
    return subprocess.check_output(["git", *args], cwd=cwd).decode("utf-8")


def get_repo_root(start: Path) -> Path:
    root = run_git(["rev-parse", "--show-toplevel"], cwd=start).strip()
    return Path(root)


def is_binary_bytes(sample: bytes) -> bool:
    if b"\x00" in sample:
        return True
    return False


def iter_files(repo_root: Path) -> Iterable[Path]:
    files = run_git(["ls-files", "-z"], cwd=repo_root)
    for entry in files.split("\x00"):
        if not entry:
            continue
        yield repo_root / entry


def load_patterns(patterns_path: Path | None) -> List[re.Pattern]:
    raw_patterns = []
    if patterns_path and patterns_path.exists():
        for line in patterns_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            raw_patterns.append(line)
    else:
        raw_patterns = DEFAULT_PATTERNS

    compiled = []
    for pat in raw_patterns:
        compiled.append(re.compile(pat, re.IGNORECASE))
    return compiled


def scan_text(text: str, patterns: List[re.Pattern]) -> List[Tuple[re.Pattern, List[Tuple[int, int]]]]:
    results = []
    for pat in patterns:
        spans = [m.span() for m in pat.finditer(text)]
        if spans:
            results.append((pat, spans))
    return results


def redact_text(text: str, patterns: List[re.Pattern]) -> Tuple[str, int]:
    total = 0
    for pat in patterns:
        text, count = pat.subn("***", text)
        total += count
    return text, total


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan or redact sensitive info.")
    parser.add_argument("--patterns", help="Path to regex patterns file.")
    parser.add_argument("--redact", action="store_true", help="Replace matches with ***.")
    parser.add_argument("--exclude-ext", action="append", default=[], help="Extra extensions to skip.")
    parser.add_argument("--exclude-path", action="append", default=[], help="Repo-relative paths to skip.")
    parser.add_argument("--report", default="privacy-report.txt", help="Report file name in repo root.")
    args = parser.parse_args()

    repo_root = get_repo_root(Path.cwd())
    patterns = load_patterns(Path(args.patterns) if args.patterns else None)
    exclude_exts = set(DEFAULT_EXCLUDE_EXTS) | {ext if ext.startswith(".") else f".{ext}" for ext in args.exclude_ext}
    exclude_paths = DEFAULT_EXCLUDE_PATHS | {p.strip() for p in args.exclude_path if p.strip()}

    report_lines = []
    total_hits = 0
    total_files = 0

    for path in iter_files(repo_root):
        rel_path = str(path.relative_to(repo_root))
        if rel_path in exclude_paths:
            continue
        if path.suffix.lower() in exclude_exts:
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        if is_binary_bytes(data[:4096]):
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue

        matches = scan_text(text, patterns)
        if not matches:
            continue

        total_files += 1
        file_hits = sum(len(spans) for _, spans in matches)
        total_hits += file_hits
        report_lines.append(f"{path.relative_to(repo_root)}: {file_hits} hits")
        for pat, spans in matches:
            report_lines.append(f"  pattern: {pat.pattern} ({len(spans)} hits)")

        if args.redact:
            redacted, count = redact_text(text, patterns)
            if count:
                path.write_text(redacted)

    report_path = repo_root / args.report
    report_path.write_text("\n".join(report_lines) + ("\n" if report_lines else ""))

    print(f"Scanned repo: {repo_root}")
    print(f"Files with hits: {total_files}")
    print(f"Total hits: {total_hits}")
    print(f"Report: {report_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
