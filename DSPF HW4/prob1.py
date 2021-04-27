from collections import deque, defaultdict, deque

class GNode:
    def __init__(self, id):
        self.id = id
        self.edge = []
    def get_id(self):
        return self.id
    def get_edge(self):
        return self.edge
    def add_edge(self, dest):
        self.edge.append(dest)
        self.edge = sorted(self.edge)

class Graph:
    def __init__(self, filename):
        self.graph = defaultdict(GNode)
        f=open(filename)
        while True:
            line = f.readline()
            if not line: break
            edge = line.split(',')
            self.graph[edge[0]].add_edge(edge[1])
        f.close()

    def bfs(self, x):
        q = deque()
        # passed = defaultdict(int)

        trace = [x]
        # passed[x] = 1
        q.extend(self.graph[x].get_edge())
        while len(q) != 0:
            next = q.popleft()
            trace.append(next)
            # passed[next]=1

            toadd = self.graph[next].get_edge()
            for n in toadd:
                if n not in trace:
                    q.append(n)
        return trace

    def dfs(self, x):

        return