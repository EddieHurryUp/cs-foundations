#!/usr/bin/env python3
from multiprocessing import Process, Semaphore
from multiprocessing.shared_memory import SharedMemory
import struct
import time


INT_SIZE = 4
COUNT = 10


def writer(shm_name, sem):
    shm = SharedMemory(name=shm_name)
    try:
        for i in range(COUNT):
            with sem:
                shm.buf[i * INT_SIZE : (i + 1) * INT_SIZE] = struct.pack("i", i * 10)
                print(f"[writer] write index={i}, value={i * 10}")
            time.sleep(0.05)
    finally:
        shm.close()


def reader(shm_name, sem):
    shm = SharedMemory(name=shm_name)
    try:
        for i in range(COUNT):
            with sem:
                data = bytes(shm.buf[i * INT_SIZE : (i + 1) * INT_SIZE])
                value = struct.unpack("i", data)[0]
                print(f"[reader] read index={i}, value={value}")
            time.sleep(0.08)
    finally:
        shm.close()


def main():
    shm = SharedMemory(create=True, size=COUNT * INT_SIZE)
    sem = Semaphore(1)
    try:
        p1 = Process(target=writer, args=(shm.name, sem))
        p2 = Process(target=reader, args=(shm.name, sem))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
    finally:
        shm.close()
        shm.unlink()


if __name__ == "__main__":
    main()
