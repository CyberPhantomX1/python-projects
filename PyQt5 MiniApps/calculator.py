import math
from PyQt5.QtWidgets import QLineEdit, QPushButton, QGridLayout

def create_calculator_tab(layout):
    calc_display = QLineEdit()
    layout.addWidget(calc_display)

    grid_layout = QGridLayout()
    buttons = [
        ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
        ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
        ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
        ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
        ('C', 4, 0), ('M+', 4, 1), ('M-', 4, 2), ('MR', 4, 3),
        ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('√', 5, 3)
    ]

    memory = {'value': 0}

    for btn_text, row, col in buttons:
        button = QPushButton(btn_text)
        button.clicked.connect(lambda checked, b=btn_text: on_calc_button_click(b, calc_display, memory))
        grid_layout.addWidget(button, row, col)

    layout.addLayout(grid_layout)

def on_calc_button_click(button_text, calc_display, memory):
    if button_text == 'C':
        calc_display.clear()
    elif button_text == 'M+':
        try:
            memory['value'] += float(calc_display.text())
            calc_display.clear()
        except ValueError:
            calc_display.setText('Error')
    elif button_text == 'M-':
        try:
            memory['value'] -= float(calc_display.text())
            calc_display.clear()
        except ValueError:
            calc_display.setText('Error')
    elif button_text == 'MR':
        calc_display.setText(str(memory['value']))
    elif button_text == 'sin':
        try:
            result = math.sin(math.radians(float(calc_display.text())))
            calc_display.setText(str(result))
        except ValueError:
            calc_display.setText('Error')
    elif button_text == 'cos':
        try:
            result = math.cos(math.radians(float(calc_display.text())))
            calc_display.setText(str(result))
        except ValueError:
            calc_display.setText('Error')
    elif button_text == 'tan':
        try:
            result = math.tan(math.radians(float(calc_display.text())))
            calc_display.setText(str(result))
        except ValueError:
            calc_display.setText('Error')
    elif button_text == '√':
        try:
            result = math.sqrt(float(calc_display.text()))
            calc_display.setText(str(result))
        except ValueError:
            calc_display.setText('Error')
    elif button_text == '=':
        try:
            result = eval(calc_display.text())
            calc_display.setText(str(result))
        except Exception:
            calc_display.setText('Error')
    else:
        current_text = calc_display.text()
        new_text = current_text + button_text
        calc_display.setText(new_text)
