import tkinter as tk

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} открыт!")
    def update_rating(self, new_rating):
        self.rating = new_rating

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, opening_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        self.location = location
        self.opening_hours = opening_hours
        self.ice_cream_types = {
            "Рожок": [],
            "Станканчик": []
        }


    def display_flavors(self):
        if self.flavors:
            print("Доступные типы мороженного:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print("Доступных типов мороженного нет.")



    def add_flavor(self, new_flavor):
        self.flavors.append(new_flavor)

    def remove_flavor(self, flavor_to_remove):
        if flavor_to_remove in self.flavors:
            self.flavors.remove(flavor_to_remove)
        else:
            print(f"{flavor_to_remove} не найден в меню.")

    def check_flavor(self, flavor_to_check):
      return flavor_to_check in self.flavors

    def add_ice_cream_type(self, ice_cream_type, flavors):
        if ice_cream_type in self.ice_cream_types:
            self.ice_cream_types[ice_cream_type].extend(flavors)
        else:
            print(f"Мороженного типа '{ice_cream_type}' нет в меню.")


    def display_ice_cream_types(self):
        for ice_cream_type, flavors in self.ice_cream_types.items():
            if flavors:
                print(f"\n{ice_cream_type.replace('_', ' ').title()}:")
                for flavor in flavors:
                    print(f"- {flavor}")

morozhenka = IceCreamStand("Мороженка", "Мороженное", "Ударников д. 30", "8:30 - 19:00")
morozhenka.add_flavor("Шоколадное")
morozhenka.add_flavor("Ванильное")
morozhenka.add_flavor("Вишневое")


morozhenka.add_ice_cream_type("Рожок", ["Шоколадный", "Вишневый"])
morozhenka.add_ice_cream_type("Станканчик", ["Ванильный", "Со вкусом манго"])
morozhenka.describe_restaurant()

morozhenka.display_ice_cream_types()

# 14.3

def display_ice_cream():
    flavors = ["Шоколадный", "Ванильный", "Вишневый"]
    flavor_listbox.delete(0, tk.END)
    for flavor in flavors:
        flavor_listbox.insert(tk.END, flavor)

root = tk.Tk()
root.title("Мороженка")
heading_label = tk.Label(root, text="Приветствуем в кафе Мороженка!", font=("Arial", 16))
heading_label.pack(pady=10)
flavor_listbox = tk.Listbox(root, width=30)
flavor_listbox.pack()
display_button = tk.Button(root, text="Показать сорты", command=display_ice_cream)
display_button.pack(pady=10)
root.mainloop()
