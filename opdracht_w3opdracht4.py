__author__ = 'jer'


class TrieNode:
    def __init__(self, a=None):
        self.dictionary = {}
        self.n = 0
        self.element = a

    def __repr__(self):
        return str(self.element)


def calcFrequencyTrie(path):
    root = TrieNode("root")
    node = root
    a = open(path,'r')

    for line in a:
        for word in line.split():
            for char in word:
                keys = node.dictionary.keys()

                if not char in keys:
                    node.dictionary[char] = TrieNode(char)
                    node = node.dictionary[char]


                else:
                    node = node.dictionary[char]

            node.n += 1
            node = root
    a.close()
    return root


def printTreeValues(node, s, f):
    if node.n > 0:
        #string = s + " ----> " + str(node.n) + "\n"
        string = s + " " + str(node.n) + "\n"
        # print(string[0:-1])
        f.write(string)

    if len(node.dictionary) == 0:
        return

    else:

        for key in node.dictionary.keys():

            if node.element == "root":
                s = s + key
                printTreeValues(node.dictionary[key], s,f)
                s = " "

            else:

                remind = s
                s = s + key
                printTreeValues(node.dictionary[key], s,f)

                s = ""
                s = s + remind

        return

def writeTreeToFile(node):
    f = open("outputTrie.txt",'w')
    s = ""
    printTreeValues(node, s, f)
    f.close()
    return


def calcFrequencyDict(path):
    f=open(path,'r')
    dict = {}
    for line in f:
        for word in line.split():
            if word in dict.keys():
                dict[word] = dict[word] + 1

            else:
                dict[word] = 1

    f.close()

    f= open("freuquencyDict.txt", 'w')
    for key in dict.keys():
        string = key + " " + str(dict[key]) + '\n'
        f.write(string)
        #print(key + " " + str(dict[key]))
    f.close()
    return dict



def compareFiles():
    f1 = open("outputTrie.txt",'r')
    f2 = open("freuquencyDict.txt",'r')

    dict1 = {}
    for line in f1:
        element = line.split()
        dict1[element[0]] = element[1]
    print(dict1)
    f1.close()



    dict2 = {}
    for line in f2:
        element = line.split()
        dict2[element[0]] = element[1]
    print(dict2)
    f2.close()

    print("len of trie dict = " + str(len(dict1)))
    print("len of dict dict = " + str(len(dict1)))
    gedeeldItems = set(dict1.items()) & set(dict2.items())
    print ("overeenkomstige waardes = " +str(len(gedeeldItems)))


path = "test.txt"

print("-"*12 + '\n')
print("calc tree")
print("-"*12 + '\n')

writeTreeToFile(calcFrequencyTrie(path))

print("-"*12 + '\n')
print("calc dic")
print("-"*12 + '\n')

calcFrequencyDict(path)


compareFiles()
