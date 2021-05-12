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
        # 그냥 시작할 때 나머지 모든 노드를 넣어놓고 시작하도록 구상하기
        # tree가 여러개여도 잘 작동함.
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

    def get_close(self, x, k):
        """
        q를 이중 loop를 사용한다.
        """
        # q = deque()
        q=[]
        passed = defaultdict(int)

        trace = []
        passed[x] = 1 #que안에 있는 것까지 모두 추적
        q.append(self.graph[x].get_edge())
        for i in range(k):  # Within distance k
            nextq=[]
            while len(q[i]) != 0:
                next = q[i][-1]  # .popleft()
                q[i]=q[i][:-1]
                trace.append(next)
                passed[next]=1
                toadd = self.graph[next].get_edge()
                toaddq=[]
                for n in toadd:
                    if passed[n] != 1:
                    # if n not in trace and n not in q:
                        nextq.append(n)
            q.append(nextq)
        return sorted(trace)

if __name__ == "__main__":
    G = Graph("./small.txt")
    for i in range(2):
        for j in range(1,3):
            print(f"Get close {i}, {j}:\n   {G.get_close(i, j)}\n\n")

