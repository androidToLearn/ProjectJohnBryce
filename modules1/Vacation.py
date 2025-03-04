
class Vacation:
    def __init__(self, id: int, id_country: int, description: str, date_start: str, date_end: str, price: int, image_name: str):
        self.id = id
        self.id_country = id_country
        self.description = description
        self.date_start = date_start
        self.date_end = date_end
        self.price = price
        self.image_name = image_name

    def __init__(self):
        self.id = -1
        self.id_country = -1
        self.description = ''
        self.date_start = ''
        self.date_end = ''
        self.price = -1
        self.image_name = ''
