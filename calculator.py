'''
L=[1,2,3,4,5,6,7,8,]
L[1:3]=L[5:7]
print(L)
L[1:1]=[2,3]
print(L)
del L[3:5]
print(L)
L.extend([9,10])
print(L)
print(sum(L))
L2=['aksdjfl','AdkO','KLASJFLJ']
print(sorted([x.capitalize() for x in L2],reverse=True),L2[1][0:3].replace('k','*'))

list=['a','y','a','z']
print (''.join(list))
'''

#below coding is for basic calculator


#for addition
def addition():
    n=int(input('for addition '+'\nenter the number :'))+int(input('enter the number :'))
    print(n)

#multiplication
def multiplication():
    n=int(input("for multiplication "+'\nenter the number :'))*int(input('enter the number :'))
    print(n)


#for substraction
def substraction():
    n=int(input("for substraction "+'\nenter the number :')) - int(input('enter the number :'))
    print(n)


#for division
def division():
    n=(int(input("for division "+'\nenter the number :'))) // int(input('enter the number :'))
    print(float(n))


active = True
while active:
    print('Basic calculator'+'\nSelect the operation below\n')
    operation=['\t1= addition +','\t2= multiplication x','\t3= substraction -','\t4= division /', '\t5= quit']
    #for op in operation:
     #   print(op.upper())
    user = int((input('\nselect the option number: ')))
    message = user

    if message == 5:
        print(('Thanks for using this calculator'))
        active = False
    elif user >= 6:
        print('please select numbers from the list')
    elif user == 1:
        print(addition())
    elif user == 2:
        print(multiplication())
    elif user == 3:
        print(substraction())
    elif user == 4:
        print(division())
