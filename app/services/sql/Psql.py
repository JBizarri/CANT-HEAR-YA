from os import stat

import psycopg2
from app.config import (DATABASE, DATABASE_PASS, DATABASE_PORT, DATABASE_URL,
                        DATABASE_USER)


class Psql:
    @staticmethod
    def _connect_to_db():
        conn = psycopg2.connect(
            user=DATABASE_USER,
            password=DATABASE_PASS,
            host=DATABASE_URL,
            port=DATABASE_PORT,
            database=DATABASE,
        )
        return conn

    def execute_query(self, query, params=tuple()):
        conn = self._connect_to_db()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
        except Exception:
            conn.rollback()
        else:
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def fetchall(self, query, params=tuple()):
        conn = self._connect_to_db()
        cursor = conn.cursor()

        result = None
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

        return result
