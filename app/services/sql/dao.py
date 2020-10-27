from app.services.sql.Psql import Psql


def fetchall_comments():
    sql = "SELECT * FROM comments"
    comments = Psql().fetchall(sql)

    if not comments:
        return list()

    return [comment[0] for comment in comments]


def insert_comment(comment):
    sql = "INSERT INTO comments (comment) VALUES(%s)"

    Psql().execute_query(sql, params=(comment,))
