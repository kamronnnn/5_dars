# 1 - Masala

#class Person:
#     def __init__(self, full_name, email, phone_number, address):
#         self._full_name = full_name
#         self._email = email
#         self._phone_number = phone_number
#         self._address = address
#
#     @property
#     def full_name(self):
#         return self._full_name
#
#     @full_name.setter
#     def full_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Ism str bolishi kerak")
#         self._full_name = value
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Email str bolishi kerak")
#         self._email = value
#
#     @property
#     def phone_number(self):
#         return self._phone_number
#
#     @phone_number.setter
#     def phone_number(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Tel raqam sonlardan iborat bolishi kerak")
#         if not value.startswith('+998'):
#             raise TypeError('Tel raqam +998 bilan boshlanishi kerak')
#         self._phone_number = value
#
#     @property
#     def address(self):
#         return self._address
#
#     @address.setter
#     def address(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Addres str bolishi kerak")
#         self._address = value
#
#
# person = Person("Kamron Qodirov", "kamron.qodirov@gmail.com", "+998 - 99 - 123 - 44 - 55", "Farg'ona")
#
# print(person.full_name)
# print(person.email)
# print(person.phone_number)
# print(person.address)
#
# person.full_name = "Kamron Qodirov"
# person.email = "kamron.qodirov@gmail.com"
# person.phone_number = "+998 - 99 - 123 - 44 - 55"
# person.address = "Farg'ona"

#=======================================================

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
        with open("products.csv", mode='a') as csv_fila:
            write = csv.writer(csv_fila, lineterminator='\n')
            write.writerow(
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
        self.file_path = file_path
        self.file = open(f"{file_path}.csv")
        self.products = list(csv.reader(self.file))

    def info(self):
        print("\033[32m{}".format("Mahsiulotlar ro'yxati") + '\033[0m')
        for p in self.products:
            print("|", str(p[0]).ljust(4), "|", p[1].ljust(13), "|", str(p[2]).ljust(13), "|", p[3].ljust(13), "|")

    def set_command(self, cmd):
        if cmd == 'add':
            self.__add_product()
        elif cmd == 'delete':
            self.__delete_product()
        elif cmd == 'clear':
            self.__clear_cart()
        elif cmd == 'show_card':
            self.__show_cart()
        elif cmd == 'submit':
            self.__submit_order()

    def __add_product(self):
        product_id = int(input("Mahsulot idsini kiriting: "))
        kg = int(input("Mahsulot kg sini kiriting: "))
        productt = self.products[product_id]

        self.card[product_id] = {"product_name": productt[1], "product_price": productt[2], "kg": kg}
        print("Mahsulot savatchaga qo'shildi.")

    def __delete_product(self):
        product_id = int(input("O'chirish uchun mahsulot idsini kiriting: "))
        if product_id in self.card:
            del self.card[product_id]
            print("Mahsulot savatchadan o'chirildi.")
        else:
            print("Bunday mahsulot savatchada mavjud emas.")

    def __clear_cart(self):
        self.card = {}
        print("Savat tozalandi.")

    def __show_cart(self):
        print("\033[34m{}".format("Savatchadagi mahsulotlar") + '\033[0m')
        for product_id, details in self.card.items():
            print("|", str(product_id).ljust(4), "|", details["product_name"].ljust(13), "|",
                  str(details["product_price"]).ljust(13), "|", str(details["kg"]).ljust(13), "|")

    def __input_card(self):
        card_number = input("Karta raqamini kiriting: ")
        if self.__card(card_number):
            print("Karta qabul qilindi.")
        else:
            print("Noto'g'ri karta raqami.")


shop = Shop("products")
shop.info()

while True:
    commanda = input("Komandani kiriting ('stop' to'xtash uchun): ")
    if commanda == "stop":
        break
    shop.set_command(commanda)

