import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel



class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное меню")
        self.resize(1000, 450)


        self.start_button=QPushButton("Начало игры")
        self.start_button.clicked.connect(self.start_game)


        self.rules_button=QPushButton("Правила")
        self.rules_button.clicked.connect(self.show_rules)


        self.sound_button=QPushButton("Звук")
        self.sound_button.clicked.connect(self.show_sound_options)


        self.exit_button=QPushButton("Выход")
        self.exit_button.clicked.connect(self.close)


        # Создаем вертикальный layout и добавляем кнопки
        layout=QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.rules_button)
        layout.addWidget(self.sound_button)
        layout.addWidget(self.exit_button)


        # Создаем виджет, устанавливаем layout и устанавливаем виджет как основной виджет главного окна
        widget=QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



    def start_game(self):
        print("Начало игры")


    def show_rules(self):
        print("Правила")


    def show_sound_options(self):
        print("Звук")



if __name__=="__main__":
    app=QApplication(sys.argv)
    menu=MW()
    menu.show()
    sys.exit(app.exec())