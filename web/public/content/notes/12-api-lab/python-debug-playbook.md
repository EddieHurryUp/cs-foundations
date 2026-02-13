---
title: Python API 调试手册
tags: [api, debug, python, http]
level: core
updated: 2026-02-14
---

# Python API 调试手册

## 1. 先看最关键信息

- 请求：`method + url + headers + body`
- 响应：`status_code + headers + text/json`
- 时延：请求开始到结束的耗时

## 2. 推荐实践

- 给每个请求设置超时（避免无穷等待）
- 显式打印关键信息（先不要过度抽象）
- 区分异常类型（超时、连接失败、HTTP 错误）
- 对可重试错误设置指数退避
- 让日志跟真实参数一致（不要写死提示文案）

## 3. 运行方式

```bash
python3 notes/12-api-lab/python/experiments/01_get_request.py
python3 notes/12-api-lab/python/experiments/02_post_json.py
python3 notes/12-api-lab/python/experiments/03_auth_header.py
python3 notes/12-api-lab/python/experiments/04_timeout_retry.py
python3 notes/12-api-lab/python/experiments/05_async_concurrency.py
```

## 4. 本轮关键结论（Round 1）

- `httpbin` 是回显服务，适合对账请求，不等于真实业务接口
- `GET` 主要用 query params，`POST` 主要用 JSON body
- `Authorization: Bearer <token>` 是最常见认证头
- timeout 不应理解成“整次请求绝对上限”
- 并发总耗时通常接近最慢请求耗时，而不是单次耗时总和

## 5. 常见错误排查

- `ConnectionError`：先确认网络、域名、代理
- `Timeout`：增加 timeout、检查服务端延迟
- `401/403`：检查 token 是否缺失或过期
- `429`：触发限流，需退避或降低并发
- `5xx`：服务端错误，优先重试并保留日志

## 6. 最小排查顺序

1. 看 `status_code`
2. 看 `response body`（错误详情）
3. 看请求参数与请求头是否正确
4. 看 timeout/retry 配置是否合理
5. 再看并发和限流因素
