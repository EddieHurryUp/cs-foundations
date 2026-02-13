---
title: API 实验学习地图（Python）
tags: [api, http, rest, debug, python]
level: core
updated: 2026-02-14
---

# API 实验学习地图（Python）

目标：通过小型代码实验理解 API 的使用方式与底层机理，而不是只记调用方法。

## 环境准备

- [x] 安装 Python 3.11+
- [x] 创建虚拟环境并激活
- [x] 安装依赖：`pip install -r notes/12-api-lab/python/requirements.txt`

## 实验顺序

- [x] `01_get_request.py`：最小 GET，请求/响应结构
- [x] `02_post_json.py`：JSON 请求体与响应解析
- [x] `03_auth_header.py`：认证头（Bearer Token）与 401 场景
- [x] `04_timeout_retry.py`：超时、重试、退避
- [x] `05_async_concurrency.py`：并发请求与吞吐差异

## 每次实验固定观察项

- [x] URL、Method、Headers、Body
- [x] Status Code、Response Headers、Response Body
- [x] 总耗时、失败类型（超时/连接错误/4xx/5xx）
- [x] 重试次数与最终结果

## 机理理解主线

- 请求是如何从客户端发出并等待响应的
- 状态码如何表达语义（成功、客户端错误、服务端错误）
- 为什么需要超时与重试策略
- 为什么并发模型会影响吞吐和资源占用

## 实验记录

每个实验执行后复制模板填写：`notes/12-api-lab/experiment-log-template.md`

## 本轮产出

- 学习总结：`notes/12-api-lab/learning-summary-round-1.md`

## Round 2 计划

- [ ] 本地 Mock API 实验（降低公网依赖）
- [ ] 并发实验补充成功率/失败率/P95
- [ ] 使用 `pytest` 固化回归实验
