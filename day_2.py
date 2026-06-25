# 1.even/odd
'''
n=float(input('enter the number :'))
if n%2==0:
    print('its even')
else:
    print('its odd')
'''

# 2.+ve/-ve
'''
n=float(input('enter the number :'))
if n>0:
    print('it\'s positive')
else:
    print('its negetive')
'''

# 3.largest number
'''
n=float(input('enter the num 1 :'))
b=float(input('enter the num 2 :'))
if n>b:
    print(n,'is greater then ',b)
else:
    print(b,'is greater then ',n)
'''

# 4.smallest number
'''
a=float(input('enter the number'))
b=float(input('enter the number'))
if a<b:
    print(a,'is smaller then',b)
else:
    print(b,'smaller then',b) 
'''

# 5.number div by 5

'''
n=int(input('enter the number : '))
if n%5==0:
    print(n,'entered number is div by 5 ')
else:
    print(n,'not div by 5')    
'''
# 6.div by 3 and also 5
'''
n=int(input('enter the number : '))
if n%3==0 and n%5==0:
    print('entered number is div by both 3 and 5')
else:
    print('the number is not div by both')
'''
# 7.voting
'''
name=input('enter your name : ')
age=int(input('enter your age : '))
if age>18:
    print(name,'you can vote !')
else :
    print(name,'wait until you are above 18')
print('thank you !')
'''

# 8.leap year
'''
year=int(input('enter the year'))
if (year%400==0) or (year %4==0 and year %100 !=0):
    print('its a leap year !')
else:
    print('it\'s normal year ')
'''

# 9.gratest among 3 numbers
'''
a=int(input('enter the number 1 : '))
b=int(input('enter the number 2 : '))
c=int(input('enter the number 3 : '))
if a>b and a>c:
    print(a,'is greater then ',b,',',c)
elif b>a and b>c:
    print(b,'is greater then',a,',',c)
else :
    print(c,'is greater then',a,',',b)    
'''

# 10.calculator
'''
n1=float(input('enter the number : '))
n2=float(input('enter the number : '))
op=input('enter the operation(+,-,x,/)') 

if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='x':
    print(n1*n2)
elif op=='/':
    print(n1/n2)        
'''


