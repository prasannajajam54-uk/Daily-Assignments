#count the frequency of each character in a string#
s=input("enter a string:")
freq = {}
for char in s:
    if char in freq:
        freq[char]=+1
    else:
        freq[char]=1
for char, count in freq.items():
    print(f"{char}:{count}")


#enter a string:prasanna#
#output:p:1#
#r:1
#a:1
#s:1
#n:1#
