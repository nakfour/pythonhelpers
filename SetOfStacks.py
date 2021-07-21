from classstack import Stack

class SetOfStacks():
    def __init__(self, limit=5):
        self.limit = limit
        self.stackOfStacks = Stack()
        self.stackOfStacks.insert(Stack())

    def pop(self):
        print("pop")
        if self.stackOfStacks.getSize() == 0:
            return False
        currentStack = self.stackOfStacks.remove()
        if currentStack.getSize() == 0:
            #currenStack is empty
            #pop next stack
            currentStack = self.stackOfStacks.remove()
            currentData = currentStack.remove()
            self.stackOfStacks.insert(currentStack)
            #push back again
            return currentData
        else:
            self.stackOfStacks.insert(currentStack)
            return currentStack.remove()


    def push(self,data):
        print("push")
        currentStack = self.stackOfStacks.remove()
        if currentStack.getSize() == self.limit:
            newStack = Stack()
            newStack.insert(data)
            self.stackOfStacks.insert(currentStack)
            self.stackOfStacks.insert(newStack)
        else:
            currentStack.insert(data)
            # need to queue back currentStack
            self.stackOfStacks.insert(currentStack)
        return True





