# cs-foundations

这是一个用于管理计算机基础、算法与相关工程知识的开源知识库。以中文为主，必要时补充英文说明。
This is an open knowledge base for CS foundations, algorithms, and engineering topics. Chinese-first with English as needed.

## 目录结构 / Structure

```
cs-foundations/
  README.md
  index/
    topics.md
    tags.md
    glossary.md
  notes/
    00-overview/
    01-programming/
    02-data-structures/
    03-algorithms/
    04-os/
    05-network/
    06-db/
    07-system-design/
    08-distributed/
    09-security/
    10-ai/
    11-tools/
  problems/
    leetcode/
    interview/
  resources/
  assets/
  templates/
  skills/
```

## 使用 cs-foundations-maintainer 维护结构 / Using the Maintainer Skill

这个仓库内置 `cs-foundations-maintainer` skill，用于整理结构、维护索引，并在开源前进行隐私扫描与脱敏。
The `cs-foundations-maintainer` skill keeps the repo organized and privacy-safe for open-source release.

### 基本流程 / Basic Flow

1. 先扫描隐私（生成报告，不修改文件）：

```bash
python3 skills/cs-foundations-maintainer/scripts/privacy_sanitize.py \
  --report privacy-report.txt \
  --patterns skills/cs-foundations-maintainer/references/privacy_patterns.txt
```

2. 若准备发布，进行脱敏（替换为 `***`）：

```bash
python3 skills/cs-foundations-maintainer/scripts/privacy_sanitize.py \
  --redact \
  --report privacy-report.txt \
  --patterns skills/cs-foundations-maintainer/references/privacy_patterns.txt
```

3. 根据报告修正结构与索引：

- 更新 `index/topics.md`、`index/tags.md`、`index/glossary.md`
- 使用 `templates/note.md` 新建内容
- 保持文件命名 `kebab-case.md`

### 隐私规则维护 / Privacy Rules

若你有特定用户名、真实姓名、公司名等敏感信息，请追加到：
`skills/cs-foundations-maintainer/references/privacy_patterns.txt`

## 贡献方式 / Contributing

欢迎补充内容。提交前请运行隐私扫描。
Contributions are welcome. Please run the privacy scan before submitting.
