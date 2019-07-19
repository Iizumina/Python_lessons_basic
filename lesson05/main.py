# import my_module
# temp.test()

# import my_module
# print(my_module.a) # Вывод значения а из файла my_module.py
# a = 12 # присвоение а = 12
# print(a) # Вывод значения а из текущего файла

# from my_module import * # -  * - просит импортировать все из файла my_module
# print(a) # - для вывода значения теперь не надо бует обращаться к тому файлу
# a = 12
# print(a)
#
# from my_module import test # - лучше обращаться к названию функции модуля, а не к переменной
# # from my_module import test, a # для удобства можно перечислить через запятую то, что нужно импортировать,
# # чтобы не дублировать переменные
# a = 12
# print(test()) # - просим вывести не значение а, а результат работы функции из импорта

# import my_module # - загрузка моего модуля (вирт. окружение)
# import importlib # - загрузка модуля загрузки
# importlib.reload(my_module) # - возвра т модуля к исходной загрузке

# import my_module # - загрузка моего модуля (вирт. окружение)
# def test(): # - обращение к внутренней функции файла
#     return True
# my_module.test() # - обращение к функции импортируемого файла

# import math # - в приоритетет импортируется библиотека окружения, а не стандартная
# math.test() # - поэтому важно не использовать имена стандартных библиотечных модулей

# import math # - импорт стандартой библиотеки и использования функции
# print(math.sqrt(4))

# from math import sqrt # - импорт функции квадратного корня из стандартной библиотеки math.import
# # - если из всей библиотеки нужна только 1 функция, то можно обратиться к ней таким способом

# from my_module_lib.funcs import func # - импортировать из библиотеки модулей созданной нами функцию func
#
# import my_module_lib # - обращается к модулю my_module_lib к стандартному файлу __init.py__
# # - чобы делать импорты самих библиотек, необходимо импортировать их в файл __init.py__
#
# my_module_lib.func() # - подгружаем импортированную функцию из библиотеки __innit.py__

# import sys # - отвечает за системные характеристики устройства
# print(sys.path) # - папки окружения в котором будут искаться наши модули

# import os # - c помощью модуля OS можно создавать и удалять файлы/папки.
# # print(os.name) # - имя операционной системы nt - Windows, posix - iOS
# print("PATH", os.getcwd()) # - путь папки откуда была запущена данная программа

# import sys
# for arg in sys.argv:
#     print(arg)

# import sys
# args = sys.argv
# print(type(args)) # - хочу увидеть тип переменной
# print('#'*10) # - вывести 10 звездочек
# for arg in args: # -напечатать те документы которые введены
#     print(arg)
#
# # (env) E:\Python\Python_lessons_basic\lesson05\env>python main.py hello right
# # # <class 'list'>
# # # ##########
# # # main.py
# # # hello
# # # right


# import sys
# args = sys.argv
# def menu():
#     print('Hello')
#     result = input('Whats you name?\n')
#     return result
# if __name__ == '__main__':
#     args = sys.argv
#     if len(args) > 1:
#         print(f'Nice to meet you {args[1]}')
#     else:
#         name = menu()
#         print(f'Nice to meet you {name}')
# #
# # (env) E:\Python\Python_lessons_basic\lesson05\env>python main.py Masha
# # Nice to meet you Masha
# #
# # (env) E:\Python\Python_lessons_basic\lesson05\env>python main.py
# # Hello
# # Whats you name?
#  pip install requests(командная строка)

# import requests
# page = requests.get('https://geekbrains.ru')
# # print(page) # - возвращает код ответа от сервера: <Response [200]> гиперссылка
# # print(page.headers) # - заголовки ответа сервера в виде словаря
#
# print(page.text) # - текст страницы
# with open('page.html', 'w', encoding='UTF-8') as file:
#     file.write(page.text)

# import requests
# import json
# temp_dict = {'name': 'Sergey', 'auth':True}
# j_temp = json.dumps(temp_dict)
#
# with open ('test.json', 'w') as file:
#     file.write(j_temp)

# import requests
# import json
#
# with open('test.json', 'r') as file:
#    temp_r = file.read()
# print(type(temp_r))
# print(temp_r)
#
# j_temp = json.load(temp_r) # - перевод с словарь
# print(type(j_temp))


# import requests
# import json
#
# t_github = requests.get('https://api.github.com')
# # print(t_github.text)
# print(t_github.json()['current_user_url']) # - просим вывести ссылку объекта

# import requests
# import json
#
# t_github = requests.get('https://api.github.com').json()
# for key, value in t_github.items(): # - получение объекта из сети
#     # print(key)
#     # print(value)
#     print(f'{key}-----{value}')


# import requests
# import json #  - для общения с онлайн сервисами
#
# t_weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Moscow').json() # - params - словарь куда передаетс параметры и то что идет после знака ?
# # t_weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params={'q':'Moscow'}).json()
# for key, value in t_weather.items(): # - получение объекта из сети
#     print(f'{key}-----{value}')

import requests
import json

# t_weather = requests.get('https://gismeteo.ru/api').json()
# for key, value in t_weather.items(): # - получение объекта из сети
#     print(f'{key}-----{value}')
import os
for i in dir(os):
    print(i)
