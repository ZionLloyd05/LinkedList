from Node import Node
from LinkedList import LinkedList

def AddTwoLL(firstList, secondList):

    res = Node(None)
    prev = Node(None)
    temp = Node(None)
    
    first = firstList.head
    second = secondList.head

    print("first_data=> ", first.data)
    print("second_data=> ", second.data)
    carry = 0

    while (first is not None or second is not None):
        dataFirst = 0
        dataSecond = 0

        #print("\n")
        if(first is not None):
            dataFirst = first.data
            #print("dataFirst=> ", dataFirst)

        if(second is not None):
            dataSecond = second.data
            #print("dataSecond=> ", dataSecond)

        sumData = carry + dataFirst + dataSecond
        #print("sumData_atFirst=> ", sumData)

        if(sumData >= 10):
            carry = 1
        else:
            carry = 0
        #print("carry=> ", carry)

        sumData = sumData % 10
        #print("real_sumData=> ", sumData)
        temp = Node(sumData)
        
        if(res.data == None):
            res = temp
            #print("res empty")
        else:
            prev.nextNode = temp
            #print("res not empty")

        prev = temp

        if(first):
            first = first.nextNode

        if(second):
            second = second.nextNode

    if(carry > 0):
        temp.nextNode = Node(carry)

    print("\nresult-----")
    while(res is not None):
        print(res.data)
        res = res.nextNode

ListOne = LinkedList()

ListOne.insertStart(9)
ListOne.insertStart(9)
ListOne.insertStart(7)
ListOne.insertStart(5)
print("---Linked List One---")
ListOne.traverseList()


ListTwo = LinkedList()

ListTwo.insertStart(9)
ListTwo.insertStart(1)
ListTwo.insertStart(7)
print("---Linked List Two---")
ListTwo.traverseList()

print("\n--On Adding the two---")
AddTwoLL(ListOne, ListTwo)
