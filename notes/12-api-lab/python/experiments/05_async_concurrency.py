import asyncio
import time
import sys
from pathlib import Path

import httpx

CURRENT_DIR = Path(__file__).resolve().parent
LIB_DIR = CURRENT_DIR.parent / "lib"
sys.path.append(str(LIB_DIR))

from http_debug import pretty_json


async def fetch(client: httpx.AsyncClient, idx: int) -> dict:
    url = "https://httpbin.org/get"
    start = time.perf_counter()
    resp = await client.get(url, params={"job": idx})
    elapsed = int((time.perf_counter() - start) * 1000)
    return {
        "idx": idx,
        "status": resp.status_code,
        "elapsed_ms": elapsed,
        "url": str(resp.url),
    }


async def main() -> None:
    total = 20
    timeout = httpx.Timeout(5.0, connect=3.0)
    begin = time.perf_counter()

    async with httpx.AsyncClient(timeout=timeout) as client:
        tasks = [fetch(client, i) for i in range(total)]
        results = await asyncio.gather(*tasks)

    total_elapsed = int((time.perf_counter() - begin) * 1000)
    print(f"concurrency={total}, total_elapsed_ms={total_elapsed}")
    print(pretty_json(results))


if __name__ == "__main__":
    asyncio.run(main())
