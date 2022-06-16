"""
Student Name: Sudarat Suwannasang
ID : 364211760051
Group : MIT212
"""

# Encapsulation

class Student:
    def __init__(self):
        # object attributes
        self.name = ''  # public member
        self.__age = 0    # private member  age >=18
        self._major = 'MT'  # protected


    # getter and setter methods
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age >= 18:
            self.__age = new_age
        else:
            #print('Age should be higher than 18.')
            raise ValueError('Age should be higher than 18.')


    def display_info(self):
        print(f'Name: {self.name} Age: '
              f'{self.__age} '
              f'Major: {self._major}')

# std1 = Student('Purwiat',35)
# std1.display_info()

# using getter method
# print(std1.get_age(),type(std1.get_age()))
# myage = std1.get_age()
# print(myage)

# using setter method
# std1.set_age('18a')
# print(std1.get_age())

# std1.set_age('Hello')
# print(std1.get_age())

print('Enter your student detail')

name = input('Student name: ')
age = int(input('age: '))

std2 = Student()  # call init()
std2.name = name
std2.set_age(age)

std2.display_info()