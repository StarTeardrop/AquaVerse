from AquaThread.BaseCallbackThread import *


class ImageDisplayThread(BaseCallbackWorker):
    def __init__(self, window_name="Image"):
        super().__init__(name=window_name)
        self.window_name = window_name

    def run(self):
        while self._running:
            with self._lock:
                img = self._data.copy() if self._data is not None else None

            if img is not None:
                cv2.imshow(self.window_name, img)
                cv2.waitKey(1)
            else:
                time.sleep(0.01)

        cv2.destroyWindow(self.window_name)
