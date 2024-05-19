import json
from PyQt5.QtWidgets import QLineEdit, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox

def create_todo_list_tab(layout):
    todo_list = QListWidget()
    layout.addWidget(todo_list)

    todo_input = QLineEdit()
    add_button = QPushButton('Add')
    remove_button = QPushButton('Remove')
    save_button = QPushButton('Save')
    load_button = QPushButton('Load')

    h_layout = QHBoxLayout()
    h_layout.addWidget(todo_input)
    h_layout.addWidget(add_button)
    h_layout.addWidget(remove_button)

    layout.addLayout(h_layout)
    layout.addWidget(save_button)
    layout.addWidget(load_button)

    add_button.clicked.connect(lambda: add_todo_item(todo_input, todo_list))
    remove_button.clicked.connect(lambda: remove_todo_item(todo_list))
    save_button.clicked.connect(lambda: save_todo_list(todo_list))
    load_button.clicked.connect(lambda: load_todo_list(todo_list))

def add_todo_item(todo_input, todo_list):
    item_text = todo_input.text()
    if item_text:
        todo_list.addItem(item_text)
        todo_input.clear()

def remove_todo_item(todo_list):
    selected_items = todo_list.selectedItems()
    if not selected_items:
        return
    for item in selected_items:
        todo_list.takeItem(todo_list.row(item))

def save_todo_list(todo_list):
    items = [todo_list.item(index).text() for index in range(todo_list.count())]
    with open('todo_list.json', 'w') as file:
        json.dump(items, file)

def load_todo_list(todo_list):
    try:
        with open('todo_list.json', 'r') as file:
            items = json.load(file)
            todo_list.clear()
            todo_list.addItems(items)
    except FileNotFoundError:
        QMessageBox.information(None, 'Error', 'No saved to-do list found')
