import unittest

class Test(unittest.TestCase):

    def test_givenOneBookWhenGettingPriceShouldReturn8(self):

        book = Book()
        self.assertEqual(book.getPrice(), 8)

    def test_givenTwoBooksWhenDifferentAndWhenGettingPriceShouldReturnFifteenPointTwo(self):
        basket = Basket()
        book1 = Book()
        book2 = Book()
        basket.add(book1, 1)
        basket.add(book2, 2)
        self.assertEqual(basket.getPrice(),15.2)

    def test_givenThreeBooksWhenTwoDifferentAndWhenGettingPriceShouldReturnTwentyThreePointTwo(self):
        basket = Basket()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        basket.add(book1, 1)
        basket.add(book2, 1)
        basket.add(book3, 2)
        self.assertEqual(basket.getPrice(), 23.2)

    def test_givenFourBooksWhenTwoSameAndWhenGettingPriceShouldReturnThirtyPointFour(self):
        basket = Basket()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        book4 = Book()
        basket.add(book1,1)
        basket.add(book2,1)
        basket.add(book3,2)
        basket.add(book4,2)
        self.assertEqual(basket.getPrice(), 30.4)

    def test_givenTwoBooksWhenGettingLengthShouldReturnTwo(self):
        basket = Basket()
        book1 = Book()
        book2 = Book()
        basket.add(book1)
        basket.add(book2)
        self.assertEqual(basket.getSize(), 2)

    def test_givenThreeBooksWhenThreeDifferentsWhenGettingPriceShouldReturnTwentyOnePointSix(self):
        basket = Basket()
        book1 = Book()
        book2 = Book()
        book3 = Book()
        basket.add(book1, 1)
        basket.add(book2, 2)
        basket.add(book3, 3)
        self.assertEqual(basket.getPrice(), 21.6)

class Book():
    def __init__(self, type = 1):
        self.price = 8
        self.type = type


    def getPrice(self):
        return 8

class Basket():
    def __init__(self):
        self.price = 0
        self.books = []
        self.count = {}

    def add(self, book, type = 1):
        self.books.append(Book(type))
        if str(type)not in self.count:
            self.count[str(type)] = 0
        self.count[str(type)] += 1

    def getPrice(self):

        while len(self.count.keys()) > 0:
            mini = next(iter(self.count.values()))
            for i in self.count.values():
                if mini > i:
                    mini = i

            if len(self.count.keys()) == 1:
                self.price += mini * 8
            elif len(self.count.keys()) == 2:
                self.price += (mini * 8 * 2) * 0.95
            elif len(self.count.keys()) == 3:
                self.price += (mini * 8 * 3) * 0.90
            elif len(self.count.keys()) == 4:
                self.price += (mini * 8 * 4) * 0.80
            elif len(self.count.keys()) == 5:
                self.price += (mini * 8 * 5) * 0.75

            countcopy = list(self.count.keys())
            for i in countcopy:
                self.count[i] -= mini
                if self.count[i] == 0:
                    self.count.pop(i)

        return self.price

    def getSize(self):
        return len(self.books)
