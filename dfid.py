graph = {
  'S' : ['1','2','3','4'],
  '1' : ['5','6','7'],
  '2' : ['8','9'],
  '3' : ['10','11'],
  '4' : ['12','13','14'],
  '5' : ['15'],
  '6' : ['16'],
  '7' : [],
  '8' : ['17'],
  '9' : ['18'],
  '10' : ['19'],
  '11' : ['20'],
  '12' : ['21'],
  '13' : [],
  '14' : ['22'],
  '15' : [],
  '16' : [],
  '17' : [],
  '18' : [],
  '19' : [],
  '20' : ['D'],
  '21' : [],
  '22' : [],
  'D':[]
}


max_depth = 10
start_node = 'S'
destn_node = 'D'

path = list()


def DFS(currentNode,destination,graph,maxDepth,curList):
    print("\n----- Next Iteration -----")
    print("Checking for destination",currentNode)
#     print("Open list: ", open_list)
#     print("Closed_list: ", closed_list)
#     print()
    curList.append(currentNode)
    print(f"Closed List: {curList}")
    print("Open List: [", end = '')
    for i in list(graph.keys()):
        if i not in curList:
            print("'" + i + "'", end = ',')
    print("]")
    if currentNode==destination:
        return True
    if maxDepth<=0:
        path.append(curList)
        return False
    for node in graph[currentNode]:
        if DFS(node,destination,graph,maxDepth-1,curList):
            return True
        else:
            curList.pop()
    return False

def iterativeDDFS(currentNode,destination,graph,maxDepth):
    open_list = list(graph.keys())
    closed_list = []
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode,destination,graph,i,curList):
            return True
    return False

if not iterativeDDFS(start_node, destn_node, graph, max_depth):
    print("\nPath is not available!")
else:
    print("\nA path exists!")