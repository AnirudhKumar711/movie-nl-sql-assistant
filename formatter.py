def format_response(question, columns, results):
    if not results:
        return "No results found."

    if "highest average rating" in question.lower():
        genre, rating = results[0]
        return f"The genre with the highest average rating is {genre} with {round(rating,2)} stars."

    col_widths = []
    for i in range(len(columns)):
        max_len = len(columns[i])
        for row in results:
            max_len = max(max_len, len(str(row[i])))
        col_widths.append(max_len + 2)

    header = ""
    for i, col in enumerate(columns):
        header += col.upper().ljust(col_widths[i])

    separator = "-" * len(header)

    rows = ""
    for row in results:
        line = ""
        for i, val in enumerate(row):
            line += str(val).ljust(col_widths[i])
        rows += line + "\n"

    table = "\n" + header + "\n" + separator + "\n" + rows

    return table