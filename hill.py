succlist  = {
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


start = 'S'
Closed = list()

def MOVEGEN(N):
    new_list = list()
    if N in succlist.keys():
        new_list = succlist[N]
    return new_list

def SORT(L):
    L.sort(key = lambda x: x[1])
    return L

def heu(Node):
    return Node[1]

def APPEND(L1,L2):
    new_list = list(L1) + list(L2)
    return new_list

def Hill_Climbing(start):
    global closed
    N = start
    child = MOVEGEN(N)
    SORT(child)
    N = [start,100]
    print("\nStart: ",N)
    print("Sorted Child  List: ",child)
    newnode = child[0]
    closed = [N]

    while heu(newnode)<=heu(N):
        print('\n------------------')
        N=newnode
        print('N = ',N)
        closed = APPEND(closed,[N])
        child = MOVEGEN(N[0])
        SORT(child)
        print("Sorted Child List = ", child)
        print("Closed List: ", closed)
        newnode = child[0]
    Closed = closed
    

Hill_Climbing(start) #calling the search algorithm 