#Minimax with Alpha Beta Pruning Pseudocode from: https://www.youtube.com/watch?v=zp3VMe0Jpf8

import queue
import uuid

def sanitize_id(id):
    return id.strip().replace(" ", "")

(_ADD) = range(3)
(_ROOT) = range(3)

class Node:
    def __init__(self, task, ID=None, expanded=True):
        self.__ID = (str(uuid.uuid1()) if ID is None else
                sanitize_id(str(ID)))
        self.task = task
        self.expanded = expanded #Gives children of current node
        self.__bpointer = None 
        self.__fpointer = [] 

    @property
    def ID(self):
        return self.__ID

    @property
    def bpointer(self):
        return self.__bpointer

    @bpointer.setter
    def bpointer(self, value):
        if value is not None:
            self.__bpointer = sanitize_id(value)

    @property
    def fpointer(self):
        return self.__fpointer

    def update_fpointer(self, ID, mode=_ADD):
        if mode is _ADD:
            self.__fpointer.append(sanitize_id(ID))
        elif mode is _DELETE:
            self.__fpointer.remove(sanitize_id(ID))
        elif mode is _INSERT:
            self.__fpointer = [sanitize_id(ID)]

class Tree:
    def __init__(self):
        self.nodes = []

    def getIndex(self, position):
        for index, node in enumerate(self.nodes):
            if node.ID == position:
                break
        return index

    def initNode(self, task, ID=None, parent=None):
        node = Node(task, ID)
        self.nodes.append(node)
        self.__update_fpointer(parent, node.ID, _ADD)
        node.bpointer = parent
        return node

    def isBranch(self, position):
        return self[position].fpointer

    def __update_fpointer(self, position, ID, mode):
        if position is None:
            return
        else:
            self[position].update_fpointer(ID, mode)

    def __update_bpointer(self, position, ID):
        self[position].bpointer = ID

    def __getitem__(self, key):
        return self.nodes[self.getIndex(key)]

    def minimax(self, position):
        value = 0
        alpha = 0
        beta = 0
        visitCount = 1
        answer = ""
        yield position
        
        '''
        rootNode = self[position].ID
        if self[position].task == "max":
            self.maximum(rootNode, alpha, beta, answer)
        elif self[position].task == "min":
            self.minimum(rootNode, alpha, beta, answer)
        '''
        
        queue = self[position].fpointer
        while queue:
            print("Assigned VALUE:   " + (queue[0]))
            print("Assigned TASK:    " + (self[queue[0]].task)) #Gives either MIN or MAX to determine function to use
            if queue[0].isdigit():
                leafVal = int(queue[0])
                if (leafVal > value):
                    value = leafVal
            expansion = self[queue[0]].fpointer #All nodes that are children of current node
            queue = expansion + queue[1:]
            print("CHILDREN:         " + str(expansion))
            print("QUEUE:            "  + str(queue))
            visitCount += 1

        print("="*80)
        print(visitCount) #Number of nodes visited
        print(value) #Final value

    '''
    def minimum(self, value, alpha, beta, answer, queue):
        print("minTEST")

    def maximum(self, value, alpha, beta, answer, queue):
        print(self[value].task)
        print("maxTEST")
    '''
        
def main():

    #idea here is that the assignments will be converted from text file to list of tuples. Seperating the two sets.
    #Still need to figure that out
    maxMinList = [("a","MAX"),("b","MIN"),("c","MIN"),("d","MAX"),("e","MAX"),("f","MAX"),("g","MAX")]
    pairList = [("A","B"),("A","C"),("B","D"),("B","E"),("C","F"),("C","G"),("D","4"),("D","3"),("E","2"),("E","7"),("F","3"),("F","2"),("G","2"),("G","8")]

    #Idea onwards is to get all the above and convert them to lowercase.
    
    #(task, ID, parent)
    #gameTree created in same order as in the example.
    gameTree = Tree()
    gameTree.initNode("max", "a")  #root
    gameTree.initNode("min", "b", parent = "a")
    gameTree.initNode("min", "c", parent = "a")
    gameTree.initNode("max", "d", parent = "b")
    gameTree.initNode("max", "e", parent = "b")
    gameTree.initNode("max", "f", parent = "c")
    gameTree.initNode("max", "g", parent = "c")
    gameTree.initNode("", "4", parent = "d")
    gameTree.initNode("", "3", parent = "d")
    gameTree.initNode("", "2", parent = "e")
    gameTree.initNode("", "7", parent = "e")
    gameTree.initNode("", "3", parent = "f")
    gameTree.initNode("", "2", parent = "f")
    gameTree.initNode("", "2", parent = "g")
    gameTree.initNode("", "8", parent = "g")

    #minimax with alphabeta prunning
    for node in gameTree.minimax("a"):
        print("")
    
main()
