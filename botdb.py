import sqlite3

class Bd():
    def __init__(self, file='db.db'):
        self.con = sqlite3.connect(file, check_same_thread=False)
        self.cursor = self.con.cursor()


    def find(self, words):
        query = '''SELECT book_name, author, file FROM books'''
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        variants = set()
        for column in columns:
            for row in column:
                if words in row:
                    variants.add((column[0], column[2]))
        return list(variants)


    def give_file(self, words):
        query = '''SELECT file FROM books WHERE book_name == ?'''
        self.cursor.execute(query, (words,))
        columns = self.cursor.fetchall()
        return columns[0][0]


    def picture(self, words):
        query = '''SELECT book_name, author, picture FROM books'''
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        for column in columns:
            for row in column:
                if words in row:
                    return column[2]

    def get_site(self, words):
        query = '''SELECT book_name, site FROM books'''
        self.cursor.execute(query)
        columns = self.cursor.fetchall()
        for column in columns:
            for row in column:
                if words in row:
                    return column[1]

    def close(self):
        self.con.close()

