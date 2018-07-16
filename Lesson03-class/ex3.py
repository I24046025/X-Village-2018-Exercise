class Life:
    def __init__(self,map_arg,pattern_arg):
        self.map=map_arg
        self.pattern=pattern_arg
        
        for i in range(self.map):
            k=[]
            for j in range(self.map):
                sc="*"
                k.append(sc)
            scores.append(k)
            

        for i in range(self.map):
            gg=[]
            for j in range(self.map):
                if i==m and m<=j<=m+2:
                    sc="0"
            
                elif i==m+1 and j==m:
                    sc="0"
            
                elif i==m+2 and j==m+1:
                    sc="0"
            
                else:
                    sc="*"
                gg.append(sc)
            glider.append(gg)
            
    def display(self):
        print("印出nxn map:")
        for i in range(self.map):
            for j in range(self.map):
                print(scores[i][j],end='')
            print()
        
        print("印出 p=1 Glider:")    
        for i in range(self.map):
            for j in range(self.map):
                print(glider[i][j],end='')
            print()



n=int(input("please enter an n to print nxn map:"))
p=int(input("please enter 1 to display Glider:"))
scores=[]
glider=[]
m=int((n-3)/(p+1))

yeap=Life(n,p)
yeap.display()
