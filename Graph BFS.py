from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def add_edge(self,from_node,to_node):
        self.graph[from_node].append(to_node)
    def BFS(self,root_node):
        q=[]
        visited=[False]*(len(self.graph))
        q.append(root_node)
        visited[root_node]=True

        while q:
            root_node=q.pop(0)
            print(root_node,end=" ")
            for i in self.graph[root_node]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True
g=Graph()
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(1,3)
g.add_edge(3,4)
r=1
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
g.BFS(2) 

