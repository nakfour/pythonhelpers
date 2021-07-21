class DoubleNode(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev

class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def getHead(self):
        return self.head

    def insert(self, data):
        new_node = DoubleNode(data)
        new_node.set_next(self.head)
        if self.head is not None:
            self.head.set_prev(new_node)
        self.head = new_node

    def getSize(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            return "Data not in list"
        else:
            return current

    def delete(self, data):
        traverse = self.head
        found = False
        while traverse and found is False:
            if traverse.get_data() == data:
                found = True
            else:
                traverse = traverse.get_next()
        # If we got to the end and we found nothing
        if traverse is None:
            return "Data not in list"
        else:
            #Need to delete the node traverse is pointing at
            traverse.get_prev().set_next(traverse.get_next())
            traverse.get_next().set_prev(traverse.get_prev())
            return "Delete Success"







