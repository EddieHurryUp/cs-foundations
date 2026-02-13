import sys
from pathlib import Path

import requests

CURRENT_DIR = Path(__file__).resolve().parent
LIB_DIR = CURRENT_DIR.parent / "lib"
sys.path.append(str(LIB_DIR))

from http_debug import elapsed_ms, now_ms, pretty_json, print_response_summary


def request_with_token(token: str) -> None:
    url = "https://httpbin.org/bearer"
    headers = {"Authorization": f"Bearer {token}"}
    start = now_ms()
    resp = requests.get(url, headers=headers, timeout=5)
    cost = elapsed_ms(start)

    print_response_summary("GET", url, resp.status_code, cost)
    try:
        print(pretty_json(resp.json()))
    except ValueError:
        print(resp.text[:200])


def main() -> None:
    print("case_1: token is empty (expect 401)")
    request_with_token("")
    print("-" * 40)
    print("case_2: token is non-empty (expect 200)")
    request_with_token("demo-token")


if __name__ == "__main__":
    main()
