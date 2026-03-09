# IPC Lab (macOS + zsh + Python 3)

This lab gives you runnable IPC examples:

- `01_pipe.py`: parent/child one-way communication with `multiprocessing.Pipe`
- `02_queue.py`: producer/consumer with `multiprocessing.Queue`
- `03_shared_memory_semaphore.py`: shared memory with semaphore synchronization
- `04_socket.py`: local TCP socket server/client communication

## Run

```bash
python3 notes/04-os/ipc-lab/01_pipe.py
python3 notes/04-os/ipc-lab/02_queue.py
python3 notes/04-os/ipc-lab/03_shared_memory_semaphore.py
python3 notes/04-os/ipc-lab/04_socket.py
```

## What to Observe

1. Data direction:
   Pipe and Queue send serialized messages.
2. Synchronization:
   Shared memory needs semaphore/lock to avoid races.
3. Scope:
   Socket works for local and remote processes.
