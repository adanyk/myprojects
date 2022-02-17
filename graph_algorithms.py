import numpy as np

#lists/arrays of connections, weights and vertices of graphs
c1 = np.array([[0, 0, 0, 0, 1], [1, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 0], [0, 0, 1, 1, 0]])
w1 = np.array([[0, 0, 0, 0, 7], [10, 0, 0, 3, 0], [0, 1, 0, 9, 6], [5, 2, 0, 0, 0], [0, 0, 4, 2, 0]])
v1 = ['s', 'u', 'v', 'x', 'y']

c2 = np.array([[0, 1, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1], [0, 0, 1, 0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 1, 0, 0, 0, 1, 1, 0]])
w2 = np.array([[0, 4, 0, 0, 0, 0, 0, 8, 0], [4, 0, 8, 0, 0, 0, 0, 11, 0], [0, 8, 0, 7, 0, 4, 0, 0, 2], [0, 0, 7, 0, 9, 14, 0, 0, 0], [0, 0, 0, 9, 0, 10, 0, 0, 0], [0, 0, 4, 14, 10, 0, 2, 0, 0], [0, 0, 0, 0, 0, 2, 0, 1, 6], [8, 11, 0, 0, 0, 0, 1, 0, 7], [0, 0, 2, 0, 0, 0, 6, 7, 0]])
v2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

c3 = np.array([[0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 1, 1, 0]])
w3 = np.array([[0, 0, 0, 0, 0, 0], [16, 0, 5, 0, 9, 0], [13, 12, 0, 0, 0, 0], [0, 12, 0, 0, 0, 0], [0, 0, 15, 6, 0, 0], [0, 0, 0, 12, 20, 0]])
v3 = ['A', 'B', 'C', 'D', 'E', 'F']


def multiple_matmul(vector, matrix, number):
    if number == 1:
        return np.matmul(matrix, vector)
    else:
        return np.matmul(matrix, multiple_matmul(vector, matrix, number - 1))


class Graph:

    def __init__(self, v, c, w):
        
        #check whether input parameters can create a valid graph
        if c.shape[0] != c.shape[1]:
            raise Exception("Adjacency matrix is not square.")
        if c.shape != w.shape:
            raise Exception("Weights matrix has not the same shape as adjacency matrix.")
        if len(v) != c.shape[0]:
            raise Exception("Number of vertices is not the same as the size of matrix.")

        #create graph
        self.vertices = v[:]
        self.connections = np.array(c)
        self.weights = np.array(w)

    def display(self):
        print(self.vertices, end="\n\n")
        print(self.connections, end="\n\n")
        print(self.weights)
    
    def is_graph_directed(self):
        T = self.weights == np.transpose(self.weights)
        return T.all()

    def dijkstra(self, source):

        #create list of vertices with initial distance of infinity
        Q = []
        for i, v in enumerate(self.vertices):
            Q.append([i, np.inf, [source]])    #vertex = [index, distance, [path]]
        Q[self.vertices.index(source)][1] = 0       #assign distance of source to 0
        
        #create eventual list of vertices
        S = []

        #fillup S
        while Q:
            #find vetrex in Q with the lowest distance, add it to S and remove it from Q
            u = Q[0]
            for i in Q:
                if i[1] < u[1]:
                    u = i
            S.append(u)
            Q.remove(u)

            #find vertices you can reach from u
            for v in Q:
                if self.connections[v[0]][u[0]]:   #if u goes to v
                    alt_value = u[1] + self.weights[v[0]][u[0]]
                    if alt_value < v[1]:
                        #if distance to v via u is lower than the previous one: update distance and path to v
                        v[1] = alt_value
                        v[2] = u[2][:]
                        v[2].append(self.vertices[v[0]])
        
        for i in S:
            i[0] = self.vertices[i[0]]   #vertex = [name, distance, [path]]

        #create graph of the shortest paths from source to remaining destinations
        sp = Graph(self.vertices, np.zeros((len(self.vertices), len(self.vertices)), dtype=int), np.zeros((len(self.vertices), len(self.vertices)), dtype=int))
        for v in S:
            if v[0] != source:
                sp.connections[self.vertices.index(v[0])][self.vertices.index(v[2][-2])] = self.connections[self.vertices.index(v[0])][self.vertices.index(v[2][-2])]
                sp.weights[self.vertices.index(v[0])][self.vertices.index(v[2][-2])] = self.weights[self.vertices.index(v[0])][self.vertices.index(v[2][-2])]

        return S, sp

    def kruskal(self):    
        A = []      #eventual list of edges [(weight, vertex1, vertex2)]

        #create list of edges, sorted in non-descending order
        edges = []
        for i in range(1, len(self.vertices)):
            for j in range(i):
                if self.connections[i][j]:
                    edges.append((self.weights[i][j], self.vertices[j], self.vertices[i]))
        edges.sort()

        #create list of sets of joined vertices (i.e. forest of trees) [{joined vertices}]
        #assign initial content as set that includes the first element of edges
        T = [{edges[0][1]}]
            
        #fillup A
        for e in edges:     #(weight, vertex1, vertex2)
                    
            #determine whether vertex1 and vertex2 belong to common tree
            common_tree = False
            for t in T:
                if {e[1], e[2]}.issubset(t):
                    common_tree = True
                    break
            
            #if they don't
            if not common_tree:

                #add vertex1 and vertex2 to T
                for t in T:
                    #find tree t in forest T which contains one of vertices and add the second to it
                    if e[1] in t or e[2] in t:
                        t.update({e[1], e[2]})
                        for r in T:
                            #find tree r in forest T which contains the vertex t did not and merge it with t
                            if (e[2] in r and e[1] not in r) or (e[1] in r and e[2] not in r):
                                t.update(r)
                                T.remove(r)
                                break
                        break
                    else:
                        #in case none of vertices belongs to T add both as a new tree
                        T.append({e[1], e[2]})

                #add egde to A
                A.append(e)
            
        #create graph representing minimum spanning forest/tree
        msf = Graph(self.vertices, np.zeros((len(self.vertices), len(self.vertices)), dtype=int), np.zeros((len(self.vertices), len(self.vertices)), dtype=int))

        for ind, val in enumerate(A):
            msf.connections[msf.vertices.index(val[1])][msf.vertices.index(val[2])] = msf.connections[msf.vertices.index(val[2])][msf.vertices.index(val[1])] = 1
            msf.weights[msf.vertices.index(val[1])][msf.vertices.index(val[2])] = msf.weights[msf.vertices.index(val[2])][msf.vertices.index(val[1])] = val[0]
                
        return A, msf

    def ford_fulkerson(self, source, target):

            #make copies of Graph to work on
            G_flow = (self.connections, self.weights)
            G_residual = np.zeros((len(self.vertices), len(self.vertices)), dtype=int)
            
            #initiate source vector (e.g. [[1], [0], [0], [0], [0], [0]])
            s_vector = np.zeros((len(self.vertices), 1), dtype=int)
            s_vector[self.vertices.index(source)][0] = 1

            #find path from source to target in G_flow

            #determine whether the path exists and how long it is
            path_exists = True

            while path_exists:
                for i in range(1, len(self.vertices)):
                    t_vector = multiple_matmul(s_vector, G_flow[0], i)
                    if t_vector[self.vertices.index(target)][0]:
                        path_exists = True
                        path = []
                        #create tree representing possible paths to target in i steps
                        Tree = [[target]]
                        for j in range(i):
                            temp_Tree = []
                            for t in Tree:
                                for ind, v in enumerate(self.vertices):
                                    if self.connections[self.vertices.index(t[-1])][ind]:  #if v goes to the last vertex in branch t
                                        #create copy of t, add v to it, add it to Tree
                                        temp = t[:]
                                        temp.append(v)
                                        temp_Tree.append(temp)
                                #remove t form Tree (instead of t we have now extentions of ts going to vs)
                            Tree = temp_Tree[:]
                        #create best path (with greatest capacity) based on contents of Tree
                        max_capacity = 0
                        for t in Tree:
                            if t[-1] == source:
                                #create list of capacities in edges between adjacent vertices in t
                                edges_capacities = []
                                for ind, v in enumerate(t):
                                    if ind:
                                        #fill edges_capacities with values found in G_flow
                                        edges_capacities.append(G_flow[1][self.vertices.index(t[ind-1])][self.vertices.index(v)])
                                #determine whether path through vertices in t is the best one
                                min_capacity = min(edges_capacities)
                                if min_capacity > max_capacity:
                                    #if it is: update path and its capacity
                                    max_capacity = min_capacity
                                    path = t

                        #update G_flow and G_residual
                        for i, v in enumerate(path):
                            if i:
                                G_flow[1][self.vertices.index(path[i - 1])][self.vertices.index(v)] -= max_capacity
                                G_flow[1][self.vertices.index(v)][self.vertices.index(path[i - 1])] += max_capacity

                                if G_flow[1][self.vertices.index(path[i - 1])][self.vertices.index(v)]:
                                    G_flow[0][self.vertices.index(path[i - 1])][self.vertices.index(v)] = 1
                                else:
                                    G_flow[0][self.vertices.index(path[i - 1])][self.vertices.index(v)] = 0

                                G_residual[self.vertices.index(path[i - 1])][self.vertices.index(v)] += max_capacity
                        break

                    else:
                        path_exists = False

            #create dict of edges based on G_residual
            edges = {}
            flow = 0
            for i, v1 in enumerate(self.vertices):
                for j, v2 in enumerate(self.vertices):
                    if G_residual[i][j]:
                        edges[(v2, v1)] = G_residual[i][j]
                    if v1 == target:
                        #calculate sum of edges heading directly to target
                        flow += G_residual[i][j]

            #create graph representing maximum flow
            #mf = Graph(self.vertices, np.zeros((len(self.vertices), len(self.vertices)), dtype=tuple), np.zeros((len(self.vertices), len(self.vertices)), dtype=int))
            mf = Graph(self.vertices, self.connections, G_residual)
            
            return edges, flow, mf

if __name__ == "__main__":

    G1 = Graph(v1, c1, w1)
    G2 = Graph(v2, c2, w2)
    G3 = Graph(v3, c3, w3)


    #USE ONE OF THREE ALGORITHMS, comment out remaining ones
    #dijkstra on G1
    print("\nList:")
    ver, gra = G1.dijkstra('s')
    for i in ver:
       print(i)
    print("\n\nGraph of the shortest paths:")
    
    # #kruskal on G2
    # edg, gra = G2.kruskal()
    # for i in edg:
    #     print(i)
    
    # #ford_fulkerson on G3
    # ed, fl, gra = G3.ford_fulkerson('A', 'F')
    # print("\nEdges:" + ''.join(f"\n{key}: {value}" for key, value in ed.items()))
    # print(f"\nMax flow: {fl}")
    # print("\n\nMax flow graph:")

    
    gra.display()


