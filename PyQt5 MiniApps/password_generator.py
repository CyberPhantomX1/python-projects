import random
import string
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QFormLayout, QCheckBox, QSpinBox

def create_password_generator_tab(layout):
    password_length_spinbox = QSpinBox()
    password_length_spinbox.setRange(1, 100)
    password_length_spinbox.setValue(12)

    include_uppercase = QCheckBox('Include Uppercase')
    include_uppercase.setChecked(True)

    include_numbers = QCheckBox('Include Numbers')
    include_numbers.setChecked(True)

    include_symbols = QCheckBox('Include Symbols')
    include_symbols.setChecked(True)

    generate_button = QPushButton('Generate Password')
    password_display = QLineEdit()
    password_display.setReadOnly(True)

    password_strength_label = QLabel('Strength: ')

    generate_button.clicked.connect(lambda: generate_password(password_length_spinbox, include_uppercase, include_numbers, include_symbols, password_display, password_strength_label))

    form_layout = QFormLayout()
    form_layout.addRow('Password Length:', password_length_spinbox)
    form_layout.addRow(include_uppercase)
    form_layout.addRow(include_numbers)
    form_layout.addRow(include_symbols)
    form_layout.addRow(generate_button)
    form_layout.addRow('Generated Password:', password_display)
    form_layout.addRow(password_strength_label)

    layout.addLayout(form_layout)

def generate_password(password_length_spinbox, include_uppercase, include_numbers, include_symbols, password_display, password_strength_label):
    length = password_length_spinbox.value()
    characters = string.ascii_lowercase
    if include_uppercase.isChecked():
        characters += string.ascii_uppercase
    if include_numbers.isChecked():
        characters += string.digits
    if include_symbols.isChecked():
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.setText(password)
    check_password_strength(password, password_strength_label)

def check_password_strength(password, password_strength_label):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    strength = 'Weak'
    if length >= 12 and has_upper and has_lower and has_digit and has_symbol:
        strength = 'Strong'
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_symbol)):
        strength = 'Moderate'

    password_strength_label.setText(f'Strength: {strength}')
