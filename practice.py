import streamlit as st

st.title("Business Dashboard with Streamlit Layouts")

msg  = "## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
st.write(msg)

col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
