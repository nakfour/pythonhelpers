from queue import Queue

class ClassQueue (object):
    def __init__(self, size):
        self.size = size
        self.numberOfElements = 0
        self.iQueue = Queue(maxsize=size)

    def addData(self, data):
        if self.iQueue.full():
            return False
        else:
            self.iQueue.put(data)
            self.numberOfElements += 1
            return True

    def dequeuData(self):
        if self.iQueue.empty():
            return False
        else:
            self.numberOfElements -= 1
            return self.iQueue.get()

    def getnumberOfElements(self):
        return self.numberOfElements

    def isQueueEmpty(self):
        return self.iQueue.empty()

    def isQueueFull(self):
        return self.iQueue.full()

