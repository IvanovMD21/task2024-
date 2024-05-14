def z1():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
        def describe(self):
            print(f'Ресторан {self.name}:  {self.cuisine} кухня')
        def open(self):
            print(f'{self.name} сейчас открыт')

    newRestaurant = Restaurant("ChinaTown", "Китайская")
    newRestaurant.describe()
    newRestaurant.open()

def z2():
    class Restaurant:
        def __init__(self, name, cuisine):
            self.name = name
            self.cuisine = cuisine
        def describe(self):
            print(f'Ресторан {self.name}:  {self.cuisine} кухня')
        def open(self):
            print(f'Ресторан {self.name}:  сейчас работает')
    newRestaurant1 = Restaurant("ChinaTown", "Китайская")
    newRestaurant2 = Restaurant("INDUSION", "Индийская")
    newRestaurant3 = Restaurant("MEXICOSITY", "Мексиканская")
    newRestaurant1.describe()
    newRestaurant2.describe()
    newRestaurant3.describe()


def z3():
    class Restaurant:
        def __init__(self, name, cuisine, rating=0):
            self.name = name
            self.cuisine = cuisine
            self.rating = rating
        def describe(self):
            print(f'Ресторан {self.name}:  {self.cuisine} кухня')
        def open(self):
            print(f'Ресторан {self.name}:  сейчас работает')
        def newRating(self, new_rating):
            if new_rating > 0 and new_rating <= 10:
                self.rating = new_rating
            print(f'Рейтинг: {self.rating} очков')
    newRestaurant1 = Restaurant("ChinaTown", "Китайская")
    newRestaurant2 = Restaurant("INDUSION", "Индийская")
    newRestaurant3 = Restaurant("MEXICOSITY", "Мексиканская")
    newRestaurant1.describe()
    newRestaurant1.newRating(0)
    newRestaurant2.describe()
    newRestaurant2.newRating(0)
    newRestaurant3.describe()
    newRestaurant3.newRating(0)


z1()
z2()
z3()


