import time
import sys
from pathlib import Path

import requests

CURRENT_DIR = Path(__file__).resolve().parent
LIB_DIR = CURRENT_DIR.parent / "lib"
sys.path.append(str(LIB_DIR))

from http_debug import elapsed_ms, now_ms, print_response_summary


def get_with_retry(url: str, retries: int = 3, timeout: float = 1.0) -> None:
    for attempt in range(1, retries + 1):
        start = now_ms()
        try:
            resp = requests.get(url, timeout=timeout)
            cost = elapsed_ms(start)
            print_response_summary("GET", url, resp.status_code, cost)
            if resp.status_code < 500:
                print(f"success on attempt={attempt}")
                return
            print(f"server error, attempt={attempt}")
        except requests.Timeout:
            cost = elapsed_ms(start)
            print(f"timeout on attempt={attempt}, elapsed_ms={cost}")
        except requests.RequestException as exc:
            print(f"request error on attempt={attempt}: {exc}")

        if attempt < retries:
            backoff = 2 ** (attempt - 1)
            print(f"sleep {backoff}s before next retry")
            time.sleep(backoff)

    print("failed after retries")


def main() -> None:
    delayed_url = "https://httpbin.org/delay/2"
    print("expect timeout due to timeout=1.0")
    get_with_retry(delayed_url, retries=3, timeout=2.48)


if __name__ == "__main__":
    main()
