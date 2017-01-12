__author__ = 'jer'
class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyCircularLinkedList:
    def __init__(self):
        #self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.tail
        holdCurrent = self.tail

        if current != None:
            s = s + str(current)
            current = current.next
        while current != holdCurrent:
            s = s + " -> " + str(current)
            current = current.next

        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.head == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,None)
            n.next = self.tail.next
            self.tail.next = n
            self.tail = n



    def delete(self,e):
        if self.tail:
            if id(self.tail) == id(self.tail.next):
                if self.tail.data == e:
                    self.tail = None

            elif self.tail.data == e and self.tail.next.data == e:
                current = self.tail
                captureCurrent = self.tail
                if current.next.data == e:
                    current.next = current.next.next
                    return
                else:
                    current = current.next

                while  current.next.data != e  and current != captureCurrent:
                    current = current.next

                if current.next.data == e:
                    current.next = current.next.next
                    return


            elif self.tail.data == e:
                 self.tail = self.tail.next
                 self.delete(e)

            else:
                current = self.tail
                captureCurrent = self.tail
                if current.next.data == e:
                    current.next = current.next.next
                    return
                else:
                    current = current.next

                while  current.next.data != e  and current != captureCurrent:
                    current = current.next
                if current.next.data == e:
                    current.next = current.next.next
                    return
                if current == captureCurrent:
                    print("element not detected")
                    return

        else:
            print("cant delete list empty ")


if __name__ == '__main__':
    print("starting....")
    mylist =  MyCircularLinkedList()



    mylist.addLast(6)
    mylist.addLast(6)
    mylist.addLast(6)
    mylist.addLast(2)
    mylist.addLast(3)
    mylist.addLast(4)

    print(mylist)

    mylist.delete(4)
    print(mylist)
    mylist.delete(3)
    print(mylist)
    mylist.addLast(5)
    print(mylist)
    mylist.delete(2)
    print(mylist)
    mylist.delete(5)
    print(mylist)
    mylist.delete(6)
    print(mylist)
    mylist.delete(6)
    print(mylist)
    mylist.delete(6)
    print(mylist)




