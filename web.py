import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    local_todo = st.session_state["new_todo"] +"\n"
    todos.append(local_todo)
    functions.write_todos(todos)


st.session_state["new_todo"] = ""
todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my todo app test test")
st.write("This app is a simple test")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a To Do Item", placeholder="Enter new todo...",
              on_change=add_todo, key="new_todo")

# print("hello test")
# st.session_state
