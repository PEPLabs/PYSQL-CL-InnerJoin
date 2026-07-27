import os
import sqlite3

"""
SQL sublanguage: DQL (Data Query Language)

INNER JOIN is when we query two or more tables on some criteria, and only see results where there are matching
rows in all tables.

Example: SELECT * FROM table_left INNER JOIN table_right
ON table_left.column1 = table_right.column3;
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def problem1():
    """
    Consider the following tables:

                 class                                  student
    | id |  teacher_name |class_title|     | id |      student_name |class_title|
    ----------------------------------     --------------------------------------
    |1   |'Ms. Lovelace' |'Physics'  |     |1   |'John Stewart'     |'Writing'  |
    |2   |'Ms. Lovelace' |'Math'     |     |2   |'Stephen Colbert'  |'Physics'  |
    |3   |'Mr. McCarthy' |'Writing'  |     |3   |'Samantha Bee'     |'Math'     |
    |4   |'Ms. Goodall'  |'Biology'  |     |4   |'Aasif Mandvi'     |'Writing'  |
                                           |5   |'Robert Riggle'    |'Physics'  |
                                           |6   |'Jessica Williams' |'Art'      |

    Problem 1: Write a query that will return the id, and name of each of Ms. Lovelace's students, using an
    INNER JOIN combined with a WHERE clause on the teacher name.

    Returns a set of (id, student_name) tuples.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE class ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "teacher_name VARCHAR(255),"
        "class_title VARCHAR(255)"
        ");"
    )
    cur.execute(
        "INSERT INTO class (teacher_name, class_title) VALUES "
        "('Ms. Lovelace', 'Physics'),"
        "('Ms. Lovelace', 'Math'),"
        "('Mr. McCarthy', 'Writing'),"
        "('Ms. Goodall', 'Biology');"
    )

    cur.execute(
        "CREATE TABLE student ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "student_name VARCHAR(255),"
        "class_title VARCHAR(255)"
        ");"
    )
    cur.execute(
        "INSERT INTO student (student_name, class_title) VALUES "
        "('John Stewart', 'Writing'),"
        "('Stephen Colbert', 'Physics'),"
        "('Samantha Bee', 'Math'),"
        "('Aasif Mandvi', 'Writing'),"
        "('Robert Riggle', 'Physics'),"
        "('Jessica Williams', 'Art');"
    )
    conn.commit()

    results = set()
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            results.add((row[0], row[1]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return results
