from project import view_todos, add_todo, mark_todo_as_done
import sys
from io import StringIO


def test_view_todos(capsys):
    todo_list = [
        {"task": "Task 1", "done": False},
        {"task": "Task 2", "done": True},
    ]
    view_todos(todo_list)
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected_output = "Todo List:\n1. [ ] Task 1\n2. [X] Task 2"
    assert output == expected_output



def test_mark_todo_as_done():
    todo_list = [
        {"task": "Task 1", "done": False},
        {"task": "Task 2", "done": False},
    ]
    mark_todo_as_done(todo_list, 1)
    assert todo_list[0]["done"]
    assert not todo_list[1]["done"]

    mark_todo_as_done(todo_list, 2)
    assert todo_list[1]["done"]


def test_add_todo():
    todo_list = []
    add_todo(todo_list, "Task 1")
    assert len(todo_list) == 1
    assert todo_list[0]["task"] == "Task 1"
    assert not todo_list[0]["done"]

