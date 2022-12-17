import json


class Listing:
    title = ''
    href = ''
    link = ''
    price = ''
    price_per_square = ''
    size = ''

    base_url = 'https://www.otodom.pl'

    def __init__(self, partial):
        self.title = partial.get('title')
        self.link = f"{self.base_url}{partial.get('href')}"
        self.href = partial.get('href')
        self.price = partial.get('price')
        self.price_per_square = partial.get('price_per_square')
        self.size = partial.get('size')

    def __str__(self) -> str:
        data = {
            'title': self.title,
            'href': self.href,
            'price': self.price,
            'price_per_square': self.price_per_square,
            'size': self.size
        }

        return json.dumps(data)

    def get_message(self) -> str:
        message = '\n --------------------------'
        message = message + f"\n Tytul: {self.title}"
        message = message + \
            f"\n Cena: {self.price} / Powierzchnia: {self.size}"
        message = message + f"\n \n Link: {self.link}"
        message = message + '\n \n --------------------------'

        return str(message)
