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
    12-api-lab/
  problems/
    leetcode/
    interview/
  resources/
  assets/
  templates/
  skills/
```

## 学习地图 / Learning Map

- 入口地图：`notes/00-overview/learning-map.md`
- 目标：根据板块查缺补漏，按需新增笔记文件。

## 前端页面 / Web App

前端代码位于 `web/`，用于浏览 Markdown 内容。

```bash
cd web
npm install
npm run prepare-content
npm run dev
```

`prepare-content` 会同步 `notes/`、`index/` 和 `README.md` 到 `web/public/content/` 并生成目录清单。

### GitHub Pages 部署

推送到 `master` 后会自动构建并部署到 GitHub Pages。

## 协作与维护 / Collaboration & Maintenance

- 文件命名：优先使用 `kebab-case.md`。
- 新建笔记：使用 `templates/note.md` 作为起始模板。
- 索引维护：同步更新 `index/topics.md`、`index/tags.md`、`index/glossary.md`。

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
