# 1.reverse a string 
'''
s=input('enter the stentence : ')
print('the reversed string is : ',s[::-1])
'''
# 2.count vowl and cons
'''

s=input('enter the sentence :')
vow='aeiouAEIOU'
v_c=0
c_c=0
for ch in s:
    if ch.isalpha():
        if ch in vow:
            v_c +=1
        else:
            c_c +=1
print('voewls in sentence : ',v_c)
print('consonants in sentence : ',c_c)

'''
# 3.palindrome string cheacking
'''
s=input('enter the sentence : ')
if s==s[::-1]:
    print('its palindrome string')
else:
    print('not a palindrome')
'''
# 4.character frequency
'''
s=input('enter the sentence : ')
print("Character Frequency:")
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for key, value in freq.items():
    print(key, ":", value)
'''
# 5.upper and lower case
'''
s=input('enter the sentence : ')
print('upper_string :',s.upper())
print('lower_string :',s.lower())
'''
# 6.replace character
'''
s=input('enter the sentence :')
old=input('enter the old character to replaced :')
new=input('enter the new characater to replced insted of old :')
print('the replaced character is :',s.replace(old,new))
'''
# 7.removing the space
'''
s=input('enter the sentence :')
print('the space between the sentence has me removed',s.replace(" ",""))
'''
# 8.count the number of words in the sentence

s=input('enter the sentence :')
words=s.split()
print('the number of words in the sentence',len(words))