from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


from PyQt5 import QtWidgets

def button_click(button_num):
    print(f"Нажата кнопка {button_num}")

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()
window.setWindowTitle("Пример кнопок")

# Создание 4 кнопок
button1 = QtWidgets.QPushButton("Кнопка 1")
button1.clicked.connect(lambda: button_click(1))
button2 = QtWidgets.QPushButton("Кнопка 2")
button2.clicked.connect(lambda: button_click(2))
button3 = QtWidgets.QPushButton("Кнопка 3")
button3.clicked.connect(lambda: button_click(3))
button4 = QtWidgets.QPushButton("Кнопка 4")
button4.clicked.connect(lambda: button_click(4))

# Создание вертикального и горизонтального размещения для кнопок
v_layout = QtWidgets.QVBoxLayout()
h_layout = QtWidgets.QHBoxLayout()
h_layout.addWidget(button1)
h_layout.addWidget(button2)
v_layout.addLayout(h_layout)
h_layout = QtWidgets.QHBoxLayout()
h_layout.addWidget(button3)
h_layout.addWidget(button4)
v_layout.addLayout(h_layout)

window.setLayout(v_layout)
window.show()

app.exec()