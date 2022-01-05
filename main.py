import sqlite3
from DataBase.DealPrimeData import DealPrimeData

class FindPrime:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.dealPrimeData = DealPrimeData()
        self.dealPrimeData.createDataTable()

    def findPrime(self):
        for i in range(self.a, self.b +1):
            if self.dealPrimeData.primeIf(i) :
                try:
                    self.dealPrimeData.insertPrimeData(i)
                except sqlite3.IntegrityError:
                    pass



F1 = FindPrime(2, 100000)
F1.findPrime()


