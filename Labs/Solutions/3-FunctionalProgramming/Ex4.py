class Node:

    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self) :
        self.head = None

        
    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            self.doAdd(self.head, newNode)

        
    def doAdd(self, currNode, newNode):
        if newNode.data < currNode.data:
            if currNode.left is None:
                currNode.left = newNode
            else:
                self.doAdd(currNode.left, newNode)
        else:
            if currNode.right is None:
                currNode.right = newNode
            else:
                self.doAdd(currNode.right, newNode)

        
    def display(self):
        if self.head is None:
            print("Empty tree")
        else:
            self.doDisplay(self.head)


    def doDisplay(self, currNode):

        if currNode.left is not None:
            self.doDisplay(currNode.left)

        print(currNode.data)
        
        if currNode.right is not None:
            self.doDisplay(currNode.right)

        
if __name__ == "__main__" :

    tree = BinaryTree()
    tree.add("ManU")
    tree.add("Liverpool")
    tree.add("Swansea")
    tree.add("Chelsea")
    tree.add("ManC")
    tree.add("QPR")
    tree.add("Wolves")
    tree.add("Cardiff")
    
    tree.display()
    