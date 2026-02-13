---
title: API 实验室目录说明
tags: [api, python, learning]
level: intro
updated: 2026-02-14
---

# API 实验室目录说明

- `api-lab-learning-map.md`：学习路线与实验顺序
- `python-debug-playbook.md`：Python 调试步骤与排查
- `experiment-log-template.md`：实验复盘模板
- `learning-summary-round-1.md`：第 1 轮实验总结
- `python/experiments/`：可运行代码实验
- `python/lib/`：实验共用工具函数

## 建议学习顺序

1. 先看：`api-lab-learning-map.md`
2. 再跑：`python/experiments/01_get_request.py` 到 `05_async_concurrency.py`
3. 每跑完一个实验，填写：`experiment-log-template.md`
4. 最后复盘：`learning-summary-round-1.md`

## 快速开始

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r notes/12-api-lab/python/requirements.txt
python3 notes/12-api-lab/python/experiments/01_get_request.py
```

## 一次性运行 5 个实验

```bash
python3 notes/12-api-lab/python/experiments/01_get_request.py
python3 notes/12-api-lab/python/experiments/02_post_json.py
python3 notes/12-api-lab/python/experiments/03_auth_header.py
python3 notes/12-api-lab/python/experiments/04_timeout_retry.py
python3 notes/12-api-lab/python/experiments/05_async_concurrency.py
```
