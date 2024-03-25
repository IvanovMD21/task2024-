def z1():
    list = [43, 56, 23, 86, 12]
    a = int(input("Введите число: "))
    if a in list:
        print(*list, a)
        print('Поздравляю, вы угадали число!')
    else:
        print('Нет такого числа!')

def z2():
    list = [35, 23, "бегемот", 87, "жираф", 23]
    x = 0
    for i in list:
        if list.count(i) >= 2 and x != i:
            print(i)
            x = i
            break
    else:
        print("Повторяющихся значений в списке нет")



def z3():
    list = ("пн", "вт", "ср", "чт", "пт", "сб", "вс")
    x = int(input("Сколько выходных ты хочешь? "))
    print("Выходные дни: ", *list[len(list)-x:])
    print("Рабочие дни: ", *list[:-x])


def z4():
    import random
    group1 = ["Чипсыма", "Торхов", "Здобнов", "Уланова", "Одинцов", "Озеров", "Киселева", "Соловьева", "Кузнецов",
              "Петров"]
    group2 = ["Алексеев", "Вдовин", "Куприянов", "Филиппов", "Воронков", "Дулина", "Любимов", "Жилин", "Михайлова",
              "Иванов"]
    x = list(range(10))
    random.shuffle(x)
    y = list(range(10))
    random.shuffle(y)
    sportgroup = [group1[i] for i in x[:5]] + [group2[i] for i in y[:5]]
    print('\n first: ', *group1, '\n second: ', *group2, '\n sportgroup: ', *sportgroup)
    print('Длина: ', len(sportgroup))
    sportgroup = sorted(sportgroup)
    print('Отсортированный список: ', *sportgroup)
    if "Иванов" in sportgroup:
        print('Иванов в команде!')
        print('Сколько Ивановых: ', sportgroup.count("Иванов"))
    else:
        print('Иванова в команде нет')


z1()
z2()
z3()
z4()