#cout number of vowels and consonants in string#
count_vowels=0
count_consonant=0
variable=input('enter a string:')
vowels='AEIOUaeiou'
for i in variable:
    if i in vowels:
        count_vowels+=1
    else:
        count_consonant+=1
print('count_vowels:',count_vowels)
print('count_consonant:',count_consonant)

#input:enter a string:hello#
#output:count_vowels: 2#
#count_consonant: 3#
