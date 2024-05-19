from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QFormLayout
from PyQt5.QtChart import QChart, QChartView, QPieSeries

def create_bmi_calculator_tab(layout):
    form_layout = QFormLayout()

    weight_input = QLineEdit()
    height_input = QLineEdit()
    bmi_result_label = QLabel('BMI: ')

    calculate_button = QPushButton('Calculate')
    calculate_button.clicked.connect(lambda: calculate_bmi(weight_input, height_input, bmi_result_label, bmi_chart_view))

    bmi_chart_view = QChartView()

    form_layout.addRow('Weight (kg):', weight_input)
    form_layout.addRow('Height (m):', height_input)
    form_layout.addRow(calculate_button)
    form_layout.addRow(bmi_result_label)
    form_layout.addRow(bmi_chart_view)

    layout.addLayout(form_layout)

def calculate_bmi(weight_input, height_input, bmi_result_label, bmi_chart_view):
    try:
        weight = float(weight_input.text())
        height = float(height_input.text())
        bmi = weight / (height ** 2)
        bmi_result_label.setText(f'BMI: {bmi:.2f}')
        update_bmi_chart(bmi, bmi_chart_view)
    except ValueError:
        bmi_result_label.setText('Please enter valid numbers')

def update_bmi_chart(bmi, bmi_chart_view):
    series = QPieSeries()
    series.append('Underweight', 18.5)
    series.append('Normal weight', 24.9 - 18.5)
    series.append('Overweight', 29.9 - 24.9)
    series.append('Obesity', 40 - 29.9)

    if bmi < 18.5:
        series.slices()[0].setExploded(True)
    elif bmi < 24.9:
        series.slices()[1].setExploded(True)
    elif bmi < 29.9:
        series.slices()[2].setExploded(True)
    else:
        series.slices()[3].setExploded(True)

    chart = QChart()
    chart.addSeries(series)
    chart.setTitle('BMI Categories')
    bmi_chart_view.setChart(chart)
