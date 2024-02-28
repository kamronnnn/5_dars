# class Age:
#     def __init__(self):
#         self.__age = 0
#
#     def __get__(self, instance, owner):
#         raise self.__age
#
#     def __set__(self, instance, value):
#         if (value) is not int:
#             raise TypeError('Yosh integer bolish kerak')
#
#         if value < 0:
#             raise ValueError('Yosh 0 dan katta bolish kerak')
#
#         self.__age = value
#
#     def __delete__(self, instance):
#         del self.__age
#
# class User:
#     age = Age()
#
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
# user = User('Kamron', 'Qodirov', 15)
# print(user.age)
# del user.age

#===================================================================

# class Name:
#     def __init__(self):
#         self.__name = ""
#
#     def __get__(self, instance, owner):
#         return self.__name
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError('Name faqat harflardan ibort bolish kerak')
#
#         self.__name = value
#
#     def __delete__(self, instance):
#         del self.__name
#
# class User:
#     name = Name()
#
#     def __init__(self, name, last_name, age):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#
# user = User('Kamron', 'Qodirov', 15)
# print(user.age)

#===================================================================
import csv
with open('product_csv', mode='w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(
        ['ID', 'PRODUCT_NAME', 'PRODUCT_PRICE', 'CATEGORY']
    )

class Product_price:
    def __init__(self):
         self.__product_price = 0

    def __get__(self, instance, owner):
        return self.__product_price

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Price faqat sonlardan iborat bolishi kerak')

        if value < 0:
            raise ValueError('Price 0 dan katta bolishi kerak')

        self.__product_price = value

    def __delete__(self, instance):
        del self.__product_price

class Product:
    product_price = Product_price()

    def __init__(self, product_id, product_name, product_price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.category = category
        self.write()

    def write(self):
        with open('product_csv', mode='a') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(
                [self.product_id, self.product_price, self.category]
            )

p1 = Product(1, 'Olma', 5000, 'Meva')

products = (
    [2, 'Anor', 10000, 'Meva']
    [3, 'Bexi', 3000, 'Meva']
    [4, 'Shaftoli', 7000, 'Meva']
)

for product in products:
    Product(product[0], product[1], product[2], product[3])














