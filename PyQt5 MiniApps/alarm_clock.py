from PyQt5.QtWidgets import QListWidget, QTimeEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QTime, QTimer

def create_alarm_clock_tab(layout):
    alarm_list = QListWidget()
    layout.addWidget(alarm_list)

    alarm_time_edit = QTimeEdit()
    alarm_time_edit.setDisplayFormat('HH:mm:ss')
    layout.addWidget(alarm_time_edit)

    add_alarm_button = QPushButton('Add Alarm')
    snooze_button = QPushButton('Snooze')

    layout.addWidget(add_alarm_button)
    layout.addWidget(snooze_button)

    alarm_timer = QTimer()
    alarm_timer.timeout.connect(lambda: check_alarm_time(alarm_list, alarm_timer))

    add_alarm_button.clicked.connect(lambda: add_alarm(alarm_time_edit, alarm_list))
    snooze_button.clicked.connect(lambda: snooze_alarm(alarm_time_edit, alarm_list))

    alarm_timer.start(1000)  # Check every second

def add_alarm(alarm_time_edit, alarm_list):
    alarm_time = alarm_time_edit.time().toString('HH:mm:ss')
    alarm_list.addItem(alarm_time)

def snooze_alarm(alarm_time_edit, alarm_list):
    current_time = QTime.currentTime()
    snooze_time = current_time.addSecs(300)  # Add 5 minutes
    alarm_time_edit.setTime(snooze_time)
    add_alarm(alarm_time_edit, alarm_list)

def check_alarm_time(alarm_list, alarm_timer):
    current_time = QTime.currentTime().toString('HH:mm:ss')
    for index in range(alarm_list.count()):
        if alarm_list.item(index).text() == current_time:
            alarm_timer.stop()
            show_alarm_message()
            alarm_list.takeItem(index)
            alarm_timer.start(1000)  # Restart the timer
            break

def show_alarm_message():
    QMessageBox.information(None, 'Alarm', 'Time to wake up!')
