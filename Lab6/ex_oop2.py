"""
Student Name: Sudarat Suwannasang
ID : 364211760051
Group : MIT212

"""

# class attributes

class Student:
    # class attribute
    major = 'MIT'

    def __init__(self,name,group):
        # object attributes
        self.name = name
        self.group = group
    def introduce(self):
        print(f'My name is {self.name}, I\'m in {self.group} and'
              f' studying in {self.major} major.')

std1 = Student('Puriwat Lertkrai','MIT212')
std1.introduce()

std2 = Student('Piyapong Senanut','MIT211')
std2.introduce()

Student.major = 'LM'

std1.introduce()
std2.introduce()

std2.group = 'LM211'
std2.introduce()