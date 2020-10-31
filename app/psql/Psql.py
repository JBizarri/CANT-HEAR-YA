import psycopg2
import psycopg2.extras
from app.config import DATABASE_URL


class Psql:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

            try:
                print("Connecting to PostgreSQL database...")
                connection = Psql._instance.connection = psycopg2.connect(DATABASE_URL)
                Psql._instance.cursor = connection.cursor()
            except Exception as error:
                print(f"Error: connection not established\n{error}")
            
            return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor

    def __del__(self):
        self.cursor.close()
        self.connection.close()            
    
    def execute(self, sql, params=tuple(), fetchall=False):
        try:
            self.cursor.execute(sql, (params,))
        except Exception as error:
            self.connection.rollback()
            print('error execting query "{}", error: {}'.format(sql, error))
            return None
        else:
            if fetchall:
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.statusmessage

    def execute_many(self, sql, params=tuple()):
        try:
            psycopg2.extras.execute_values(self.cursor, sql, params)
        except Exception as error:
            self.connection.rollback()
            print('error execting query "{}", error: {}'.format(sql, error))
            return None
        else:
            self.connection.commit()
            return self.cursor.statusmessage
