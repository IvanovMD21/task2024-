def z1():
    a = int(input("введите число = "))
    if a % 3 == 0:
        print("это число делится на 3 ")
    else:
        print("введите правильное число")


def z2():
    try:
        a = int(input("ввод числа "))
        n = 100 / a
    except ValueError:
        print("это не число")
    except ZeroDivisionError:
        print("введен 0")
    else:
        print(n)

def z3():
    date = input("Формат: дд.мм.гггг: ").split(".")

    print(date)
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print("Магическая дата")
    else:
        print("не магическая дата")


def z4():
    tic = input("введите номер билета: ")
    a = 0
    b = 0
    if len(tic) % 2 == 0:
        for i in tic[int(len(tic) / 2)]:
            a = a + int(i)
        for i in tic[int(len(tic) / 2):int(len(tic)) + 1]:
            b = b + int(i)
        if a == b:
            print("Счастливый белет")
        else:
            print("Не счастливый билет")
    else:
        print("не четно")


z1()
z2()
z3()
z4()

