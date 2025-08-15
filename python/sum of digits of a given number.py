#fid the sum of digits of a given number#
n=int(input("enter the number:"))
sum=0
while(n>0):
    r=int(n%10)
    sum=int(sum+r)
    n=n/10
print("sum of digits is:",sum)



#output:enter the number:59#
#sum of digits is: 14#
