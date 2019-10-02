n=int(input("Enter no of rows= "))
n1=0
n2=0
if n%2==0:
    for a in range(1,int(n/2+1)):
        for b in range(1,a+1):
            print("* ",end="")
        print()
    for c in range(int(n/2),0,-1):
        for d in range(1,c+1):
            print("* ",end="")
        print()   
    
else:
    n1=int(n/2)
    n2=int(n/2+1)
    for a in range(1,n1+1):
        for b in range(1,a+1):
            print("* ",end="")
        print()
    for c in range(n2,0,-1):
        for d in range(1,c+1):
            print("* ",end="")
        print()        
