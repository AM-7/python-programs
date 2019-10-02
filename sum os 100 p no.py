s=-1
for num in range(1,101):
    for i in range(2,num):
        if num%i==0:
            break


    else:
        s=s+num
print("Sum of prime no from 1 to 100= ",s)        
