import requests

api_url = 'https://5ka.ru/api/v2/special_offers/?records_per_page=12&page=1'


class Collection:
    products = []
    next = None
    previous = None

    def __init__(self, url):

        while True:
            if self.next:
                data = self.get_next_data(self.next)
            else:
                data = self.get_next_data(url)

            for item in data.get('results'):
                self.products.append(Product(item))

            for key, value in data.items():
                setattr(self, key, value)

            if not data['next']:
                break

    def get_next_data(self, url):
        return requests.get(url).json()
class Product:
    def __init__(self, product_dict):
        for key, value in product_dict.items():
            setattr(self, key, value)


class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print('ДАЙ мне ', item)

        return getattr(self.wrapped, item)

class NotExintError(Exception):
    def __init__(self, item):
        self.item = item
        Exception.__init__(self)
    def __str__(self):
        return f'NotExintError: в списке {self.item}, нет выхода'
def cheak(item):
    if 'Exit' not in tmp:
        raise NotExintError
if __name__ == '__main__':
    # market = Collection(api_url)
    # print(1111)
    tmp = [1, 2, 3, 4, 5, 'Exit']

    try:
        cheak(tmp)
    except NotExintError as e:
        print(e)
    else:
        print('Все отлично')