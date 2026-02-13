import json
import time
from typing import Any


def now_ms() -> int:
    return int(time.time() * 1000)


def elapsed_ms(start_ms: int) -> int:
    return now_ms() - start_ms


def pretty_json(data: Any) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


def print_response_summary(method: str, url: str, status_code: int, elapsed: int) -> None:
    print(f"[{method}] {url}")
    print(f"status={status_code} elapsed_ms={elapsed}")
