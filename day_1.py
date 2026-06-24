# 1.print your name
'''
name=input("enter you name:")
print("your name is ",name)
'''

# 2.add two numbers
'''
a=int(input('enter the number 1:'))
b=int(input('enter the number 2:'))
c=a+b
print('the add number are:',c)
'''

# 3.multiple two numbers
'''
a=int(input('enter the number 1:'))
b=int(input('enter the number 2:'))
c=a*b
print('the multiple of numbers result as:',c)
'''

# 4.celsius to fahrenheit
'''
cel=float(input('enter the temperature to converted:'))
far=(cel*9/5)+32
print('the fharenhit is :',far)
'''
# 5.square of two numbers
'''
a=int(input('enter the number to squared'))
b=a**2
print('the squared number if:',b)
'''

# 6.cube of two numbers
'''
a=int(input('enter the number to squared :'))
b=a ** 3
print('the squared number if:',b)
'''

# 7.simple intrest
'''
p=float(input('enter the principle amount :'))
r=float(input('enter the rate of intrest :'))
t=int(input('enter the number of days :'))
t=t/365
si=(p*r*t)/100
print("the simple intrest of the amount is ",si)
'''

# 8.swaping two numbers
'''
a=int(input('enter the number 1 : '))
b=int(input('enter the number 2 : '))
temp =a
a=b
b=temp
print(f'a :{a},b:{b}')
'''

# 9.convert minutes to hours
'''

n=float(input('enter the minutes to covert as the hour'))
h=n/60
print('the hour is :',h)
'''
# 10.getting the datatype of variables


n=10
s='methun sm'
h=2.66666
y=True
print(type(n))
print(type(s))
print(type(h))
print(type(y))
