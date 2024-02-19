def z1():
    a = input("введите пароль: ")
    b = input("введите пароль еще раз: ")
    if a == b:
        print("Пароль принят")
    else:
        print("пароль не принят")



def z2():
    place = int(input("Введите место: "))

    if place % 2 == 0 and place >= 1 and place <= 36:
        print("Купе верхнее")
    elif place % 2 == 1 and place >= 1 and place <= 36:
        print("Купе нижнее")
    elif place % 2 == 0 and place >= 37 and place <= 53:
        print("Боковое верхнее")
    elif place % 2 == 1 and place >= 37 and place <= 53:
        print("Боковое нижнее")
    else:
        print("Неверно указано место")


def z3():
    year = int(input("введите год: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Год високосный")
    else:
        print("Этот год не високосный")

def z4():
    x = input("введите 1 цвет: ")
    y = input("введите 2 цвет: ")
    if (x == "красный" and y == "синий") or (y == "красный" and x == "синий"):
        print("Получился фиолетовый цвет")
    elif (x == "красный" and y == "желтый") or (y == "красный" and x == "желтый"):
        print("Получился оранжевый цвет")
    elif (x == "синий" and y == "желтый") or (y == "синий" and x == "желтый"):
        print("Получился зеленый цвет")
    else:
        print("я еще не умею такое смешивать")

z1()
z2()
z3()
z4()


