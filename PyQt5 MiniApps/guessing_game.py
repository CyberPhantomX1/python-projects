import random
from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QMessageBox, QVBoxLayout

def create_guessing_game_tab(layout):
    guess_input = QLineEdit()
    layout.addWidget(guess_input)

    guess_button = QPushButton('Guess')
    layout.addWidget(guess_button)

    attempts_label = QLabel('Attempts: 0')
    layout.addWidget(attempts_label)

    game_state = {'random_number': random.randint(1, 100), 'attempts': 0}

    guess_button.clicked.connect(lambda: on_guess_button_click(guess_input, attempts_label, game_state))

def on_guess_button_click(guess_input, attempts_label, game_state):
    guess = int(guess_input.text())
    game_state['attempts'] += 1
    attempts_label.setText(f'Attempts: {game_state["attempts"]}')

    if guess < game_state['random_number']:
        QMessageBox.information(None, 'Guess Result', 'Too low!')
    elif guess > game_state['random_number']:
        QMessageBox.information(None, 'Guess Result', 'Too high!')
    else:
        QMessageBox.information(None, 'Guess Result', f'Correct! The number was {game_state["random_number"]}')
        game_state['random_number'] = random.randint(1, 100)
        game_state['attempts'] = 0
        attempts_label.setText('Attempts: 0')
