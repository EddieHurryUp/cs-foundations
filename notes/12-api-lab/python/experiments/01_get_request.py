import os
import sys
from pathlib import Path

import requests #快递公司

CURRENT_DIR = Path(__file__).resolve().parent
LIB_DIR = CURRENT_DIR.parent / "lib"
sys.path.append(str(LIB_DIR))

from http_debug import elapsed_ms, now_ms, pretty_json, print_response_summary


def main() -> None:
    url = "https://httpbin.org/get"
    params = {"topic": "api-lab", "step": "01"}
    headers = {"Accept": "application/json"}
    timeout = 5

    print(f"python={os.sys.version.split()[0]}")
    start = now_ms()
    resp = requests.get(url, params=params, headers=headers, timeout=timeout) # 核心
    cost = elapsed_ms(start)

    print_response_summary("GET", resp.url, resp.status_code, cost)
    print("response_headers_content_type=", resp.headers.get("Content-Type"))
    print(pretty_json(resp.json()))


if __name__ == "__main__":
    main()
