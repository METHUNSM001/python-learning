# 1.grade calculator

'''
mark=int(input('enter your mark : '))
if mark>=90:
    print('your grade is A')
elif mark>=75 and mark<90:
    print('your grade is B')
elif mark>=50 and mark<75:
    print('your grade is C')
else:
    print('your grade is F')           
'''

# 2.traffic signal
'''
traffic=input('enter the colour of light(red/yellow/green) : ')
if traffic=='red':
    print('stop')
elif traffic=='yellow':
    print('get ready')
elif traffic=='green':
    print('go')
else:
    print('contact traffic police. Drive slow and carefull')        
'''

# 3.number sign checker

'''
num=int(input('enter the number to be checked : '))
if num>0:
    print('its positive')
elif num<0:
    print('its negetive')
elif num==0:
    print('its netural')
else:
    print('error')           
'''

# 4.discount calculator
'''
amt = float(input('Enter the amount of things purchased: '))

if amt >= 5000:
    dis = amt * 0.05
    print('Discount =', dis)
    print('Final amount =', amt - dis)
elif amt >= 2000:
    dis = amt * 0.02
    print('Discount =', dis)
    print('Final amount =', amt - dis)
else:
    print('You have a gift')
    print('Final amount =', amt)

'''

# 5.electricity bill
'''
units=int(input('enter the electricity units'))

if units<=100:
    bill = units*2
elif units<=200:
    bill=(100*2)+((units-100)*3)
else:
    bill=(100*2)+(100*3)+((units-200)*5)   

print("your electricity bill is : ",bill)     
'''
# 6.bmi calculator
'''
w=float(input('enter weight : '))
h=float(input('enter height : '))

bmi=w/(h**2)

if bmi<18.5:
    print('under weight')
elif bmi<25:
    print('normal')
elif bmi<30:
    print('over weight')
else:
    print('obese')            
'''

# 7.age category
'''
age=int(input('enter your age'))
if age<13:
    print('you are child')
elif age<20:
    print('you are teen') 
elif age<60:
    print('you are adult') 
else:
    print('you are senior citizen')          
'''
# 8.login valditation
'''
user=input('enter the user name : ')
pas=input('enter the passward : ')

if user=='methun' and pas=='1234':
    print('successfully logged in')
else:
    print('user name or passward is incorrect check and try again !')    
'''

# 9.triangle validity
'''
a=float(input('enter the side one : '))
b=float(input('enter the side two : '))
c=float(input('enter the side three : '))

if a+b>c and a+c>b and b+c>a:
    print('valid triangle')
else:
    print('not a valid triangle')    
'''
# 10.quadratic roots 

a=float(input("enter a : "))
b=float(input("enter b : "))
c=float(input("enter c : "))
d=b**2-4*a*c
if d>0:
    print('two distinct roots')
elif d==0:
    print('one root is repeated')
else:
    print('two complex roots')        
