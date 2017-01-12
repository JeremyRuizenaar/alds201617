__author__ = 'jer'


import random

class MyHashTable:

    def __init__(self, length):
        self.used = 0
        self.len = length
        self.table = [None] * length

    def search(self, e):
        h = e.value % self.len
        if self.table[int(h)] is not None:
            return self.table[int(h)].search(e)
        return False

    def insert(self, e):
        h = e.value % self.len
        if self.table[int(h)] is not None:
            self.table[int(h)].insert(e.value)
        else:
            self.table[int(h)] = e
        self.used += 1
        if self.used > self.len * 0.75:
            self.rehash()

    def delete(self, e):
        if self.search(e):
            h = e.value % self.len
            if self.table[int(h)].value == e.value:
                self.table[int(h)] = self.table[int(h)].next
            else:
                self.table[int(h)].delete(e)
            self.used -= 1
            if self.used > self.len * 0.75:
                self.rehash()

    def __repr__(self):
        r = ""
        for i in range(len(self.table)):
            if self.table[i] is not None:
                r += self.table[i].__repr__()
            else:
                r + "- \n"
        return r

    def rehash(self):
        old_len = self.len
        old_table = self.table
        self.len = old_len * 2
        self.table = [None] * self.len
        self.used = 0

        print("new table")

        for i in range(old_len):
            if old_table[i] is not None:
                elem = old_table[i]
                temp = []
                while elem.next is not None:
                    temp.append(elem.next.value)
                    elem = elem.next
                elem.next = None
                self.insert(elem)
                for val in temp:
                    self.insert(Entry(val))
        print("used " + str(self.used))
        print("---------")

        print(self.__repr__())



class Entry:

    def __init__(self, element):
        self.value = element
        self.next = None

    def __repr__(self):
        if self.next is not None:
            return str(self.value) + " -> " + str(self.next.__repr__())
        return str(self.value) + " \n"

    def insert(self, e):
        if self.next is None:
            self.next = Entry(e)
        else:
            self.next.insert(e)

    def search(self, e):
        if self.value == e:
            return True
        else:
            if self.next is not None:
                return self.next.search(e)
            else:
                return False

    def delete(self, e):
        if self.next.value == e.value:
            self.next = self.next.next
        else:
            self.next.delete(e)

myHashTable = MyHashTable(10)
numbersF = [random.uniform(0, 100) for _ in range(200)]

for number in numbersF:
    #print("inserting" + str(number))
    myHashTable.insert(Entry(number))
print("table filled")
print(myHashTable.used)
print(myHashTable.__repr__())