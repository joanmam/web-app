import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my first App")
st.write("This app is for fun")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.popup(index)
        functions,wrtie_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input("", placeholder="Add a new todo...",
              on_change=add_todo, key="new_todo")