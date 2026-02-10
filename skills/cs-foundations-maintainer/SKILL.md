---
name: cs-foundations-maintainer
description: 维护并组织 `cs-foundations` 知识库，包括结构整理、索引更新与 GitHub 开源发布准备。用户请求管理、重构、内容新增或发布准备时使用。发布前必须扫描隐私信息并用 `***` 脱敏。 Maintain and organize the `cs-foundations` knowledge repo, including structure cleanups, index upkeep, and open-source readiness. Always scan for sensitive info and redact with `***` before any publishing guidance.
---

# CS Foundations Maintainer / 知识库维护管家

## Overview / 概览

以中文为主维护 `cs-foundations` 知识库，必要时补充英文说明，确保结构一致、内容可维护、可安全开源发布。 Always keep the repo organized, consistent, and safe to publish.

## Workflow / 工作流

### 1. Confirm Scope / 确认范围

- 确认仓库根目录与本次维护目标。
- 判断是否涉及 GitHub 开源发布准备。

### 2. Structure and Content / 结构与内容维护

- 保持已有约定，除非用户要求调整。
- 文件命名优先使用 `kebab-case.md`。
- 主题索引/标签/术语表与内容保持同步。
- 当新增/移动/删除内容时，必须更新索引文件（如 `index/topics.md`、`index/tags.md`、`index/glossary.md`）。
- 当内容有变更且需要同步到网站时，运行 `node web/scripts/sync-content.js` 并更新清单 `node web/scripts/generate-manifest.js`。
- 参考 `references/maintenance_checklist.md` 做例行维护。

### 3. Privacy Scan (Mandatory) / 隐私扫描（必做）

- 发布前必须扫描敏感信息。
- 使用 `scripts/privacy_sanitize.py`，示例：
  - `python3 skills/cs-foundations-maintainer/scripts/privacy_sanitize.py --report privacy-report.txt --patterns skills/cs-foundations-maintainer/references/privacy_patterns.txt`
- 汇总报告并向用户说明命中情况。

### 4. Redaction (Mandatory for Publishing) / 脱敏处理（发布必做）

- 发布准备必须将命中内容替换为 `***`。
- 运行：
  - `python3 skills/cs-foundations-maintainer/scripts/privacy_sanitize.py --redact --report privacy-report.txt --patterns skills/cs-foundations-maintainer/references/privacy_patterns.txt`
- 明确指出被修改的文件。

### 5. Publish Readiness / 发布准备

- 确保 `README.md`、`CONTRIBUTING.md`、`LICENSE` 等文件齐全。
- 若仍存在风险，必须先提示并等待确认。

## Resources / 资源

- `scripts/privacy_sanitize.py`: 扫描/脱敏敏感信息。
- `references/privacy_patterns.txt`: 默认隐私正则列表。
- `references/privacy_patterns.md`: 隐私规则说明与扩展建议。
- `references/maintenance_checklist.md`: 维护检查清单。
