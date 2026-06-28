# 1.print 1 to 100 using for loop
'''
for i in range(1, 101):
    print(i)
'''

# 1.print 1 to 100 using while loop 
'''
i=1
while (i<101):
    print(i)
    i +=1
'''
# 2.sum the numbers 1 to 100 using for loop
'''
total=0
for i in range(1,101):
 total +=i
 print(total)
'''
# 2.sum the number 1 to 100 using while 
'''
i=1
total=0
while(i<101):
    total +=i
    i +=1
    print(total)
'''
# 3.multiplication table using for loop
'''
n=int(input('enter the number of the table you want : '))

for i in range(1,11):
    print(i,'x',n,'=',n*i)
'''
# 3.multiplication table using while loop

'''
n=int(input('enter the number of table you want : '))

i=1
while i<=10:
    print(i,'x',n,'=',i*n)
    i += 1
'''
# 4.factorail using for loop
'''
n= int(input("Enter a number: "))
f = 1

for i in range(1, n+1):
    f*= i

print("Factorial =", f)
'''
# 4.factorial using while loop
'''
n=int(input('enter the number to find the factorial : '))
f=1
i=1
while i<=n:
    f*=i
    i+=1

print('the factorial is',f)  
'''
# 5.reversing the number using for loop
'''
for i in range(100,0,-1):
    print(i)
'''    
# 5.reversing the number using while loop
'''
i=100
while i>= 1:
    print(i)
    i -= 1
'''
# 6.suming the entered values using for loop
'''
n=int(input('enter the numbers need to be sumed : '))
total=0
for i in range(n):
     l=int(input(f'Enter element {i+1}: '))
     total +=l

print('the sume of entered values are',total)    

'''
# 6.suming the entered values using while loop

n=int(input('enter the number of element to be added : '))
total=0
i=1
while i<=n:
     l=int(input(f'Enter element {i}: '))
     total +=l
     i+=1

print('the summed number is',total)



