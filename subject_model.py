import mysql.connector

DATABASE = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_databasename'
}

class Subject:
    TABLE_NAME = "Subjects"

    def __init__(self, id=None, name=None, duration=None):
        self.id = id
        self.name = name
        self.duration = duration

    @staticmethod
    def connect():
        return mysql.connector.connect(**DATABASE)

    @staticmethod
    def read(id=None):
        with Subject.connect() as connection:
            cursor = connection.cursor()
            if id:
                query = f"SELECT id, name, duration FROM {Subject.TABLE_NAME} WHERE id=%s"
                cursor.execute(query, (id,))
                result = cursor.fetchone()
                if result:
                    subject = Subject(name=result[1], duration=result[2])
                    subject.id = result[0]
                    return subject
                else:
                    return None
            else:
                query = f"SELECT id, name, duration FROM {Subject.TABLE_NAME}"
                cursor.execute(query)
                results = cursor.fetchall()
                subjects = []
                for result in results:
                    subject = Subject(name=result[1], duration=result[2])
                    subject.id = result[0]
                    subjects.append(subject)
                return subjects
    
    def create(self):
        query = f"INSERT INTO {self.TABLE_NAME} (name, duration) VALUES (%s, %s)"
        values = (self.name, self.duration)
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, values)
            self.id = cursor.lastrowid

    def update(self):
        query = f"UPDATE {self.TABLE_NAME} SET name=%s, duration=%s WHERE id=%s"
        values = (self.name, self.duration, self.id)
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, values)

    def delete(self):
        query = f"DELETE FROM {self.TABLE_NAME} WHERE id=%s"
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute(query, (self.id,))
