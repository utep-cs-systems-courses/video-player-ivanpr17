import threading,cv2,base64,queue
import numpy as np

framesQueueLock = threading.Lock()

class producerConsumerQueue():
    def __init__(self):
        self.fullSem = threading.Semaphore(0)
        self.emptySem = threading.Semaphore(10)
        self.framesQueue = queue.Queue()

    def insert(self,frame):
        self.emptySem.acquire()
        framesQueueLock.acquire()
        self.framesQueue.put(frame)
        framesQueueLock.release()
        self.fullSem.release()

    def remove(self):
        self.fullSem.acquire()
        framesQueueLock.acquire()
        frame = self.framesQueue.get()
        framesQueueLock.release()
        self.emptySem.release()
        return frame

    def empty(self):
        framesQueueLock.acquire()
        isEmpty = self.framesQueue.empty()
        framesQueueLock.release()
        return isEmpty
