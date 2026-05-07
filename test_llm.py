from nl_to_sql import generate_sql

question = "Which genre has the highest average rating?"

sql_query = generate_sql(question)

print("Generated SQL:\n")
print(sql_query)