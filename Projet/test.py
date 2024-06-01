    
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

dessin_graph(9, 9)