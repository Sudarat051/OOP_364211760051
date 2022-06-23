class Student():
    def __init__(self, name, id, age, weigth, height):
        # object attributes
        self.__name = name
        self.__id = id
        self.__age = age
        self.__weigth = weigth
        self.__heigth = height

    # getter and setter methods
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_weight(self):
        return self.__weigth

    def set_weight(self, weigth):
        self.__weigth = weigth

    def get_heigth(self):
        return self.__heigth

    def set_hegith(self, heigth):
        self.__heigth = heigth

    def student_detail(self):
        print(f'STD Name: {self.__name}\n'
                  f'ID: {self.__id}\n'
                  f'Age: {self.__age}\n'
                  f'Weight: {self.__weigth}\n'
                  f'Height: {self.__heigth}\n')

class Vaccine():
    def __init__(self,vac_name):
        self.__vac_name = vac_name

    #getter and setter method
    def get_vaccine(self):
        return self.__vac_name
    def set_vaccine(self,new_name):
        self.__vac_name = new_name

    def vaccine_detail(self):
        print(f'Vaccine name: {self.__vac_name}')

class Vaccinated():
    def __init__(self, student):
        self.student = student
        self.vaccinated = list() # []
        self.date = list() # []
    def add_vaccinated(self,vaccine):
        self.vaccinated.append(vaccine)
    def add_date(self,date):
        self.date.append(date)

    def vaccinated_detail(self):
        print('Student Vaccinated Informations:')
        self.student.student_detail()

        for i in range(len(self.vaccinated)):
            print(f'\tvaccine {i+1}: {self.vaccinated[i].get_vaccine()} date: {self.date[i]}')


# object
std1 = Student('Chalita Sahnguanchao','023',22,54.00,155)
#std1.student_detail()

vac1 = Vaccine('Pizer')
#vac1.vaccine_detail()
vac2 = Vaccine('Moderna')
#vac2.vaccine_detail()

date1 = '10/7/2564'
date2 = '5/1/2565'

std_vac = Vaccinated(std1)
# add data to object
std_vac.add_vaccinated(vac1)
std_vac.add_date(date1)

std_vac.add_vaccinated(vac2)
std_vac.add_date(date2)

# display student vaccinated
std_vac.vaccinated_detail()

# build your interface for input data  -- here
n = input('Student name: ')
id = input('ID: ')

std2 = Student(n,id,35,80.00,180)

"""
input name,id,age,weight,height
input How many vaccinated
select vaccines
input date(str)
"""

name = input('Student Name: ')
id = input('student ID: ')
age = int(input('Age: '))
weight = float(input('Weight (kg): '))
height = float(input('Height (cm): '))

num = int(input('How many your vaccinated ? : '))
vacc = list()
date = list()
select = 0
for x in range(num):
    print('which vaccine: ')
    print('\t1.sinovac')
    print('\t2.astrazeneca')
    print('\t3.johnson&johnson')
    print('\t4.moderna')
    print('\t5.sinopharm')
    print('\t6.pfizer')
    select = int(input('select(1-6)'))
    if select == 1:
        vacc.append('sinovac')
    elif select == 2:
        vacc.append('astrazeneca')
    elif select == 3:
        vacc.append('johnson&johnson')
    elif select == 4:
        vacc.append('moderna')
    elif select == 5:
        vacc.append('sinopharm')
    elif select == 6:
        vacc.append('pfizer')
    else:
        print('Please, enter number 1-6 only')
    d = input('Data: ')
    date.append(d)

print([x for x in vacc])
print([x for x in date])

