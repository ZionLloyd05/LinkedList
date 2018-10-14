from Node import Node
from LinkedList import LinkedList

def reverseList(self):

    nextNd = Node(0)
    currentNode = self.head
    prevNode = Node(None)

    while (currentNode != None):
        nextNd = currentNode.nextNode
        currentNode.nextNode = prevNode
        if(currentNode.data is not None):
            prevNode = currentNode
        
        currentNode = nextNd
        
    self.head = prevNode

def addOneToList(self):

    temp = Node(None)
    carry = 0
    currentNode = self.head
    count = 1
    while(currentNode != None):

        nodeData = currentNode.data
        if (nodeData != None):
            if (count == 1):
                summ = carry + nodeData + 1
            else:
                summ = carry + nodeData

            if(summ >= 10):
                summ = summ % 10
                carry = 1
            else:
                carry = 0

            #print("summ=> ", summ)
            #print("carry=> ", carry)
            currentNode.data = summ
            temp = currentNode
            count += 1
            currentNode = currentNode.nextNode
            
        else:
            break

    if(carry > 0):
        currentNode.nextNode = Node(carry)
        
    return currentNode

def recursiveReversal(self, currentNode, prevNode, nextNd):

    if(currentNode != None):
        nextNd = currentNode.nextNode
        currentNode.nextNode = prevNode
        if(currentNode):
            prevNode = currentNode
        currentNode = nextNd
        recursiveReversal(self, currentNode, prevNode, nextNd)
    else:
        self.head = prevNode

ListOne = LinkedList()

ListOne.insertStart(3)
ListOne.insertStart(2)
ListOne.insertStart(1)

print("---Linked List One---")
ListOne.traverseList()

print("\n---Reverse Linked List One---")
currentNode = ListOne.head
prevNode = Node(None)
nextNode = Node(None)

#print(nextNode.data)
recursiveReversal(ListOne, currentNode, prevNode, nextNode)

ListOne.traverseList()

#print("\n---add one to list---")
#addOneToList(ListOne)

#print("\n---Reverse Modified List One---")
#reverseList(ListOne)
#ListOne.traverseList()

#print("\n---Reversing modified List---")
#reverseList(ListOne)
