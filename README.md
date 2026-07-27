# Background

SQL sublanguage: DQL (Data Query Language)

INNER JOIN lets us query two or more tables on some criteria, and only see results where there are matching rows
in all tables.

SELECT * FROM table_left INNER JOIN table_right
ON table_left.column1 = table_right.column3
WHERE table_left.column1 = value;

## Problem 1

Assume the following tables already exist.

class

| id | teacher_name | class_title |
|----|--------------|-------------|
| 1 | Ms. Lovelace | Physics |
| 2 | Ms. Lovelace | Math |
| 3 | Mr. McCarthy | Writing |
| 4 | Ms. Goodall | Biology |

student

| id | student_name | class_title |
|----|--------------|-------------|
| 1 | John Stewart | Writing |
| 2 | Stephen Colbert | Physics |
| 3 | Samantha Bee | Math |
| 4 | Aasif Mandvi | Writing |
| 5 | Robert Riggle | Physics |
| 6 | Jessica Williams | Art |

Write a query in `problem1.sql` that will return the id and name of each of Ms. Lovelace's students, using an
INNER JOIN combined with a WHERE clause on the teacher name. Do not use a wildcard (`*`) - specify
`table.column` for each selected column, since the column names may be ambiguous between `class` and `student`.
