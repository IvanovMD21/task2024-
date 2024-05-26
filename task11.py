import tkinter as tk
def z1():
    class Restaurant:
        def __init__(self, name, cuisine, rating=0):
            self.name = name
            self.cuisine = cuisine
            self.rating = rating
        def describe(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.cuisine}")
            print(f"Рейтинг: {self.rating}")
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine, rating=0):
            super().__init__(name, cuisine, rating)
            self.flavors = []
        def display_flavors(self):
            print("Виды мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    ice_cream = IceCreamStand("Сладкая жизнь", "Ice Cream", 4)
    ice_cream.flavors = ["Кактус", "Ананас", "Арбуз"]
    ice_cream.display_flavors()



def z2():
    class Restaurant:
        def __init__(self, name, cuisine, rating=0):
            self.name = name
            self.cuisine = cuisine
            self.rating = rating
        def describe(self):
            print(f"Название ресторана: {self.name}")
            print(f"Тип кухни: {self.cuisine}")
            print(f"Рейтинг: {self.rating}")
    class IceCreamStand(Restaurant):
        def __init__(self, name, cuisine, rating=0, location=None, hours=None):
            super().__init__(name, cuisine, rating)
            self.flavors = []
            self.location = location
            self.hours = hours
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
        def has_flavor(self, flavor):
            return flavor in self.flavors
        def display_flavors(self):
            print("Вкусы мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")

    ice_cream = IceCreamStand("SweetLife", "Ice Cream", 4, "ул. Пушкина, д. Колотушкина", "08:00 - 18:00")
    ice_cream.add_flavor("Ананас")
    ice_cream.add_flavor("Кактус")
    ice_cream.add_flavor("Арбуз")
    ice_cream.remove_flavor("Шоколадное")
    print(ice_cream.has_flavor("Черничное"))
    print(ice_cream.has_flavor("С Кактусом"))
    ice_cream.display_flavors()



def z3():
    class IceCreamStand:
        def __init__(self, master):
            self.master = master
            self.master.title("Sweet Life")

            self.flavor_frame = tk.Frame(self.master)
            self.flavor_frame.pack(side=tk.LEFT)

            self.flavors = ["Кактус", "Ананас", "Арбуз", "Маракуя"]
            self.flavor_list = tk.Listbox(self.flavor_frame)
            for flavor in self.flavors:
                self.flavor_list.insert(tk.END, flavor)
            self.flavor_list.pack()

            self.add_button = tk.Button(self.flavor_frame, text="Добавить в заказ", command=self.add_flavor)
            self.add_button.pack()
            self.remove_button = tk.Button(self.flavor_frame, text="Убрать из заказа", command=self.remove_flavor)
            self.remove_button.pack()

            self.order_frame = tk.Frame(self.master)
            self.order_frame.pack(side=tk.RIGHT)

            self.order_list = tk.Listbox(self.order_frame)
            self.order_list.pack()

            self.order_button = tk.Button(self.order_frame, text="Заказ", command=self.place_order)
            self.order_button.pack()

        def add_flavor(self):
            selected_flavor = self.flavor_list.get(tk.ACTIVE)
            self.order_list.insert(tk.END, selected_flavor)
        def remove_flavor(self):
            selected_flavor = self.order_list.get(tk.ACTIVE)
            self.order_list.delete(tk.ACTIVE)
        def place_order(self):
            print("Вы заказывали: ")
            for item in self.order_list.get(0, tk.END):
                print(f"- {item}")
    root = tk.Tk()
    ice_cream = IceCreamStand(root)
    root.mainloop()


z1()
z2()
z3()