def isitnumber(x):
    try:
        int(x)
        return True
    except:
        return False

#-------start task 1 ----------
x = None
while not isitnumber(x):
    x = input('Введите число:')
    if isitnumber(x):
        x = int(x)
        for i in range(1,x+1):
            print(i)
    else:
        print('Вам нужно ввести целое число! Попробуйте снова.')
#-------end task 1 ------------

#-------start task 2 ----------
a = b = None
while not isitnumber(a) or not isitnumber(b):
    a = input('Введите первое число:')
    b = input('Введите второе число:')
    if isitnumber(a) and isitnumber(b):
        a = int(a)
        b = int(b)
        print('Большее число:', max(a, b))
    else:
        print('Вы ввели не число! Попробуйте снова.')
#-------end task 2 ------------
