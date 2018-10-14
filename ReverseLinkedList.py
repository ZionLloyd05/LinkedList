from LinkedList import LinkedList
from Node import Node

def reverse(self):
    headRef = self.head

    #print(headRef.data)
    prevNode = Node(None)
    currentNode = self.head
    #print("head at first=> ", self.head)
    nextNd =Node(0)
    counter = 0
    while currentNode is not None:
        counter += 1
        #print("\nLoop %d--------\n" % counter)

        #if(currentNode is not None):
            #print("curr_before=> ", currentNode.data)
        #else:
            #print("curr_before=> None")
            
        nextNd = currentNode.nextNode
        
        currentNode.nextNode = prevNode

        #print("prev_before=> ",prevNode.data)
        prevNode = currentNode

        #print("curr_nextNode=> ", currentNode.nextNode.data)

        currentNode = nextNd
        
        #print("prev_after=> ",prevNode.data)

        #if(currentNode is not None):
            #print("curr_before=> ", currentNode.data)
        #else:
            #print("curr_before=> None")

        #if(nextNd is not None):
            #print("next_after=> ", nextNd.data)
        #else:
            #print("next_after=> None") 

    self.head = prevNode
    
    #print("head at last=> ", self.head.data)

    print("\n-----after reversal----")
    while self.head is not None:
        print(self.head.data);
        self.head = self.head.nextNode

LinkedList = LinkedList()

#LinkedList.insertEnd(10)
#LinkedList.insertEnd(20)
#LinkedList.insertEnd(30)

LinkedList.insertStart(5)
LinkedList.insertStart(4)
LinkedList.insertStart(3)
LinkedList.insertStart(2)
LinkedList.insertStart(1)
#print("----Original LinkedList-----")
#LinkedList.traverseList()

#newList = reverse(LinkedList)
#print("\n----after reversal-----")



