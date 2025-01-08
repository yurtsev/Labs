def isitnumber(x):
    try:
        int(x)
        return True
    except:
        return False


def is_prime(x):
    k = 0
    x = float(x)
    for i in range(1, int(x ** 0.5) + 2):
        if x % i == 0:
            k += 2
    if k == 2:
        return True
    if k > 2:
        return False


def describe_person(name, age):
    while not isitnumber(age):
        age = input('введите возраст:')
        if isitnumber(age):
            x = int(age)
            if x <= 20:
                if x == 1:
                    print(f"Имя: {name} / возраст: {age} год")
                if 2 <= x <= 4:
                    print(f"Имя: {name} / возраст: {age} год")
                if 5 <= x <= 20:
                    print(f"Имя: {name} / возраст: {age} год")
            if x > 20:
                lastletter = int(str(x)[-1])
                if lastletter == 1:
                    print(f"Имя: {name} / возраст: {age} год")
                if 2 <= lastletter <= 4:
                    print(f"Имя: {name} / возраст: {age} год")
                if 5 <= lastletter <= 9 or lastletter == 0:
                    print(f"Имя: {name} / возраст: {age} год")
        else:
            print("В графе 'возраст' вы ввели не число")


name = input('введите имя:')
age = ''

describe_person(name, age)

print("--------task 2--------")
number = input('Введите число')
print(is_prime(number))
