class Stack(object):
    def __init__(self):
        self.dataStack = []
        self.size = 0

    def insert(self, data):
        #first element
        self.dataStack.append(data)
        self.size += 1

    def remove(self):
        self.size -= 1
        return self.dataStack.pop()

    def getSize(self):
        return self.size

    def decSize(self):
        self.size -= 1


class StackWithMin(Stack):
    def __init__(self):
        self.loweStack = Stack()
        self.lowestData = 0
        Stack.__init__(self)

    def insert(self, data):
        if Stack.getSize(self) == 0:
            self.lowestData = data
            #self.loweStack.insert(data)
        elif data < self.lowestData:
            self.loweStack.insert(self.lowestData)
            self.lowestData = data

        Stack.insert(self,data)

    def remove(self):
        if Stack.getSize(self) > 0:
            Stack.decSize(self)
        else:
            return False
        deletedElement = self.dataStack.pop()
        if deletedElement == self.lowestData:
            self.lowestData = self.loweStack.remove()
        return deletedElement

    def getLowestData(self):
        return self.lowestData