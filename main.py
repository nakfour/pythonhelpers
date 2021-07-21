# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from linkedlist import LinkedList
from doublelinkedlist import DoubleLinkedList
from classqueue import ClassQueue
from classstack import Stack
from classstack import StackWithMin
from SetOfStacks import SetOfStacks
from BinaryTreeTraversal import Node
from minheap import MinHeap
from trie import Trie
from graph import Graph
from projectdependency import projectdependency
from websocketsclass import websocketsclass
from websocketclientclass import wesocketsclientclass
from ransomnote import IsRansomNotePossible
from stringssubset import StringSubset
from FindMinimumSubs import MinSub



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    newLinkedList = LinkedList()
    # given 4,5,1,9
    # We need to create a pointer at 5 and not use the head
    newLinkedList.insert("4")
    newLinkedList.insert("5")
    newLinkedList.insert("1")
    newLinkedList.insert("9")



    # Given the head of a linked list, remove the nth node from the start of the list and return its head.
    # For example delete 2nd node, return head.
    nodeNumber = 2
    #runnerHead = newLinkedList.getHead()
    #count = 0
    #get to the node before the one needed to be deleted
    #while count < nodeNumber - 1:
      #  runnerHead.set_next(runnerHead.get_next())
     #   print(runnerHead.get_data())
    #    count += 1
    #runnerHead.set_next(runnerHead.get_next().get_next())
    # test next element
    #nextNode = runnerHead.get_next()
    #print(nextNode.get_data())

    # Given the head of a linked list, remove the nth node from the end of the list and return its head.
    # For example delete nth node is n=2, we delete the second from the end
    #Input: head = [1,2,3,4,5], n = 2
    #Output: [1,2,3,5]

    #Step 1 get the length of the list
    runnerHead = newLinkedList.getHead()
    count = 0
    while runnerHead.get_next() is not None:
        #runnerHead.set_next(runnerHead.get_next().get_next())
        runnerHead = runnerHead.get_next()
        count += 1
    print(count)

    # Need to delete length -n + 1 = 3+1= 4 -2 =2, need to delete item in index 2 starting from 0
    deletePosition = count + 1 - nodeNumber
    print(deletePosition)
    counter = 0
    runnerHead = newLinkedList.getHead()
    while counter < deletePosition - 1:
        runnerHead = runnerHead.get_next()
        counter += 1
    print(runnerHead.get_data())
    #delete the next node
    runnerHead.set_next(runnerHead.get_next().get_next())
    print(runnerHead.get_next().get_data())

    doubleList = DoubleLinkedList()
    doubleList.insert("3")
    doubleList.insert("4")
    doubleList.insert("5")
    doubleList.insert("6")
    doubleList.insert("7")

    print(doubleList.delete("5"))

    #Queue
    newQueue = ClassQueue(2)
    newQueue.addData("string1")
    print(newQueue.addData("String2"))
    print(newQueue.addData("String3"))
    for i in range(4):
        print(newQueue.dequeuData())

    # Animal Shelter that takes cats and dogs
    # Customers can pick cat or dog but need to take the oldest in
    # Or pick randon oldest.
    # Solution use one queue to place animals in order for first in first out
    # use a stack when customers ask for a cat or dog that is not at the top of the queue
    # offload animals from queue to another queue it matches whats requested,
    # another option is to to have two queues one for dog and one for cat with time stamps

    # every shelter has a capacity and the max number of the queue is that capacity
    animalQueue = ClassQueue(100)
    tempQueue = ClassQueue(100)
    animalQueue.addData("Cat1")
    animalQueue.addData("Dog2")
    animalQueue.addData("Cat3")
    animalQueue.addData("Dog4")
    animalQueue.addData("Dog5")
    animalQueue.addData("Cat6")
    animalQueue.addData("Dog7")


    # Guest asks for random animal
    print(animalQueue.dequeuData())

    #Guest asks for a cat
    found = False

    while not found:
        animalTemp = animalQueue.dequeuData()
        if 'Cat' in animalQueue.dequeuData():
            found = True
        else:
            # add animal Temp to stack
            tempQueue.addData(animalTemp)
    #empty the rest of the list
    while not animalQueue.isQueueEmpty():
        tempQueue.addData(animalQueue.dequeuData())
    #repopulate the list
    while not tempQueue.isQueueEmpty():
        animalQueue.addData(tempQueue.dequeuData())
    # pop all elements in stack and place them in queue again

    #Stack implementation
    mystack = StackWithMin()
    mystack.insert(1)
    mystack.insert(2)
    mystack.insert(3)
    mystack.insert(55)
    print(mystack.getLowestData())
    print(mystack.remove())
    print(mystack.remove())
    print(mystack.remove())
    print(mystack.getLowestData())
    #SetOfStackProblem
    currentSetOfStack = SetOfStacks(3)
    currentSetOfStack.push("1")
    currentSetOfStack.push("2")
    currentSetOfStack.push("3")
    currentSetOfStack.push("4")
    currentSetOfStack.push("5")
    currentSetOfStack.push("6")

    print(currentSetOfStack.pop())
    print(currentSetOfStack.pop())
    print(currentSetOfStack.pop())
    print(currentSetOfStack.pop())
    print(currentSetOfStack.pop())
    print(currentSetOfStack.pop())

    #Binary Tree Traversal
    newBinaryTreeTraversal = Node("1")
    newBinaryTreeTraversal.insert("2")
    newBinaryTreeTraversal.insert("3")
    newBinaryTreeTraversal.insert("4")
    newBinaryTreeTraversal.insert("5")
    newBinaryTreeTraversal.insert("6")
    newBinaryTreeTraversal.insert("7")
    newBinaryTreeTraversal.insert("8")
    newBinaryTreeTraversal.insert("9")
    print("Tree")
    newBinaryTreeTraversal.PrintTree()
    print("Inorder")
    newBinaryTreeTraversal.inorderTraversal(newBinaryTreeTraversal)
    print("postorder")
    newBinaryTreeTraversal.postorderTraversal(newBinaryTreeTraversal)
    print("preorder")
    newBinaryTreeTraversal.preorderTraversal(newBinaryTreeTraversal)
    print("Is tree balanced")
    print(newBinaryTreeTraversal.checkHeight(newBinaryTreeTraversal))
    print("Arry to BTS")
    someData = [1,2,3,4,5,6,7]
    newTree= newBinaryTreeTraversal.convertArrayToBinaryTreeSearch(someData)
    newTree.PrintTree()
    print("Is tree BTS balanced")
    print(newTree.checkHeight(newTree))
    #Check if BTS
    print("check if BTS")
    print(newTree.checkBTS(newTree))
    print("Check if BTS")
    print(newTree.checkBTS(newBinaryTreeTraversal))




    #MinHeap
    myminheap = MinHeap(5)
    myminheap.insert("44")
    myminheap.insert("45")
    myminheap.insert("10")
    myminheap.insert("0")

    #Trie
    myTrie = Trie()
    myTrie.insert("was")
    myTrie.insert("where")
    myTrie.insert("what")
    print(myTrie.query("wh"))

    #Graph
    mygraph = Graph()
    mygraph.addEdge(0,1)
    mygraph.addEdge(0,2)
    mygraph.addEdge(0, 3)
    mygraph.addEdge(2, 4)
    mygraph.addEdge(4, 5)
    mygraph.addEdge(4, 6)
    mygraph.addEdge(6, 1)
    mygraph.BFS(0)
    print("DFS")
    mygraph.DFS(0)
    print(mygraph.routeExist(2,3))

# Websockets Server
    #mywebsocket= websocketsclass()
    #mywebsocket.startServer()

# Websocket Client
    #myclient = websocketclientclass()
    #myclient.startClient("ws://localhost:8765")
#RansomNoteFrom Magazine
    myransomenote = IsRansomNotePossible()
    print(myransomenote.returnPossiblity("The is blue tonight", "blue sky"))


    # Is one String a subset of another
    myStringTest = StringSubset()
    print(myStringTest.IsStringASubset("hello", "g"))

    #find the miinimum subtraction between array elements
    a=[-4,4,2,0,-4]
    mymin = MinSub()
    print(mymin.findMinimium(a))



















