from collections import deque, defaultdict, deque

class GNode:
    def __init__(self, id=None):
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
            self.graph[int(edge[0])].add_edge(int(edge[1]))
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
                if n not in trace and n not in q:
                    q.append(n)
        return trace

    def dfs(self, x):
        s = []  # pseudo stack

        trace = [x]
        toadd = sorted(self.graph[x].get_edge(), reverse=True)
        s.extend(toadd)
        while len(s) != 0:
            next = s.pop()
            if next in trace:
                continue
            trace.append(next)
            toadd = sorted(self.graph[next].get_edge(), reverse=True)
            for n in toadd:
                # if n not in trace:
                s.append(n)
        return trace

if __name__ == "__main__":
    G = Graph("./small.txt")
    for i in range(3):
        print(f"bfs starting from {i}\n   {G.bfs(i)}\n\n")

    for i in range(3):
        print(f"dfs starting from {i}\n   {G.dfs(i)}\n\n")

