
def graphik(graph, c, l):
    
    """ Affiche dans la console une représentation du labyrinthe en fonction 
    de son graphe entré en paramètre """
    
    ind = 1
    for z in range(l) :
        L1 = []
        L2 = []
        for w in range(c) :
            if w == c-1:
                if z != l-1:
                    L2.append(graph[ind][-1][1])
            else:
                if z == l-1:
                    L1.append(graph[ind][-1][1])
                    ind += 1
                else:
                    L1.append(graph[ind][-1][1])
                    L2.append(graph[ind][-2][1])
                    ind += 1
        ind+=1
        Ltype1(L1)
        Ltype1bis(L1)
        Ltype2(L2)
        

def Ltype1(lst):
    if lst != None :
        for l in range(lst.__len__()):
            if l == lst.__len__()-1:
                print("|''''|",lst[l],"|''''|") 
            else:
                print("|''''|",lst[l],end=" ")

def Ltype1bis(lst):
    if lst != None :
        for l in range(lst.__len__()):
            if l == lst.__len__()-1:
                print("|____|",lst[l],"|____|") 
            else:
                print("|____|",lst[l],end=" ")

def Ltype2(lst):
    if lst != None :
        for l in range(lst.__len__()):
            if l == lst.__len__()-1:
                print("",lst[l],"",lst[l]," ") 
            else:
                print("",lst[l],"",lst[l],end="    ")


Graph_test = {1: [(5, 5), (2, 2)], 2: [(1, 2), (6, 3), (3, 3)], 3: [(2, 3), (7, 4), (4, 4)], 4: [(3, 4), (8, 3)], 5: [(1, 5), (9, 5), (6, 4)], 6: [(5, 4), (2, 3), (10, 3), (7, 2)], 7: [(6, 2), (3, 4), (11, 4), (8, 5)], 8: [(7, 5), (4, 3), (12, 3)], 9: [(5, 5), (10, 4)], 10: [(9, 4), (6, 3), (11, 5)], 11: [(10, 5), (7, 4), (12, 5)], 12: [(11, 5), (8, 3)]}

graphik(Graph_test, 4, 3)
