from PIL import Image, ImageFilter

def z1():
    filename = "leo.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, height  = img.size
    format = img.format
    color = img.mode
    print("Ширина: ",width)
    print("Высота: ",height)
    print("Формат: ",format)
    print("Цветовая модель: ",color)

def z2():
    filename = "leo.jpg"
    with Image.open(filename) as img:
        img.load()
    newsave_img = img.resize((img.width // 3, img.height // 3))
    newsave_img.save("micro-leo.jpg")
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save("LeftLeo.jpg")
    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img.save("Topleo.jpg")

def z3():
    filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in filename:
        with Image.open(file) as img:
            img.load()
            new_file = img.filter(ImageFilter.CONTOUR)
            new_file.show()

def z4():
    water = "leo.jpg"
    with Image.open(water) as img:
        img.load()

    picture = Image.open("leo.jpg").resize(img.size).convert("L")
    pictures = Image.open("leo.jpg")
    pictures = img.resize((100,100))
    cor = "4.jpg"
    with Image.open(cor) as cor:
        cor.load()

    cor.paste(pictures, (10,10), pictures)
    cor.save("water_4.jpg")
    cor.show()

z1()
z2()
z3()
z4()