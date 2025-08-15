#reverse the digits of a given number#

n=int(input("enter a number:"))
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
print('reverse is',rev)




#enter a number:345#
#reverse is 543#
