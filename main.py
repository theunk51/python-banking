import sqlite3
connection = sqlite3.connect('jp.db')
# :memory: cretaes a database RAM

c = connection.cursor()

# create table
c.execute('''CREATE TABLE account
                (accountNumber, name, balance)''')

c.execute("INSERT INTO account VALUES('A0', 'Alin Chambers', '50.65')")

# save (commit) changes
connection.commit()

connection.close()


