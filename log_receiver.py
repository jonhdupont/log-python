from multiprocessing.managers import BaseManager

class LogQueueManager(BaseManager): pass
LogQueueManager.register('get_queue')

def log_viewer(queue):
    print("=== [FENÊTRE DE LOGS EN TEMPS RÉEL] ===")
    while True:
        msg = queue.get()
        if msg == "__EXIT__":
            break
        print(msg)

if __name__ == "__main__":
    manager = LogQueueManager(address=('localhost', 50000), authkey=b'abc')
    manager.connect()
    queue = manager.get_queue()
    log_viewer(queue)