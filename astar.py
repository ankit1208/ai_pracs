class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
                'S' : 10,
                '1' : 13,
                '2' : 9,
                '3' : 8,
                '4' : 12,
                '5' : 7,
                '6' : 1,
                '7' : 10,
                '8' : 19,
                '9' : 11,
                '10' :9,
                '11' :8,
                '12' : 7,
                '13' : 1,
                '14' : 10,
                '15' : 18,
                '16' : 11,
                '17' : 7,
                '18' :10,
                '19' : 9,
                '20' : 18,
                '21' : 18,
                '22' : 19,
                'D':0
        }

        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])
        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            
            n = None
#             print(open_list)
            f=[]
            for l in range(len(open_list)):
#                 print("Node:",list(open_list)[l])
#                 print(g[str(list(open_list)[l])])
#                 print(self.h(str(list(open_list)[l])))
                val = g[str(list(open_list)[l])] + self.h(str(list(open_list)[l])) 
                f.append(val)
            ol = list(open_list)   
            pq = [ol for _,ol in sorted(zip(f,ol))]
            f= sorted(f)
            print("Node: ",pq)
            print("F(X): ",f)
            
            

#             intersect = open_list.difference(bleh)
#             print(intersect)
            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
#                     f = g[n] + self.h(n)
                    n = v
            print(f"Explore {n} \n")
                    
                    
                    
                    

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
               
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            bleh = open_list.copy()
            open_list.remove(n)
            closed_list.add(n)
            
        print('Path does not exist!')
        return None
        
adjacency_list = {
  'S' : [('1',9),('2',7),('3',10),('4',17)],
  '1' : [('5',18),('6',2),('7',10),('8',23)],
  '2' : [('8',5),('9',16)],
  '3' : [('9',33),('10',19),('11',17),('4',45)],
  '4' : [('12',12),('13',1),('14',18)],
  '5' : [('15',40),('16',7)],
  '6' : [('7',48),('16',12)],
  '7' : [],
  '8' : [('17',1),('18',42)],
  '9' : [('18',9)],
  '10' : [('19',13)],
  '11' : [('20',9)],
  '12' : [('21',10)],
  '13' : [('14',37)],
  '14' : [('22',16)],
  '15' : [('D',14)],
  '16' : [('17',19)],
  '17' : [('18',3),('19',47)],
  '18' : [],
  '19' : [('D',18)],
  '20' : [('D',35)],
  '21' : [('D',16)],
  '22' : [('D',6)],
  'D':[]
}

graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('S', 'D')