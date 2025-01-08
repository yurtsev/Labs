class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(F'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}')


ZZZaVVVodnoy_apelsin = Book('Заводной апельсин', 'Энтони Бёрджесс', '1962')
Metro2034 = Book('Метро 2034', 'Дмитрий Глуховский', '2009')
when_idet_snow = Book('Когда идет снег', 'Макс Максимов', '2017')
f451gradus_po_farengeitu = Book('451 градус по фаренгейту', 'Рэй Брэдбери', '1953')
library = [ZZZaVVVodnoy_apelsin, Metro2034, when_idet_snow, f451gradus_po_farengeitu]
for i in library:
    i.get_info()

# -----------task-2----------
print('-----------task-2----------')


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


circle_big = Circle(5, 10, 25)

print(circle_big.get_radius())
newR = input('задайте новый радиус')
circle_big.set_radius(newR)
print(circle_big.get_radius())
