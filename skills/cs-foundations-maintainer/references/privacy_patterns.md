# 隐私规则说明 / Privacy Pattern Guide

以下为默认隐私扫描正则。可按需增删。
Each line is a regex pattern. Customize based on your sensitive data needs.

推荐默认规则（示例）：
Recommended defaults (examples):

```
[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}
\b\d{3}[-.\s]?\d{2}[-.\s]?\d{4}\b
\b(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{2,4}\)?[-.\s]?)?\d{3,4}[-.\s]?\d{4}\b
\b\d{1,3}(?:\.\d{1,3}){3}\b
\b(?:[A-F0-9]{2}:){5}[A-F0-9]{2}\b
\b(?:AKIA|ASIA)[0-9A-Z]{16}\b
\b[0-9a-f]{32}\b
\b[0-9a-f]{40}\b
```

可自定义追加（示例）：
Custom additions (examples):

- 用户名、真实姓名、公司名等：
  - `\bREPLACE_WITH_USERNAME\b`
  - `\bREPLACE_WITH_REAL_NAME\b`
  - `\bREPLACE_WITH_COMPANY\b`
- 本地路径中含用户名：
  - `/Users/REPLACE_WITH_USERNAME/`
  - `C:\\Users\\REPLACE_WITH_USERNAME\\`
- Repo 内部 token/密钥：
  - `sk-[A-Za-z0-9]{20,}`

注意 / Notes:
- 规则应尽量精确，避免过度脱敏。
- 发布时对任何命中一律替换为 `***`。
