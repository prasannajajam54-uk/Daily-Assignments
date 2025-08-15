#check if given number is prime or not#
n=int(input())
i=1
cnt=0
while(i<=n):
      if n%i==0:
          cnt+=1
          i+=1
          if cnt==2:
              print('prime')
          else:
                  print('not prime')

#input:13#
#output:not prime#

