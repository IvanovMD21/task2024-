import json
def z1():
    with open('spis.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for products in data['products']:
        print(f'Название: {products["name"]}'
              '\n' f' Цена: {products["price"]}'
              '\n' f' Вес: {products["weight"]}')
        if products['available']:
            print("В Наличии")
        else:
            print('Нет в наличии')


def z2():
    with open('spis.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    new_product = {
        "name": input("Введите название товара: "),
        "price": input("Введите стоимость товара: "),
        "available": input("Товар в наличие?(True/False): "),
        "weight": int(input("Введите вес товара: "))
    }
    data["products"].append(new_product)
    with open('spis.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    with open('spis.json', 'r', encoding='utf-8') as file:
        new_data = json.load(file)

    for products in new_data['products']:
        print(f'Название: {products["name"]}'
              '\n' f' Цена: {products["price"]}'
              '\n' f' Вес: {products["weight"]}')
        if products['available']:
            print("В Наличии")
        else:
            print('Нет в наличии')

def z3():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    ru_en = {}
    for line in lines:
        eng_word, ru_tr = line.strip().split('-')
        for ru_word in ru_tr.split(','):
            if ru_word.strip() not in ru_en:
                ru_en[ru_word.strip()] = [eng_word]
            else:
                if eng_word not in ru_en[ru_word.strip()]:
                    ru_en[ru_word.strip()].append(eng_word)
    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for key in sorted(ru_en.keys()):
            trans = ','.join(sorted(ru_en[key]))
            file.write(f'{key}-{trans}\n')

z3()

