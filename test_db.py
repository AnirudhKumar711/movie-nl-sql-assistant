import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

query = """
SELECT title, rating
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
ORDER BY rating DESC;
"""

cursor.execute(query)

results = cursor.fetchall()

for row in results:
    print(row)

conn.close()