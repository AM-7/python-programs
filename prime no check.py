n=int(input("Enter any no= "))
f=1
for x in range(2,n):
    if n%x==0:
        f=0
        break
if f==0:
    print("Its not a prime no!")
else:
    print("Its a prime no!")
    
