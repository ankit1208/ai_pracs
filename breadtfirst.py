graph = {
  'S' : ['1','2','3','4'],
  '1' : ['5','6','7','8'],
  '2' : ['8','9'],
  '3' : ['9','10','11','4'],
  '4' : ['12','13','14'],
  '5' : ['15','16'],
  '6' : ['7','16'],
  '7' : [],
  '8' : ['17','18'],
  '9' : ['18'],
  '10' : ['19'],
  '11' : ['20'],
  '12' : ['21'],
  '13' : ['14'],
  '14' : ['22'],
  '15' : ['D'],
  '16' : ['17'],
  '17' : ['18','19'],
  '18' : [],
  '19' : ['D'],
  '20' : ['D'],
  '21' : ['D'],
  '22' : ['D'],
  'D':[]
}
visited = [] # List for visited nodes.
queue = []     #Initialize a queue
order = []
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  
  while queue:        
    # Creating loop to visit each node
    m = queue.pop(0) 
    order.append(m)
    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)   
    print(order)      
    print("visited",visited)
print("Following is the Breadth-First Search")

bfs(visited, graph, 'S')    # function calling
