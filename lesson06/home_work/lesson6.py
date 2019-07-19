def funk_1():
    pass
def funk_2():
    pass

temp_dict = {
    'command1': funk_1,
    'command2': funk_2,
}

# people_dict = {
#     'name': str('Василий'),
#     'surname': str('Иванов'),
#     'patronum': str('Алексеевич'),
#     'sex': str('Муж'),
#     'b_data': str('1988-03-09'),
# }

# name = people_dict['name'] # - неудобно множеством вводимых даных на множество людей
# import random
# class Human:
#     def __init__(self, name, surname, patronum,sex,b_data):
#         self.name = name # - создание и объявления аргументов нашего класса
#         self.surname = surname
#         self.patronum = patronum
#         self.sex = sex
#         self.b_data = b_data
#         self.__ids = random.randint(1, 1000)
#
#     def fio(self):
#         return f'{self.__ids} - {self.surname} {self.name} {self.patronum}'
#
# human1 = Human('Василий', 'Иванов' ,'Алексеевич', 'Муж','1988-03-09')
# # print(human1.name)
# print(human1.fio())
# # print(human1._ids)
# human1.surname = 'Петров'
# print(human1.fio())



import random
class Human:
    def __init__(self, name, surname, patronum, sex, b_data):
        self.name = name # - создание и объявления аргументов нашего класса
        self.surname = surname
        self.patronum = patronum
        self.sex = sex
        self.b_data = b_data


    def fio(self):
        return f'{self.surname} {self.name} {self.patronum}'


class Machine:
    def __init__(self, voltage, model):
        self.voltage = voltage
        self.model = model

class Car(Machine):
    pass

class Teacher(Human, Machine):
    def __init__(self, name, surname, patronum, sex, b_data, salary, plase_work, subject):
        self.salary = salary
        self.plase_work = plase_work
        self.subject = subject
        Human.__init__(self, name, surname, patronum, sex, b_data)


    def fio(self):
        return f'{Human.fio(self)} - {self.subject}'

    # def fio(self):
    #     return Machine.fio(self)

    def __add__(self, other):
        temp_names = ['Вася', 'Петя', 'Саша', 'Маша', 'Света']
        new_human = Human (name=random.choice(temp_names),
                           surname=self.surname,
                           patronum=self.name,
                           sex=random.choice(sexs),
                           b_data='2019-07-09'
                           )
        return new_human
class Student(Human):
    pass


human1 = Teacher('Василий', 'Иванов', 'Алексеевич', 'Муж', '1988-03-09', 12000, 'school 27', 'Mach')
human2 = Human('Ольга', 'Петрова', 'Васильева', 'Жен', '1989-04-12')
print(human1.fio())
print(human2.fio())
human3 = human1 + human2
print(human3)

