from os import stat

import psycopg2
from app.config import DATABASE_URL


class Psql:
    @staticmethod
    def _connect_to_db():
        return psycopg2.connect(DATABASE_URL, sslmode="required")

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
