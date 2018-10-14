from Node import Node

class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.counter = 0;

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print(actualNode.data);
            actualNode = actualNode.nextNode;


    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def insertEnd(self, data):
        self.counter += 1
        actualNode = self.head
        
        if actualNode is None:
            self.insertStart(data)
            return
        
        newNode = Node(data)

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode;

    def getSize(self):
        return self.counter;

    def remove(self, data):
        self.counter -= 1

        actualNode = self.head
        if(actualNode.data == data):
            actualNode = actualNode.nextNode
        else:
            actualNode.remove(data, actualNode)
        
    
