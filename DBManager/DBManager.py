import psycopg2
import os


class DBManager:

    def __init__(self):
        self.connection = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'))
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE  IF NOT EXISTS flats (title varchar(255),"
                            "image varchar(255));")
        self.connection.commit()

    def insert_flat(self, flat):
        self.cursor.execute("INSERT INTO flats "
                            "(title, image) "
                            "VALUES (%s, %s);", (flat['title'], flat['image_url']))
        self.connection.commit()

    def get_flats(self):
        self.cursor.execute("SELECT * FROM flats;")
        rows = self.cursor.fetchall()
        return rows

    def close(self):
        self.cursor.close()
        self.connection.close()
