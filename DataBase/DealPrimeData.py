import sqlite3
import math
import cmath


class DealPrimeData:

    def __init__(self):
        self.conn = sqlite3.connect("prime.db")
        self.cursor = self.conn.cursor()

    def __upCheckNumber(self, x):
        limit = math.trunc(cmath.sqrt(x).real)
        upNumber = x
        downNumber = 0
        try:
            while (upNumber - downNumber) > 1:
                if limit <= self.retrievePrimeData((upNumber+downNumber) // 2):
                    upNumber = (upNumber+downNumber) // 2
                else:
                    downNumber = (upNumber+downNumber) // 2
        except:
            pass
        return upNumber

    def createDataTable(self):
        create_table_sql = '''
                create table if not exists primeTable(
                id integer not null primary key autoincrement,
                prime integer not null unique
                )
            '''
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insertPrimeData(self, x):
        insert_sql = '''
            insert into primeTable(prime)
            values(%d)
            ''' % x
        self.cursor.execute(insert_sql)
        self.conn.commit()

    def retrievePrimeData(self, x):
        select_sql = "select prime from primeTable where id = %d" % x
        self.cursor.execute(select_sql)
        result = self.cursor.fetchone()[0]
        return result

    def primeIf(self, x):
        check = True
        if x != 2:
            if x % 2 != 0:
                upcheckNumber = self.__upCheckNumber(x)
                for i in range(1, upcheckNumber+1):
                    try:
                        if x % self.retrievePrimeData(i) == 0:
                            check = False
                            break
                    except:
                        break
            else:
                check = False
        return check
