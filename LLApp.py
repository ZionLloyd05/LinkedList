from LinkedList import LinkedList

LinkedList = LinkedList()

LinkedList.insertEnd(10)
LinkedList.insertEnd(20)
LinkedList.insertEnd(30)

LinkedList.insertStart(5)
LinkedList.insertStart(6)
LinkedList.insertStart(3)
print("-----before removal")
LinkedList.traverseList()

print(LinkedList.getSize())

LinkedList.remove(6)

print("-----after removal")
LinkedList.traverseList()

print(LinkedList.getSize())
