

from classqueue import ClassQueue

class GraphNode:
    def __init__(self, data):
        self.children = []
        self.data = data

    def getData(self):
        return self.data
    def getChildren(self):
        return self.children
    def addChild(self, data):
        self.children.append(data)


class projectdependency(object):
    def __init__(self, projectList, projectdependency):
        self.projects = projectList
        self.projectdep = projectdependency
        self.nodellist=[]


    def getDependency(self):
        self.createGraph()
        return self.traverseGraph()

    def createGraph(self):

        # Create a Node for each element
        for element in self.projects:
            self.nodelllist.append(GraphNode(element))


        # Read dependency and create arrows, A---> B, means A has to finish before B can run
        for dep in self.projectdep:
            # find dep[1] in nodelist and add it to graph of dep[0]
            for node in self.nodellist:
                if node.getData() == dep[0]:
                    dep[1].children.append[node]

    def traverseGraph():
        projectOrder = ClassQueue(len(self.projects))
        # find nodes with no arrow pointing at them and add them to the queue
        while (len(self.nodellist)) > 0 :
            for node in self.nodellist:
                if len(node.getChildren()) <= 0:
                    projectOrder.addData(node.data)
                    # remove from nodellist
                    self.nodellist.remove(node)
                    # remove it from childrens of other nodes
                    for n in self.nodellist:
                        for child in n.getChildren():
                            if child == node.getData:
                                n.removeChild(child)






