# Inkap ---> Public, Protected, private
# Poli
# Abstraction
# Inher

# class User:
#     def __init__(self, name, lastname, age):
#         self.__name = name
#         self.lastname = lastname
#         self.age = age
#
#     def __bool__(self):
#         return False
#
#     def __ne__(self, other):
#         pass
#
#     def __eq__(self, other):
#         pass
#
#     def __le__(self, other):
#         pass
#
#     def __lt__(self, other):
#         pass
#
#     def __ge__(self, other):
#         pass
#
#     def __gt__(self, other):
#         pass
#
#
# user = User("Toxir", "Toxirov", 27)


# --------------------------------------------------------------------------------------------------
# Descriptor lar

# class Age:
#     def __init__(self):
#         self.__age = 0
#
#     def __get__(self, instance, owner):
#         return self.__age
#
#     def __set__(self, instance, value):
#         if type(value) is not int:
#             raise TypeError("Yosh butun son bo'lishi kerak")
#
#         if value < 0:
#             raise ValueError("Yosh 0 dan katta bo'lishi kerak")
#
#         self.__age = value
#
#     def __delete__(self, instance):
#         del self.__age
#
#
#
# class Name:
#     def __init__(self):
#         self.__name = ""
#
#     def __get__(self, instance, owner):
#         return self.__name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise TypeError("Name str bo'lishi kerak")
#
#         if not value.isalpha():
#             raise ValueError("Name faqat harflardan iborat bo'lishi kerak")
#
#         self.__name = value
#
#     def __delete__(self, instance):
#         del self.__name
#
#
# class User:
#     name = Name()
#     lastname = Name()
#     age = Age()
#
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#
# user = User("Toxir", "Toxirov", 12)
# toxir = User("Toxir", "Toxirov", 45)
# print(user.age)
# del user.age


# -----------------------------------------------------------------------
import csv

with open("products.csv", mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(
        ["ID", "PRODUCT_NAME", "PRODUCT_PRICE", "CATEGORY"]
    )


class Price:
    def __init__(self):
        self.__price = 0

    def __get__(self, instance, owner):
        return self.__price

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Butun son bo\'lishi kerak')

        if value < 0:
            raise ValueError("Nolda katta bolsin")

        self.__price = value

    def __delete__(self, instance):
        del self.__price


class Product:
    product_price = Price()

    def __init__(self, product_id, product_name, product_price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.category = category
        self.write()

    def write(self):
        with open("products.csv", mode='a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(
                [self.product_id, self.product_name, self.product_price, self.category]
            )


products = [
    [1, "Olma", 1000, "Meva"],
    [2, "Anor", 15000, "Meva"],
    [3, "Behi", 18000, "Meva"],
    [4, "Shaftoli", 50000, "Meva"],
    [5, "Kartoshka", 5000, "Sabzavot"],
    [6, "Sabzi", 4000, "Sabzavot"],
]

for product in products:
    Product(product[0], product[1], product[2], product[3])



class Shop:
    card = {}

    def __init__(self, file_path):
        self.file = open(f"{file_path}.csv")
        self.products = list(csv.reader(self.file))

    def info(self):
        print("\033[32m{}".format("Mahsiulotlar ro'yxati") + '\033[0m')
        for p in self.products:
            print("|", p[0].center(13, " "), "|", p[1].center(13, " "), "|", p[2].center(13, " "), "|", p[3].center(13, " "), "|")

    def set_command(self, command):
        if command == 'add':
            self.__add_product()

    def __add_product(self):
        product_id = int(input("Mahsulot idsini kiriting: "))
        kg = int(input("Mahsulot kg sini kiriting: "))
        product = self.products[product_id]

        self.card[product_id] = {"product_name": product[1], "product_price": product[2], "kg": kg}
        print(self.card)

shop = Shop("products")
shop.info()

while True:
    command = input("Komandani kiriting: ")
    if command == "stop":
        break
    shop.set_command(command)

# delete
# clear
# submit