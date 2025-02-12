import streamlit as st
import snowflake.connector

def connect_to_snowflake(user, password, account, warehouse, database, schema):
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema
    )
    return conn

st.title("Snowflake Geospatial Capabilities")

st.sidebar.header("Snowflake Credentials")
user = st.sidebar.text_input("User")
password = st.sidebar.text_input("Password", type="password")
account = st.sidebar.text_input("Account")
warehouse = st.sidebar.text_input("Warehouse")
database = st.sidebar.text_input("Database")
schema = st.sidebar.text_input("Schema")

if st.sidebar.button("Connect"):
    conn = connect_to_snowflake(user, password, account, warehouse, database, schema)
    st.sidebar.success("Connected to Snowflake")

st.header("Geospatial Capabilities")
st.write("Explore Snowflake's Geospatial capabilities here.")
