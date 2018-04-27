# Question 3
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest possible total weight of edges. 
# Your function should take in and return an adjacency list structured like this:
    # {'A': [('B', 2)],
    #  'B': [('A', 2), ('C', 5)], 
    #  'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)

# This is my version of using the Kruskal MST alogrithm found at 
# https://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/


#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.V = vertices #No. of vertices
        self.graph = [] # default dictionary 
                                # to store graph
         
  
    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
 
    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Attach smaller rank tree under root of 
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        # If ranks are same, then make one as root 
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

# The main function to construct MST using Kruskal's 
# algorithm
def KruskalMST(graph, V):

    result = {} # This will store the resultant MST

    i = 0 # An index variable, used for sorted edges
    e = 0 # An index variable, used for result[]

    # Step 1:  Sort all the edges in non-decreasing 
    # order of their weight.  If we are not allowed to change the 
    # given graph, we can create a copy of graph
    graph.graph= sorted(graph.graph)
    # graph.graph =  sorted(graph.graph,key=lambda item: item[2])

    parent = [] ; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)
    
    # Number of edges to be taken is equal to V-1
    while e < V - 1:
        # Step 2: Pick the smallest edge and increment 
        # the index for next iteration
        u,v,w =  graph.graph[i]
        i = i + 1
        x = graph.find(parent, u)
        y = graph.find(parent ,v)

        # If including this edge does't cause cycle, 
        # include it in result and increment the index
        # of result for next edge
        if x != y:
            e = e + 1    
            z = (v, w)
            if u in result:
                result[u].append(z)
            else:
                result[u] = [z]
        # Else discard the edge    
        graph.union(parent, rank, x, y)            
    
    return result


def question3(G):
    vert_len = len(G)
    graph = Graph(vert_len)

    for i in G:
        if type(i) is str:
            for j in G[i]:
                if type(j[0]) is str:
                    graph.addEdge(str_to_int(i), str_to_int(j[0]), j[1])
                else:
                    graph.addEdge(str_to_int(i), j[0], j[1])        
        else:
            for j in G[i]:
                graph.addEdge(i, j[0], j[1])

    return KruskalMST(graph, graph.V)


def str_to_int(s):
    return ord(s.lower()) - 97


def test3():
    g =  {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    expected = {0: [(1, 2)], 1: [(2, 5)]}
    
    print "Testing 3"
    print "g = " + str(g)
    print "Case (example case):", "Pass" if question3(g) == expected else "Fail" 

    G = { 0: [(1, 2), (4, 6)], 
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)] }

    expected = {0: [(1, 2), (4, 6)], 1: [(2, 3), (3, 8)]}

    print "G = " + str(G)
    print "Case (G):", "Pass" if question3(G) == expected else "Fail" 

test3()
