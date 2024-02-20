import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtMultimedia import QSound


class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")
        self.resize(1000, 450)

        self.start_button = QPushButton("Начало игры")
        self.start_button.clicked.connect(self.open_Wgame)

        self.rules_button = QPushButton("Правила")
        self.rules_button.clicked.connect(self.open_Rules)

        self.sound_button = QPushButton("Звук")
        self.sound_button.clicked.connect(self.open_Sounds)

        self.quit_button = QPushButton("Выход")
        self.quit_button.clicked.connect(self.close)


        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.rules_button)
        layout.addWidget(self.sound_button)
        layout.addWidget(self.quit_button)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_Wgame(self):
        self.game_window = Wgame()
        self.game_window.show()
        self.close()


    def open_Rules(self):
        self.rule_window = Rules()
        self.rule_window.show()
        self.close()

    def open_Sounds(self):
        self.sound_window = Sounds()
        self.sound_window.show()
        self.close()

class Wgame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")
        self.resize(1000, 450)

        self.podskazka = QPushButton("Подсказать", self)
        #self.podskazka.clicked.connect дописать то что будет происходить

class Rules(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.resize(1000, 450)
        label6 = QLabel("Правила игры:\n1. Есть только 1 режим игры.\n2. В начале выводится матрица 4*4, заполненная буквами русского алфавита.\n3. Пользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\n4. Очки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\n5. В игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится подходящее слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру",self)
        label6.move(250, 100)

class Sounds(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Звук")
        self.resize(1000, 450)

        self.sound = QSound("music.wav", self)
        self.music_button = QPushButton("Включить музыку", self)
        self.music_button.clicked.connect(self.sound.play)
        self.music_button.move(450, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MW()
    menu.show()
    sys.exit(app.exec())
