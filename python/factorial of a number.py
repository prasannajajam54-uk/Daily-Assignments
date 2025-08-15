#find the factorial of a number#
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter a number:"))
print(f"factorial of {num} is {factorial(num)}")


#output:enter a number:4#
#factorial of 4 is 24#
