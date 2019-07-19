# # Задача-1:
# # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# # из которой запущен данный скрипт.
# # И второй скрипт, удаляющий эти папки.
#
import os
if __name__ == '__main__':
    pass

def mk_dir(__name__): # - создание функции добавления папок
    try:
        os.mkdir(str(__name__))
        print('{} - создана'.format(__name__))
    except FileExistsError:
        print('{} - уже существует'.format(__name__))

def rm_dir(__name__): # - создание функции удаления папок
    try:
        os.rmdir(__name__)
        print(__name__, ' - удален')
    except FileNotFoundError:
        print('{} - папки не существует'.format(__name__))



if __name__ == '__main__':
    start()


