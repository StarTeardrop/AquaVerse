import threading
import time
import numpy as np
import cv2

class BaseCallbackWorker(threading.Thread):
    def __init__(self, name="WorkerThread"):
        super().__init__()
        self.name = name
        self._running = True
        self._lock = threading.Lock()
        self._data = None

    def update_data(self, data):
        with self._lock:
            self._data = data

    def stop(self):
        self._running = False

    def run(self):
        raise NotImplementedError("run() must be implemented in subclasses")


