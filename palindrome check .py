n=int(input("Enter any no= "))
r=0
n1=n
n2=0
while n1!=0:
    r=n1%10
    n2=n2*10+r
    n1=int(n1/10)
if n2==n:
    print("Its a palindrome")
else:
    print("Its not a palindrome")
    


