# 🎬 Natural Language to SQL Assistant for Movies Database

## 📌 Project Overview

This project is an AI-powered **Natural Language to SQL Assistant** that enables users to query a movies database using plain English instead of writing SQL manually.

The system uses a local Large Language Model (**Mistral 7B via Ollama**) to translate natural language questions into SQL queries, safely executes them on a SQLite database, and displays the results through an interactive Streamlit interface.

### Example Queries

* “Show top 5 highest-rated movies”
* “Which genre has the highest average rating?”
* “Show movies rated by users from India”
* “List top 5 longest movies with high ratings”

---

# 🚀 Features

## ✅ Natural Language → SQL Conversion

Users can interact with the database using plain English.

## ✅ Local LLM Integration

Uses **Mistral 7B** running locally through **Ollama**.

## ✅ Schema-Aware Query Generation

The system dynamically reads the database schema and provides it to the model to improve SQL accuracy.

## ✅ SQL Injection Protection

The execution layer blocks:

* DROP
* DELETE
* UPDATE
* INSERT
* Multiple SQL statements

Only safe SELECT queries are allowed.

## ✅ Multi-Table Query Support

Supports JOIN operations across:

* movies
* ratings
* users

## ✅ Query History Support

Previous user queries are stored and used as conversational context.

## ✅ Interactive Streamlit UI

Provides a clean web-based interface for querying the database.

---

# 🧠 Technologies Used

| Technology         | Purpose                       |
| ------------------ | ----------------------------- |
| Python             | Core programming language     |
| SQLite             | Relational database           |
| Streamlit          | Web UI                        |
| Ollama             | Local LLM runtime             |
| Mistral 7B         | SQL generation model          |
| Requests           | Communication with Ollama API |
| Prompt Engineering | Improve SQL accuracy          |

---

# 🏗️ System Architecture

```text
User
  ↓
Streamlit UI (app.py)
  ↓
Natural Language Query
  ↓
Mistral 7B via Ollama (nl_to_sql.py)
  ↓
Generated SQL Query
  ↓
Execution Layer (execute_query.py)
  ↓
SQLite Database
  ↓
Results
  ↓
Streamlit UI
```

---

# 📂 Project Structure

```text
movie-nl-sql-assistant/
│
├── app.py                  # Streamlit UI
├── main.py                 # CLI version
├── nl_to_sql.py            # LLM prompt + SQL generation
├── execute_query.py        # SQL validation + execution
├── formatter.py            # Result formatting
├── setup_db.py             # Database schema creation
├── insert_data.py          # Sample dataset insertion
├── movies.db               # SQLite database
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

# 🗄️ Database Schema

## movies

| Column       | Type    |
| ------------ | ------- |
| movie_id     | INTEGER |
| title        | TEXT    |
| release_year | INTEGER |
| genre        | TEXT    |
| duration     | INTEGER |

## ratings

| Column    | Type    |
| --------- | ------- |
| rating_id | INTEGER |
| movie_id  | INTEGER |
| user_id   | INTEGER |
| rating    | REAL    |
| timestamp | TEXT    |

## users

| Column   | Type    |
| -------- | ------- |
| user_id  | INTEGER |
| name     | TEXT    |
| location | TEXT    |

---

# 🔗 Table Relationships

```text
movies.movie_id ← ratings.movie_id
users.user_id ← ratings.user_id
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/movie-nl-sql-assistant.git
cd movie-nl-sql-assistant
```

---

## 2️⃣ Install Dependencies

```bash
pip install streamlit requests
```

---

## 3️⃣ Install Ollama

Download and install Ollama from the official website.

---

## 4️⃣ Download Mistral Model

```bash
ollama run mistral
```

The model will be downloaded locally.

---

## 5️⃣ Run the Application

### Start Ollama

```bash
ollama run mistral
```

### Start Streamlit App

Open another terminal and run:

```bash
streamlit run app.py
```

---

# 🧪 Example Queries

## Basic Queries

```text
Show all movies
List all Drama movies
Show movies released after 2015
```

## Aggregation Queries

```text
Which genre has the highest average rating?
What is the lowest rated movie?
Show average rating for each genre
```

## JOIN Queries

```text
Show movies rated by users from India
List users and the movies they rated
Show ratings along with movie titles
```

## Advanced Queries

```text
Show top 5 highest rated movies
Which movie is liked by most users?
List top 5 longest movies with high ratings
```

---

# 🔒 SQL Injection Protection

The system validates generated SQL before execution.

### Protection Mechanisms

* Allows only SELECT queries
* Blocks dangerous SQL keywords
* Prevents multiple SQL statements
* Cleans common LLM-generated SQL mistakes

### Blocked Examples

```text
DROP TABLE movies
DELETE FROM users
SHOW movies; DROP TABLE movies;
```

---

# 🧠 Challenges Faced

## 1. LLM Hallucination

Smaller models occasionally generated incorrect joins or non-existent columns.

### Solution

* Added schema awareness
* Improved prompt engineering
* Added SQL validation layer

---

## 2. Ambiguous SQL Queries

Queries such as:

```text
movie_id
```

caused ambiguity during JOIN operations.

### Solution

Used fully qualified column names such as:

```sql
movies.movie_id
```

---

## 3. Aggregate Function Errors

The model sometimes used:

```sql
WHERE AVG(...)
```

instead of:

```sql
HAVING AVG(...)
```

### Solution

Added prompt constraints and query-cleaning logic.

---

# 🎯 Future Improvements

* PostgreSQL support
* Better conversational memory
* Query explanation feature
* Fine-tuned SQL-specific LLM
* Authentication system
* Export query results to CSV

---

# 📸 Demo Suggestions

Recommended demo queries:

```text
Which genre has the highest average rating?
Show movies rated by users from India
Show top 5 highest rated movies
Which movie is liked by most users?
```



This project demonstrates how Large Language Models can be integrated with relational databases to create intelligent and user-friendly database interfaces. By combining prompt engineering, schema awareness, SQL safe
