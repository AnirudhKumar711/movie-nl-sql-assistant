import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# ---------------- MOVIES ----------------
movies_data = [
    (1, "Inception", 2010, "Sci-Fi", 148),
    (2, "Interstellar", 2014, "Sci-Fi", 169),
    (3, "The Dark Knight", 2008, "Action", 152),
    (4, "Avengers: Endgame", 2019, "Action", 181),
    (5, "Parasite", 2019, "Thriller", 132),
    (6, "Titanic", 1997, "Romance", 195),
    (7, "The Matrix", 1999, "Sci-Fi", 136),
    (8, "Gladiator", 2000, "Action", 155),
    (9, "Joker", 2019, "Drama", 122),
    (10, "Toy Story", 1995, "Animation", 81),
    (11, "Frozen", 2013, "Animation", 102),
    (12, "The Godfather", 1972, "Crime", 175),
    (13, "Pulp Fiction", 1994, "Crime", 154),
    (14, "Forrest Gump", 1994, "Drama", 142),
    (15, "The Shawshank Redemption", 1994, "Drama", 142),
    (16, "Avengers: Infinity War", 2018, "Action", 149),
    (17, "Spider-Man: No Way Home", 2021, "Action", 148),
    (18, "Dune", 2021, "Sci-Fi", 155),
    (19, "Oppenheimer", 2023, "Drama", 180),
    (20, "Barbie", 2023, "Comedy", 114)
]

# ---------------- USERS ----------------
users_data = [
    (1, "Alice", "USA"),
    (2, "Bob", "UK"),
    (3, "Charlie", "India"),
    (4, "David", "Canada"),
    (5, "Emma", "Australia"),
    (6, "Frank", "Germany"),
    (7, "Grace", "France"),
    (8, "Hannah", "Japan"),
    (9, "Ivan", "Russia"),
    (10, "Jack", "Brazil")
]

# ---------------- RATINGS ----------------
ratings_data = [
    (1, 1, 1, 4.8, "2024-01-01"),
    (2, 2, 2, 4.7, "2024-01-02"),
    (3, 3, 3, 4.9, "2024-01-03"),
    (4, 4, 1, 4.6, "2024-01-04"),
    (5, 5, 2, 4.5, "2024-01-05"),
    (6, 6, 3, 4.3, "2024-01-06"),
    (7, 7, 4, 4.7, "2024-01-07"),
    (8, 8, 5, 4.6, "2024-01-08"),
    (9, 9, 6, 4.4, "2024-01-09"),
    (10, 10, 7, 4.2, "2024-01-10"),
    (11, 11, 8, 4.3, "2024-01-11"),
    (12, 12, 9, 5.0, "2024-01-12"),
    (13, 13, 10, 4.9, "2024-01-13"),
    (14, 14, 1, 4.8, "2024-01-14"),
    (15, 15, 2, 5.0, "2024-01-15"),
    (16, 16, 3, 4.7, "2024-01-16"),
    (17, 17, 4, 4.6, "2024-01-17"),
    (18, 18, 5, 4.5, "2024-01-18"),
    (19, 19, 6, 4.8, "2024-01-19"),
    (20, 20, 7, 4.1, "2024-01-20"),
    (21, 1, 8, 4.9, "2024-01-21"),
    (22, 2, 9, 4.8, "2024-01-22"),
    (23, 3, 10, 5.0, "2024-01-23"),
    (24, 4, 2, 4.7, "2024-01-24"),
    (25, 5, 3, 4.6, "2024-01-25"),
    (26, 6, 4, 4.4, "2024-01-26"),
    (27, 7, 5, 4.8, "2024-01-27"),
    (28, 8, 6, 4.7, "2024-01-28"),
    (29, 9, 7, 4.5, "2024-01-29"),
    (30, 10, 8, 4.3, "2024-01-30")
]

# ---------------- INSERT ----------------
cursor.executemany("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", movies_data)
cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", users_data)
cursor.executemany("INSERT INTO ratings VALUES (?, ?, ?, ?, ?)", ratings_data)

conn.commit()
conn.close()

print("Extended dataset inserted successfully!")