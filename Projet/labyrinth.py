
import random

""" NOTE : Dans ce code je parle de labyrithe en designant la grille énoncé dans l'énoncé du projet """





"""                         SOMMAIRE


    I . CLASSES.............................................. 50
    
        a . ANSI............................................. 56
        b . Labyrinth........................................ 70
    
    II . DIJKSTRA............................................ 197
        
        a . minimum.......................................... 205 
        b . dijkstra_pred.................................... 213
    
    III . PARTIE GRAPHIQUE................................... 248
    
        a . graphik.......................................... 254
        b . Ltype1........................................... 281
        c . Ltype1bis........................................ 289
        d . Ltype2........................................... 297
        e . Modif_Graph...................................... 307
        f . dessin_graph..................................... 374
    
    IV . FONCTIONS IDOINES................................... 413
    
        a . chemin........................................... 421
        b . chemin_court..................................... 429
        c . Test............................................. 439
        d . PARTIE_2......................................... 472
        e . Astar_test....................................... 517
    
    V . MAIN................................................. 602
    

 """




###############################################
#                                             #
#   D E B U T  D E S  C L A S S E S           #
#                                             #
###############################################



class ANSI():
    
    """ Cette classe nous permet d'ajouter une couleur à notre texte dans la console
    ici on utilisera le changement de couleur pour indiquer le chemin le plus court dans notre labyrinthe """
  
    def color_text(code):
        return "\33[{code}m".format(code=code)
    
    def stopper():
        return "\033[0;0m"
    



class Labyrinth:
    
    """ Cette classe nous permet de créer des labyrinthe en fonction de leur taille, c'est-à-dire
    le nombre de pièces qui le composent. Biensûr le labyrinthe doit avoir la méme configuration que celle
    donnée dans l'énoncé, autrement dit elle doit former une grille"""
    
    """  Exemple :  1 -- 2 -- 3 -- 4
                    |    |    |    |
                    5 -- 6 -- 7 -- 8    Nous avons ici la représentation sous forme de graphe du labyrinthe
                    |    |    |    |    donné dans l'énoncé avec les cellules représentées par les chiffres
                    9 --10 --11 --12    
                                        Dans cet exemple la taille du labyrinthe est de 12 avec 4 colonnes et
                                        3 lignes """
    
    def __init__(self, col, lig):
        T = col*lig
        self.taille = T
        self.colonne = col
        self.ligne = lig
        self.Lab = {k:[] for k in range(1,T+1)} # représente le graphe du labyrinthe
        self.Moy = 0
        
        
        def Laby(self):
            
            """ La fonction Laby initialise le graphe du labyrinthe en fonction des propriétés du labyrinthe
            Elle s'occupe aussi de générer une épaisseur aléatoires pour chaque murs séparants les cellules 
            entre elles. L'épaisseur d'un mur peut varié entre 1 et 5 """
            
            c = self.colonne
            l = self.ligne
            Mat = [[c*i+j+1 for j in range(c)] for i in range(l)]
            
            for i in range(c):
                for j in range(l):
                    
                    """ On parcours le graphe """
                    
                    """ Illustration des cellules voisines traitées dans la fonction :
                             2
                             |
                        5 -- 6 -- 7     Ici la cellule initiale (soit située à la ligne i et la colonne j) est
                             |          6 et les autres cellules correspondent à ses cellules voisines
                             10
                        
                        """
                    
                    for x in range(i-1,i+2):
                        if x == i :
                            
                            """ Dans cette boucle on va traiter les cellules situées en bas et en haut de 
                            la cellule initiale. Dans l'illustration elles correspondent aux cellules 2 et 10 """
                            
                            for y in range(j-1,j+2):
                                
                                """ Cette boucle nous permet de parcourir les cellules voisines de la cellules
                                à la ligne j et à la colonne i. Attention on prend en compte uniquement les cellules
                                situées à droite, à gauche, en bas et en haut de la cellule initiale """
                                
                                if not(x==i and y ==j):
                                    
                                    """ Cette boucle nous permet de ne pas prendre en compte la cellule initiale dans
                                    notre traitement """
                                    
                                    if x>=0 and y>=0 and x<c and y<l:
                                        if x==i-1 or y==j-1:
                                            val1 = Mat[y][x]
                                            for k in self.Lab[val1]:
                                                if k[0]== Mat[j][i]:
                                                    self.Lab[Mat[j][i]].append((Mat[y][x],k[1]))
                                        else:
                                            alea = random.randint(1,5)
                                            self.Moy += alea
                                            self.Lab[Mat[j][i]].append((Mat[y][x],alea))
                        else:
                            
                            """ Dans cette boucle on va traiter les cellules situées à droite et à gauche de 
                            la cellule initiale. Dans l'illustration elles correspondent aux cellules 5 et 7 """
                            
                            if x>=0 and x<c:
                                if x==i-1:
                                    val2 = Mat[j][x]
                                    for k in self.Lab[val2]:
                                        if k[0]== Mat[j][i]:
                                            self.Lab[Mat[j][i]].append((Mat[j][x],k[1]))
                                else:
                                    alea = random.randint(1,5)
                                    self.Moy += alea
                                    self.Lab[Mat[j][i]].append((Mat[j][x],alea))
        Laby(self)
        self.Moy = self.Moy/17
        
    ### A C C E S S E U R S ###
        
    def getLab(self):
        return self.Lab
    
    def getcolonne(self):
        return self.colonne
    
    def getligne(self):
        return self.ligne
    
    def getTaille(self):
        return self.taille
    
    def getMoy(self):
        return self.Moy
    

###############################################
#                                             #
#   F I N  D E S  C L A S S E S               #
#                                             #
###############################################










###############################################
#                                             #
#   D E B U T  D I J K S T R A                #
#                                             #
###############################################

""" Grace à la classe Labyrinth on peut récupérer le graphe représentatif du labyrinthe 
    et ainsi on peut uitliser la fonction dijkstra_pred vue en cours pour récupérer la liste des 
    prédécesseurs """

def minimum(dico):
    m=float('inf')
    for k in dico: #parcours des clés
        if dico[k] < m:
            m=dico[k]
            i=k
    return i

def dijkstra_pred(G,s):
    D={} #tableau final des distances minimales
    d={k: float('inf') for k in G} #distances initiales infinies
    d[s]=0 #sommet de départ
    P={} #liste des prédécesseurs
    while len(d)>0: #fin quand d est vide
        k=minimum(d) #sommet de distance minimale pour démarrer une étape
        for i in range(len(G[k])): #on parcourt les voisins de k
            v, c = G[k][i] #v voisin de k, c la distance à k
            if v not in D: #si v n'a pas été déjà traité
                if d[v]>d[k]+c: #est-ce plus court en passant par k ?
                    d[v]=d[k]+c
                    P[v]=k #stockage du prédécesseur de v
        D[k]=d[k] #copie du sommet et de la distance dans D
        del(d[k]) #suppression du sommet de d
    return D, P #on retourne aussi la liste des prédécesseurs



###############################################
#                                             #
#   F I N  D I J K S T R A                    #
#                                             #
###############################################









################################################################
#                                                              #
#   D E B U T  D E  L A  P A R T I E  G R A P H I Q U E        #
#                                                              #
################################################################



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
                


def Modif_Graph(lst,G):
    
    """ Cette fontion remplace les épaisseurs des murs sur le chemin le plus court par des flèches de couleur """
    
    
    
    for j in range(lst.__len__()-1):
        
        if lst[j] == lst[j+1]-1 :
            
            i = lst[j]
            for t in range(G[i].__len__()):
                
                if G[i][t][0] == i+1:
                    txt = ANSI.color_text(36)  + "⇨" + ANSI.stopper()
                    G[i][t] = (G[i][t][0], txt)
                    
            for u in range(G[i+1].__len__()):
                if G[i+1][u][0] == i-1:
                    txt = ANSI.color_text(36)  + "⇨" + ANSI.stopper()
                    G[i+1][u] = (G[i+1][u][0], txt)
                 
        elif lst[j] == lst[j+1]+1 :
            i = lst[j]
            for t in range(G[i].__len__()):
                
                if G[i][t][0] == i-1:
                    txt = ANSI.color_text(36)  + "⇦" + ANSI.stopper()
                    G[i][t] = (G[i][t][0], txt)
            
            for u in range(G[i-1].__len__()):
                if G[i+1][u][0] == i+1:
                    txt = ANSI.color_text(36)  + "⇦" + ANSI.stopper()
                    G[i+1][u] = (G[i+1][u][0], txt)
        else :
            i = lst[j]
            v = lst[j+1]
            
            if i < v :
            
                for t in range(G[i].__len__()):
                    
                    if G[i][t][0] == v:
                        txt = ANSI.color_text(36)  + "⇩" + ANSI.stopper()
                        G[i][t] = (G[i][t][0], txt)
                
                for u in range(G[v].__len__()):
                    if G[v][u][0] == i:
                        txt = ANSI.color_text(36)  + "⇩" + ANSI.stopper()
                        G[v][u] = (G[v][u][0], txt)
            else :
                
                for t in range(G[i].__len__()):
                    
                    if G[i][t][0] == v:
                        txt = ANSI.color_text(36)  + "⇧" + ANSI.stopper()
                        G[i][t] = (G[i][t][0], txt)
                
                for u in range(G[v].__len__()):
                    if G[v][u][0] == i:
                        txt = ANSI.color_text(36)  + "⇧" + ANSI.stopper()
                        G[v][u] = (G[v][u][0], txt)
            

    return G

    
def dessin_graph(c, l):
    
    Mat = [[c*i+j+1 for j in range(c)] for i in range(l)]
    
    for i in range(l):
        for j in range(c):
            if j!= c-1:
                if Mat[i][j]<10:
                    print(Mat[i][j],"-- ",end="")
                else:
                    print(Mat[i][j],"--",end="")
            else : 
                print(Mat[i][j])
        if i!= l-1:
            for j in range(c):
                print("|    ",end="")
            print()
            
                


################################################################
#                                                              #
#   F I N  D E  L A  P A R T I E  G R A P H I Q U E            #
#                                                              #
################################################################











################################################################
#                                                              #
#   F O N C T I O N S  I D O I N E S                           #
#                                                              #
################################################################


""" Les deux fonctions suivantes permettent de générer à partir de la liste des prédécesseurs le 
chemin le plus court allant d'une cellule à une autre  """

def chemin(lst, deb, fin):
    if deb != fin:
        p = [deb]
        p += chemin(lst, lst[deb], fin)
        return p
    else :
        return [fin]

def chemin_court(lst, deb, fin):
    C = chemin(lst, deb, fin)
    return C[:: -1]

""" ---- """



####### Debut Test #######

def Test(c,l):
    M = Labyrinth(c, l)
    L = M.getLab()
    Mat = [[c*i+j+1 for j in range(c)] for i in range(l)]
    List1, List2 = dijkstra_pred(L, Mat[0][0])
    Chem_Court = chemin_court(List2, M.getTaille(), Mat[0][0])
    print(L)
    print()
    print("     GRILLE")
    print()
    graphik(L, c, l)
    print()
    print("     GRAPHE")
    print()
    dessin_graph(c, l)
    print()
    print("Selon Dijkstra, le chemin le plus court allant de ",Mat[0][0]," à ",Mat[-1][-1]," est : ")
    print()
    print("     ",Chem_Court)
    print()
    print("Le poid du chemin est de : ", List1[12])
    print()
    MG = Modif_Graph(Chem_Court, L)
    graphik(MG, c, l)

####### Fin Test #######





####### Debut Partie 2 #######

def PARTIE_2(c, l):
    
    """ Cette fonction génère un labyrinthe puis un court chemin
    Ensuite elle affiche ce chemin selon les conditions de la partie 2 de l'énoncé"""
    
    M = Labyrinth(c, l)
    L = M.getLab()
    Mat = [[c*i+j+1 for j in range(c)] for i in range(l)]
    List1, List2 = dijkstra_pred(L, Mat[0][0])
    Chem_Court = chemin_court(List2, M.getTaille(), Mat[0][0])
    
    R = [[c*i+j+1 for j in range(c)] for i in range(l)]
    nl = []
    for i in range(R.__len__()) :
        
        for j in range(R[i].__len__()):
            
            for u in Chem_Court:
                
                if R[i][j] == u :
                    nl.append((i, j))
    print()
    print("     GRAPHE")
    print()
    dessin_graph(c, l)
    print()
    print("Le chemin le plus court est :")
    print()
    print(Chem_Court)
    print()
    print("Avec les modifications demandées dans l'énoncé du projet, on obtient :")
    print()
    print(nl)
    
####### Fin Partie 2 #######








####### Debut ASTAR #######

def Astar_test(c, l):
    
    
    
    def Creat_heur(col, lig, M):
        
        """ Création de la liste des heuristiques """
        
        heur = {}
        u = 1
        for i in range(lig):
            for j in range(col):
                
                if u == M[i][j]:
                    h = ((col - 1) - j) + ((lig - 1) - i)
                    heur[u] = h
                u+=1
        return heur
    
    
    def HR(h, G):
        moy = G.getMoy()
        for i in range(1,len(h)+1) :
            h[i] = h[i]*int(moy)
        
        return h
    
    def Astar(G,deb,fin,h):
        D={} #tableau final des distances minimales
        d={k: float('inf') for k in G} #distances initiales
        d[deb]=0 #sommet de départ
        dh={k: d[k]+h[k] for k in G} #distances tenant compte de l'heuristique
        while fin in d: #terminé si le sommet fin a été examiné
            k=minimum(dh)#sommet de distance minimale pour démarrer une étape
            for i in range(len(G[k])): #on parcourt les voisins de k
                v, c = G[k][i] #v voisin de k, c la distance à k
                if v not in D: #si v n'a pas été déjà traité
                    d[v]=min(d[v], d[k]+c) #est-ce plus court en passant par k ?
                    dh[v]=d[v]+h[v] #mise à jour distances de l'heuristique
            D[k]=d[k] #copie du sommet et de la distance dans D
            del(d[k]) #suppression du sommet de d
            del(dh[k]) #et de dh
        return D
    
    
    Mat = [[c*i+j+1 for j in range(c)] for i in range(l)]
    heur = Creat_heur(c, l, Mat)
    A = Labyrinth(c, l)
    DL = A.getLab()
    ha = HR(heur, A)
    res = Astar(DL, Mat[0][0], Mat[-1][-1], ha)
    
    """ Affichage """
    print()
    print("     GRILLE ")
    print()
    graphik(DL, c, l)
    print()
    print("     GRAPHE")
    print()
    dessin_graph(c, l)
    print()
    print(" Résultat renvoyé par la fonction A* :")
    print("     ", res)

####### Fin ASTAR #######



################################################################
#                                                              #
#   F I N  F O N C T I O N  I D O I N E                        #
#                                                              #
################################################################









###############################
#                             #
#   D E B U T  M A I N        #
#                             #
###############################
            

""" Test de l'implémentation complète"""

Test(4,3)

""" Fin Test """






""" DEBUT PARTIE 2 """

#PARTIE_2(4,3)

""" FIN PARTIE 2 """






""" DEBUT PARTIE 4 """

#Astar_test(4, 3)

""" FIN PARTIE 4 """

###############################
#                             #
#   F I N  M A I N            #
#                             #
###############################

    
