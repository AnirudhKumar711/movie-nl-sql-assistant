import requests
import sqlite3

def get_schema():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = ""
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        cols = cursor.fetchall()
        col_names = [col[1] for col in cols]
        schema += f"{table_name}({', '.join(col_names)})\n"

    conn.close()
    return schema


def extract_sql(response):
    # Keep only first SQL statement
    if ";" in response:
        response = response.split(";")[0] + ";"

    return response.strip()


def generate_sql(question, history=None):
    schema = get_schema()

    context = ""
    if history:
        context = "\nPrevious Queries:\n" + "\n".join(history[-3:])

    prompt = f"""
You are an expert SQL generator.

Database schema:
{schema}

IMPORTANT RULES:
- Only use columns that exist
- Do NOT invent columns
- movies table does NOT have user_id
- Use JOIN only when necessary
- users connect via ratings table
- Use HAVING for aggregates
- Output ONLY SQL

Examples:

Q: List all Drama movies
SQL:
SELECT movies.movie_id, movies.title, movies.release_year, movies.genre, movies.duration
FROM movies
WHERE movies.genre = 'Drama';

Q: Which genre has the highest average rating?
SQL:
SELECT movies.genre, AVG(ratings.rating) as avg_rating
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
GROUP BY movies.genre
ORDER BY avg_rating DESC
LIMIT 1;

Q: Show movies with average rating above 4.5
SQL:
SELECT movies.movie_id, movies.title, AVG(ratings.rating) as avg_rating
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
GROUP BY movies.movie_id, movies.title
HAVING AVG(ratings.rating) > 4.5;

{context}

User Question:
{question}

SQL:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()["response"]
    sql = extract_sql(result)

    # Fix small mistake if needed
    if "SELECT movie_id" in sql:
        sql = sql.replace("SELECT movie_id", "SELECT movies.movie_id")

    return sql