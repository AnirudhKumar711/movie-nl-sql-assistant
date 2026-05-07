from nl_to_sql import generate_sql
from execute_query import run_query
from formatter import format_response

def main():
    print("🎬 Movie SQL Assistant (type 'exit' to quit)\n")

    while True:
        question = input("Ask your question: ")

        if question.lower() == "exit":
            break

        # Generate SQL
        sql_query = generate_sql(question)
        print("\nGenerated SQL:\n", sql_query)

        # Execute query
        columns, results = run_query(sql_query)

        # Format output
        if columns:
            answer = format_response(question, columns, results)
        else:
            answer = f"Error: {results}"

        print("\nAnswer:\n", answer)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()