import os
from flask import Flask
import mysql.connector


class DBManager:
    """
    A class to manage the connection to the MySQL database.
    """
    def __init__(self, database='example', host="db", user="root", password_file=None):
        """
        Initializes the DBManager and connects to the database.

        Args:
            database (str, optional): The name of the database. Defaults to 'example'.
            host (str, optional): The hostname of the database server. Defaults to "db".
            user (str, optional): The username to connect to the database. Defaults to "root".
            password_file (str, optional): The path to the file containing the password. Defaults to None.
        """
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user, 
            password=pf.read(),
            host=host, # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        """
        Populates the database with some sample data.
        It drops the 'blog' table if it exists, creates a new 'blog' table,
        and inserts some sample blog posts.
        """
        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255))')
        self.cursor.executemany('INSERT INTO blog (id, title) VALUES (%s, %s);', [(i, 'Blog post #%d'% i) for i in range (1,5)])
        self.connection.commit()
    
    def query_titles(self):
        """
        Queries the database for all blog post titles.

        Returns:
            A list of blog post titles.
        """
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec


server = Flask(__name__)
conn = None

@server.route('/')
def listBlog():
    """
    A Flask route that connects to the database, populates it if necessary,
    queries for blog post titles, and returns them as an HTML response.

    Returns:
        An HTML string containing the blog post titles.
    """
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
        conn.populate_db()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   Hello  ' + c + '</div>'
    return response


if __name__ == '__main__':
    server.run()
