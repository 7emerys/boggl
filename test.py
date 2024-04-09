import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *


class MW(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")
        self.setMinimumSize(300, 500)

        layout = QVBoxLayout()

        self.start_button_layout = QVBoxLayout()
        self.rules_button_layout = QVBoxLayout()
        self.quit_button_layout = QVBoxLayout()
        self.sound_button_layout = QVBoxLayout()

        self.start_button = QPushButton("Начало игры", self)
        self.start_button.clicked.connect(self.open_Wgame)
        self.start_button.setFixedSize(150, 50)
        self.start_button_layout.addWidget(self.start_button)
        self.start_button.setStyleSheet("""
                font-size:20px;
                """)

        self.rules_button = QPushButton("Правила", self)
        self.rules_button.clicked.connect(self.open_Rules)
        self.rules_button.setFixedSize(150, 50)
        self.rules_button_layout.addWidget(self.rules_button)
        self.rules_button.setStyleSheet("""
                font-size:20px;
                """)

        self.sound_button = QPushButton("Звук", self)
        self.sound_button.clicked.connect(self.open_Sounds)
        self.sound_button.setFixedSize(150, 50)
        self.sound_button_layout.addWidget(self.sound_button)
        self.sound_button.setStyleSheet("""
        font-size:20px;
        """)

        self.quit_button = QPushButton("Выход", self)
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setFixedSize(150, 50)
        self.quit_button_layout.addWidget(self.quit_button)
        self.quit_button.setStyleSheet("""
                font-size:20px;
                """)

        layout.addLayout(self.start_button_layout)
        layout.addLayout(self.rules_button_layout)
        layout.addLayout(self.sound_button_layout)
        layout.addLayout(self.quit_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

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


class Wgame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")
        self.setMinimumSize(600, 800)

        layout = QVBoxLayout()

        self.podskazka_button_layout = QVBoxLayout()
        self.back_button_layout = QVBoxLayout()

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(150, 50)
        self.back_button_layout.addWidget(self.back_button)
        self.back_button.setStyleSheet("""
                                font-size:20px;
                                """)

        self.podskazka_button = QPushButton("Подсказка", self)
        self.podskazka_button.clicked.connect(self.podskazat)
        self.podskazka_button.setFixedSize(150, 50)
        self.podskazka_button_layout.addWidget(self.podskazka_button)
        self.podskazka_button.setStyleSheet("""
                        font-size:20px;
                        """)

        layout.addLayout(self.podskazka_button_layout)
        layout.addLayout(self.back_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def podskazat(self):
        pass

    def comeback(self):
        self.menu = MW()
        self.menu.show()
        self.close()


class Rules(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.setMinimumSize(200, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Правила игры:\nВ начале выводится матрица 4*4, заполненная буквами русского алфавита.\nПользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\nОчки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\nВ игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится подходящее слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру", self)
        self.label.setStyleSheet("""
        font-size:20px;
        """)

        self.back_button_layout = QVBoxLayout()
        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(150, 50)
        self.back_button_layout.addWidget(self.back_button)
        self.back_button.setStyleSheet("""
                                        font-size:20px;
                                        """)

        layout.addWidget(self.label)
        layout.addLayout(self.back_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def comeback(self):
        self.menu = MW()
        self.menu.show()
        self.close()


class Sounds(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Звук")
        self.setMinimumSize(300, 600)

        layout = QVBoxLayout()

        self.music_play_button_layout = QVBoxLayout()
        self.music_stop_button_layout = QVBoxLayout()

        self.music_play_button = QPushButton("Включить музыку", self)
        self.music_play_button.clicked.connect(self.sound_play)
        self.music_play_button.setFixedSize(150, 50)
        self.music_play_button_layout.addWidget(self.music_play_button)
        self.music_play_button.setStyleSheet("""
                                        font-size:20px;
                                        """)

        self.music_stop_button = QPushButton("Остановить музыку", self)
        self.music_stop_button.clicked.connect(self.sound_stop)
        self.music_stop_button.setFixedSize(150, 50)
        self.music_stop_button_layout.addWidget(self.music_stop_button)
        self.music_stop_button.setStyleSheet("""
                                        font-size:20px;
                                        """)

        layout.addLayout(self.music_play_button_layout)
        layout.addLayout(self.music_stop_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def Music(self):
        self.sound = QSound("song.wav", self)

    def sound_play(self):
        self.sound.play()

    def sound_stop(self):
        self.sound.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MW()
    menu.show()
    sys.exit(app.exec())