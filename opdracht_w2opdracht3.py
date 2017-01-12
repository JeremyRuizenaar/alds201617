__author__ = 'jer'
class MyStack(list):

    def push(self, a):
        self.list.append(a)

    def pop(self):
        x = self.list[-1]
        del self.list[-1]
        return x

    def clear(self):
        for i in range(0, len(self.list)):
            self.pop()

    def peek(self):
        x = self.list[-1]
        return x


    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False


    def __init__(self, list = []): # constructor
        self.list = list



    def __repr__(self): # voor print-opdracht
        return str(self.list[:])


def parseString(expr):
    s = MyStack()
    s.clear()
    for i in expr:
        #print(s)
        if i ==  '<':
            s.push(i)

        elif i == '{':
            s.push(i)

        elif i == '(':
            s.push(i)

        elif i  == '[':
            s.push(i)

        elif i ==  '>' and s.peek() == '<':
            s.pop()

        elif i == '}' and  s.peek() == '{':
            s.pop()

        elif i == ')' and s.peek() == '(':
            s.pop()

        elif i  == ']' and s.peek() == '[':
            s.pop()

    return s.isEmpty()


list = ["((<>)())", "[(<>)]()(()())","((<>))", "([)]","(((<)>))","[({<<{}>>})]","[({<}>)]"]

for expr in list:

    print("expr = "+ expr)
    print(str(parseString(expr)) )
    print("-----")



