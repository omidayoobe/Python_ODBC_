import pyodbc

class NwProducts():
    def __init__(self): # thiss class will need the login details
        self.server = 'localhost,1433' # local host = the name of the machine (means here on this matchin) - what the code is saying that python needs to connect the machine on the port 1433
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL server};' + 'SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username +';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def create(self):
        try:
            self.result = my_db.cursor.execute('CREATE Table Students (StudentID int, first_name VARCHAR(255),last_name VARCHAR(255))')
        except:
            print("something went wrong! check your code.")

        finally:
            self.result = my_db.docker_Northwind.commit()
            # close connection
            self.result = my_db.docker_Northwind.commit()

    def insert(self):
        try:
            self.result = my_db.cursor.execute = ("insert into Northwind.dbo.Students (StudentID, first_name, last_name) values (?, ?, ?), 1,'omid','Ayoobe'")
        # sql = ("insert into Northwind.dbo.Students (StudentID, first_name, last_name) values (?, ?, ?)")
        # val = [(1,'omid','Ayoobe'),
        #        (2, 'james', 'tiger')]
        # self.result = my_db.cursor.executemany(sql,val)
        # my_db.cursor.executemany.commit()
        except:
            print("something went wrong! check your code.")

        finally:
            self.result = my_db.docker_Northwind.commit()
            # close connection
            self.result = my_db.docker_Northwind.commit()


    def read_db (self):
        try:
            self.result = my_db.cursor.execute = ('SELECT * FROM Northwind.dbo.Students')

            while True: # while loop - while the loop is true
                column = my_db.cursor.fetchone() # culomn holds the columns and fitches each one at a time - the loop carrys on untile there is no more data left
                if not column: # if there is no more columns to read
                    break # break the loop and leave
                print(column) # otherwise print the columns
        except:

            print("something went wrong! check your code.")
        finally:
            self.result = my_db.docker_Northwind.commit()


my_db = NwProducts()
#my_db.create()
#my_db.insert()
my_db.read_db()



# columns = self.result.fetchall()
#         for column in columns:
#             print(column.(name))