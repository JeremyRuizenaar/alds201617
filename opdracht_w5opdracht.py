__author__ = 'jer'
class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data


INFINITY = float("inf")


def vertices(G):
    a = list(G.keys())
    a.sort()
    return a


def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u]:
            a.append((u, v))
    return a


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY
    no_cycle = True
    q = myqueue()
    q.enqueue(s)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:
                v.distance = u.distance + 1
                v.predecessor = u
                q.enqueue(v)
            elif u.predecessor != v:
                no_cycle = False
    return no_cycle


def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()


def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()


def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


def is_connected(G):
    V = vertices(G)
    BFS(G, V[0])
    for s in G:
        if s.distance == INFINITY:
            return False
    return True


def no_cycles(G):
    V = vertices(G)
    return BFS(G, V[0])


def get_bridges(G):
    bridges = []
    for e in edges(G):
        G[e[0]].remove(e[1])
        G[e[1]].remove(e[0])
        if not is_connected(G):
            bridges.append(e)
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    return bridges


def is_strongly_connected(G):
    if not is_connected(G):
        return False
    tempGraph = {}
    for edge in edges(G):
        if edge[0] in tempGraph.keys():
            tempGraph[edge[0]].append(edge[1])
        else:
            tempGraph[edge[0]] = [edge[1]]
    return is_connected(tempGraph)


def is_euler_graph(G):
    for l in G.values():
        if len(l) % 2 != 0:
            return False
    return True


def get_euler_circuit(G, s):
    if not is_euler_graph(G):
        return
    steps = [s]
    while (G[s]):
        for t in G[s]:
            k = t
            if (s, t) not in get_bridges(G):
                break
        steps.append(k)
        G[s].remove(k)
        G[k].remove(s)
        s = k

    return steps



v = [Vertex(i) for i in range(8)]

G = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1],v[2], v[5]],
    v[5]: [v[0], v[1], v[2],v[4]],
    v[6]: [v[1], v[2]],
    v[7]: [v[3]]
}
print("Is graph connected --> ", is_connected(G))
clear(G)


v = [Vertex(i) for i in range(7)]
G = {
    v[0]: [v[5], v[4]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[4]: [v[0], v[1], v[2], v[5]],
    v[5]: [v[1], v[2], v[4], v[0]],
    v[6]: [v[1], v[2]],
}

print("Is graph connected --> ", is_connected(G))
print("Graph bevat geen cycles --> ", no_cycles(G))
clear(G)


v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[5], v[4]],
     v[1]: [v[4], v[6]],
     v[2]: [v[5]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1]],
     v[5]: [v[0], v[2]],
     v[6]: [v[1]],
     v[7]: [v[3]]}
clear(G)
print("Graph bevat geen cycles --> ", no_cycles(G))
clear(G)

v = [Vertex(i) for i in range(8)]
G = {
    v[0]: [v[1], v[3]],
    v[1]: [v[0], v[2]],
    v[2]: [v[1], v[4], v[3]],
    v[3]: [v[2], v[0]],
    v[4]: [v[2], v[5], v[6]],
    v[5]: [v[4], v[6]],
    v[6]: [v[5], v[4], v[7]],
    v[7]: [v[6]]
}
print("Bridges --> ", get_bridges(G))
clear(G)


v = [Vertex(i) for i in range(3)]
G = {v[0]: [v[1]],
     v[1]: [v[2]],
     v[2]: [v[0]]}
print("Is graph strong --> ", is_strongly_connected(G))
clear(G)



v = [Vertex(i) for i in range(3)]
G = {v[0]: [v[1]],
     v[1]: [],
     v[2]: [v[0], v[1]]}
print("Is graph strong --> ", is_strongly_connected(G))
clear(G)



v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]}
print("Is graph Euler --> ", is_euler_graph(G))
print("Euler circuit startnode [0]--> ", get_euler_circuit(G, v[0]))
clear(G)


v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]}
print("Euler circuit startnode [5] --> ", get_euler_circuit(G, v[5]))
clear(G)


v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]}
print("Euler circuit startnode [7] --> ", get_euler_circuit(G, v[7]))
clear(G)


v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]}
print("Euler circuit startnode [4] --> ", get_euler_circuit(G, v[4]))
clear(G)






