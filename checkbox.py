import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os
load_dotenv(r"C:\Users\Madhura\ai_env\.env",encoding="utf-16")

url = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
key = os.getenv("NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY")
supabase: Client = create_client(url,key)


def get_todos():
    response = supabase.table('todos').select('*').execute()
    return response.data

def add_todo(task):
    supabase.table('todos').insert({"task":task}).execute()

st.header('Tasks to do')

plus = st.button(" Add Task")
task = st.text_input("Add a new task: ")
if plus:
    if task:
        add_todo(task)
        st.success("Added!")
        
    else:
        st.error("Please enter a task")

todos = get_todos()
if todos:
    for todo in todos:
        st.write(f"-{todo['task']}")

else:
    st.write("No tasks available")


#