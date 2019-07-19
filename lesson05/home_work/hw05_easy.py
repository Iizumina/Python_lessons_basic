# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
if __name__ == '__main__':
    pass

def mk_dir(__name__): # - создание функции добавления папок
    dirNamber = range(1, 10)
    try:
        for i in dirNamber:
            j = str(i)
            os.mkdir('dir_'+j)
            print('dir_{} - создана'.format(i))
    except FileExistsError:
        for i in dirNamber:
            print('dir_{} - уже существует'.format(i))

def rm_dir(__name__): # - создание функции удаления папок
    try:
        os.rmdir(__name__)
        print(__name__, ' - удален')
    except FileNotFoundError:
        print('{} - папки не существует'.format(__name__))

def start():
    answer = '_'
    dirNamber = range(1, 10)

    while True:
        answer = input('*' * 30 + ' \n'
                       'Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Cодержимое папки\n')

        if answer == '1':
            mk_dir(__name__.format())
        elif answer == '2':
            for i in dirNamber:
                rm_dir('dir_{}'.format(i))
        elif answer == '3':
            content = os.listdir()
            for n in content:
                print(n)

if __name__ == '__main__':
    start()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os

content = os.listdir()
for n in content:
    print(n)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    pass

import shutil
import os

def copyFile ():
    name_file = os.path.realpath(__file__) # - возвращает канонический путь, убирая все символические ссылки (если они поддерживаются).

    new_file = name_file[:-3] +'_copy.py'

    if os.path.isfile(new_file) != True: # - является ли путь файлом
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Файл уже скопирован'

if __name__ == '__main__':
    print(copyFile())