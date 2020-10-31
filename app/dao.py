from app.psql.Psql import Psql


def fetch_comments(psql: Psql):
    sql = "SELECT * FROM comments"

    return psql.execute(sql, fetchall=True)


def fetch_responses(psql: Psql):
    sql = "SELECT * FROM responses"

    return psql.execute(sql, fetchall=True)


def fetch_vocatives(psql: Psql):
    sql = "SELECT * FROM vocatives"

    return psql.execute(sql, fetchall=True)


def insert_comments(psql: Psql, comments: list):
    sql = "INSERT INTO comments VALUES %s"

    return psql.execute_many(sql, params=comments)


def delete_old_comments(psql: Psql, comments: tuple):
    sql = "DELETE FROM comments WHERE comment NOT IN %s"

    return psql.execute(sql, params=comments)
