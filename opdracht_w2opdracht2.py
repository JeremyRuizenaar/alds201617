__author__ = 'jer'

class MyStack(list):

    def push(self, a): # klasse-methode
        self.list.append(a)

    def pop(self): # klasse-methode
        x = self.list[-1]
        del self.list[-1]
        return x


    def peek(self): # klasse-methode
        x = self.list[-1]
        return x


    def isEmpty(self): # klasse-methode
        if not self.list:
            return True
        else:
            return False


    def __init__(self, list = []): # constructor
        self.list = list



    def __repr__(self): # voor print-opdracht
        return str(self.list[:])



s1 = MyStack([1,2,3,4,5,6,7,8,9])

print(s1)
s1.push(10)
print(s1)
s1.push(11)
print(s1)
print(s1.pop())
print(s1)
s1.push(12)
print(s1)
print(s1.pop())
print(s1)
print(s1.peek())
print(s1)
print("------------")

print(s1.list)
for i in range(0, len(s1.list)):
    print(i)
    s1.pop()

print(s1)
print(s1.isEmpty())
s1.push(6)
print(s1)
print(s1.isEmpty())