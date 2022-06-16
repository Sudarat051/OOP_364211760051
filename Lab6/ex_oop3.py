"""
Student Name: Sudarat Suwannasang
ID : 364211760051
Group : MIT212
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Teacher.')

class Student:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Student.')

mylist = []
t = Teacher('Puriwat Lertkrai')
s = Student('Jatuphon Chit')

mylist.append(t)
mylist.append(s)

#print(len(mylist))

for x in mylist:
    x.introduce()