import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from calculator import create_calculator_tab
from guessing_game import create_guessing_game_tab
from todo_list import create_todo_list_tab
from alarm_clock import create_alarm_clock_tab
from bmi_calculator import create_bmi_calculator_tab
from password_generator import create_password_generator_tab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Advanced Python Projects')
        self.setGeometry(100, 100, 1000, 800)

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        project_tabs = [
            ('Advanced Calculator', create_calculator_tab),
            ('Number Guessing Game', create_guessing_game_tab),
            ('To-Do List', create_todo_list_tab),
            ('Alarm Clock', create_alarm_clock_tab),
            ('BMI Calculator', create_bmi_calculator_tab),
            ('Password Generator', create_password_generator_tab),
        ]

        for tab_name, tab_func in project_tabs:
            self.add_project_tab(tab_name, tab_func)

    def add_project_tab(self, name, func):
        tab = QWidget()
        layout = QVBoxLayout()
        func(layout)
        tab.setLayout(layout)
        self.tabs.addTab(tab, name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
