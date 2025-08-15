#print the fibonacci series up to n terms#
n=int(input("enter the number:"))
a=0
b=1
c=0
print(a)
print(b)
while(n>0):
    c=a+b
    a=b
    b=c
    n=n-1
    print(c)

    
#enter the number:12#
#0
#1
#1
#2
#3
#5
#8
#13
#21
#34
#55
#89
#144
#233#
