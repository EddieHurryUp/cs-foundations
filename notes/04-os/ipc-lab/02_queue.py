#!/usr/bin/env python3
from multiprocessing import Process, Queue
import os
import time


def producer(q):
    for i in range(5):
        msg = f"job-{i}"
        print(f"[producer pid={os.getpid()}] put: {msg}")
        q.put(msg)
        time.sleep(1)
    # Two consumers need two stop signals.
    q.put(None)
    q.put(None)


def consumer(name, q):
    print(f"[consumer-{name} pid={os.getpid()}] start")
    while True:
        item = q.get()
        if item is None:
            print(f"[consumer-{name} pid={os.getpid()}] stop")
            break
        print(f"[consumer-{name} pid={os.getpid()}] got: {item}")


def main():
    print(f"[parent pid={os.getpid()}] start")
    q = Queue()
    p_producer = Process(target=producer, args=(q,))
    p_consumer_a = Process(target=consumer, args=("A", q))
    p_consumer_b = Process(target=consumer, args=("B", q))
    p_producer.start()
    p_consumer_a.start()
    p_consumer_b.start()
    p_producer.join()
    p_consumer_a.join()
    p_consumer_b.join()
    print(f"[parent pid={os.getpid()}] done")


if __name__ == "__main__":
    main()
