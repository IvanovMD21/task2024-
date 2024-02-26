

def z1():
    a = int(input("введите количество слов "))
    b = 0
    s = ""
    while b != a:
        word = str(input("введите слово "))
        b = b + 1
        s = s + " " +str(word)
    print(s)




def z2():
    s = ""
    word = ""
    while word != "стоп":
        word = input("введите слово ")
        s = s + " " + str(word)
    print(s)


def z3():
    word = str(input())
    if "Ф" in word or "ф" in word:
        print("Ого! Это редкое слово")
    else:
        print("Эх, это не очень редкое слово")


def z4():
    import random
    n = 0
    x = 0
    while n != 3:
        m = random.randint(0, 100)
        k = random.randint(0, 100)
        print(f'{m}+{k}=')
        c = input()
        while not (c.isdigit() and c != "stop"):
            print("Введите число: ")
            c = input()
        if c == "stop":
            break
        if m + k == int(c):
            print("Молодец!")
            x = x + 1
        else:
            print("Ты ошибся!")
            n = n + 1
    print("Игра завершена")
    print("Верных ответов: ", x)



z1()
z2()
z3()
z4()


