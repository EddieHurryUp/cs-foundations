import sys
from pathlib import Path

import requests

CURRENT_DIR = Path(__file__).resolve().parent
LIB_DIR = CURRENT_DIR.parent / "lib"
sys.path.append(str(LIB_DIR))

from http_debug import elapsed_ms, now_ms, pretty_json, print_response_summary


def main() -> None:
    url = "https://httpbin.org/post"
    payload = {
        "action": "create_user",
        "user": {"id": 1001,
                "name": "api-student",
                "profile":{
                    "age":18,
                    "home":"scihchuan",
                    "skills": ["python", "sql", "testing"]
                }
                
                },
    }
    headers = {"Content-Type": "application/json"}

    start = now_ms()
    resp = requests.post(url, json=payload, headers=headers, timeout=5) #核心
    cost = elapsed_ms(start)

    print_response_summary("POST", url, resp.status_code, cost)
    data = resp.json()
    print("server_echo_json=")
    print(pretty_json(data.get("json")))
    print("server_echo_headers_content_type=", data.get("headers", {}).get("Content-Type"))


if __name__ == "__main__":
    main()
