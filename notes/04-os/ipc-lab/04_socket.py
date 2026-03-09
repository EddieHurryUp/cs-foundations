#!/usr/bin/env python3
from multiprocessing import Process
import socket
import time


HOST = "127.0.0.1"
PORT = 50555


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[server] listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"[server] connected by {addr}")
            data = conn.recv(1024)
            msg = data.decode("utf-8")
            print(f"[server] received: {msg}")
            conn.sendall(f"ack:{msg}".encode("utf-8"))


def client():
    time.sleep(0.2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        payload = "hello-from-client123"
        print(f"[client] send: {payload}")
        s.sendall(payload.encode("utf-8"))
        data = s.recv(1024)
        print(f"[client] recv: {data.decode('utf-8')}")


def main():
    p_server = Process(target=server)
    p_client = Process(target=client)
    p_server.start()
    p_client.start()
    p_client.join()
    p_server.join()


if __name__ == "__main__":
    main()
