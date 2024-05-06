import os.path
from pathlib import Path
from PIL import Image
import csv
def z1():
    input = Path(r'Z:\1-мд-21\Иванов Ярослав\img')
    output = Path(r'Z:\1-мд-21\Иванов Ярослав\imgnew')
    output.mkdir(parents=True, exist_ok=True)
    for file in input.iterdir():
        if file.suffix in ['.jpg', '.png', '.bmp']:
            input_path = file
            output_path = output / file.name
            image = Image.open(input_path)
            image = image.convert('L')
            image.save(output_path)


def z2():
    input = Path(r'Z:\1-мд-21\Иванов Ярослав\img')
    inputf = os.listdir(input)
    output = Path(r'Z:\1-мд-21\Иванов Ярослав\imgnew')
    if not os.path.exists(output):
        os.mkdirs(output)
    for file in inputf:
        ex = os.path.splitext(file)[1]
        if ex.lower() in ['.jpg', '.png']:
            inputp = os.path.join(input, file)
            outputp = os.path.join(output, file)
            image = Image.open(inputp)
            image = image.convert('L')
            image.save(outputp)


def z3():
    file = open('spisok.csv', 'r', encoding='utf-8')
    data = list(csv.reader(file, delimiter=","))
    print("Список товаров: ")
    for i in data:
        print(f"{i[0]} - {i[1]} шт. за {i[2]} руб")
    print(f"Итоговая цена: {sum([int(i[1]) * int(i[2]) for i in data])} руб.")
z3()
