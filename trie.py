#ATrie is a tree that starts with a "*" root node, then leaves with letters to for a word. Traverse order is O(m) where m is the length of the
# word
class TrieNode:

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        # a dictionary of child nodes
        self.children = {}


class Trie(object):
    def __init__(self):
        #The root is always a * char node
        self.root = TrieNode("*")

    def insert(self, word):
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Create an * node to mark end of word
        new_node = TrieNode("*")
        node.children[char] = new_node
        node = new_node

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.char == "*":
            self.output.append((prefix, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix+node.char)

    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []

        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)