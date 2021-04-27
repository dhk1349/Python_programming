from prob2 import Graph
import time


t1 = time.time()
graph = Graph('large.txt')
x = graph.get_close(1, 5)
y = graph.get_close(123, 5)
z = graph.get_close(543, 5)
w = graph.get_close(1234, 5)
t = graph.get_close(9876, 5)
print(x,y,z,w,t)
t2 = time.time()

if t2 - t1 < 10:
    print("Pass (%.3f sec)"%(t2-t1))
else:
    print("Fail (%.3f sec)"%(t2-t1))
