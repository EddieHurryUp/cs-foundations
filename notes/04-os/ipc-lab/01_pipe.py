#!/usr/bin/env python3
from multiprocessing import Pipe, Process
import os
import time


def child(recv_end):
    print(f"[child] pid={os.getpid()}, ppid={os.getppid()}")
    msg = recv_end.recv()
    print(f"[child] received: {msg}")
    recv_end.close()


def main():
    print(f"[parent] pid={os.getpid()}, ppid={os.getppid()}")
    recv_end, send_end = Pipe(duplex=False)
    p = Process(target=child, args=(recv_end,))
    p.start()

    payload = {"type": "task", "id": 1, "content": "learn pipe"}
    time.sleep(2)
    print(f"[parent] sending: {payload}")
    time.sleep(2)
    send_end.send(payload)
    send_end.close()

    p.join()
    print("[parent] done")


if __name__ == "__main__":
    main()
