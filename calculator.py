#basic calculator


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
    for op in operation:
        print(op.upper())
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
