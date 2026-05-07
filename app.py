import streamlit as st
from nl_to_sql import generate_sql
from execute_query import run_query

st.title("🎬 Movie NL → SQL Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question:")

if query:
    st.session_state.history.append(query)

    sql = generate_sql(query, st.session_state.history)

    st.subheader("Generated SQL")
    st.code(sql, language="sql")

    cols, res = run_query(sql)

    if cols:
        st.subheader("Results")
        st.dataframe(res)
    else:
        st.error(res)