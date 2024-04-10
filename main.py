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


        self.rules_button = QPushButton("Правила", self)
        self.rules_button.clicked.connect(self.open_Rules)
        self.rules_button.setFixedSize(150, 50)
        self.rules_button_layout.addWidget(self.rules_button)


        self.sound_button = QPushButton("Звук", self)
        self.sound_button.clicked.connect(self.open_Sounds)
        self.sound_button.setFixedSize(150, 50)
        self.sound_button_layout.addWidget(self.sound_button)


        self.quit_button = QPushButton("Выход", self)
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setFixedSize(150, 50)
        self.quit_button_layout.addWidget(self.quit_button)


        layout.addLayout(self.start_button_layout)
        layout.addLayout(self.rules_button_layout)
        layout.addLayout(self.sound_button_layout)
        layout.addLayout(self.quit_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setStyleSheet("background-color: #79D6F4;")
        button_style = """
                                QPushButton {
                                    font-size: 18px;
                                    border: 2px solid #8f8f8f;
                                    border-radius: 10px;
                                    padding: 10px;
                                    background-color: #d7d7d7;
                                }
                                QPushButton:hover {
                                    background-color: #7FB6C3;
                                }
                            """


        self.start_button.setStyleSheet(button_style)
        self.rules_button.setStyleSheet(button_style)
        self.sound_button.setStyleSheet(button_style)
        self.quit_button.setStyleSheet(button_style)


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
        self.setMinimumSize(800, 400)
        self.setStyleSheet("background-color: #79D6F4;")
        button_style = """
                                                               QPushButton {
                                                                   font-size: 15px;
                                                                   border: 2px solid #8f8f8f;
                                                                   border-radius: 10px;
                                                                   padding: 5px;
                                                                   background-color: #d7d7d7;
                                                               }
                                                               QPushButton:hover {
                                                                   background-color: #7FB6C3;
                                                               }
                                                           """

        buttons_layout = QVBoxLayout()
        matrix_layuot = QGridLayout()

        self.del_button_layout = QVBoxLayout()
        self.line_word = QVBoxLayout()
        self.help_button_layout = QVBoxLayout()
        self.back_button_layout = QVBoxLayout()
        self.check_button_layout = QVBoxLayout()


        self.del_button = QPushButton("Удалить", self)
        self.del_button.clicked.connect(self.del_letter)
        self.del_button.setFixedSize(100, 30)
        self.del_button_layout.addWidget(self.del_button)

        self.line_word = QLineEdit("")

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(100, 30)
        self.back_button_layout.addWidget(self.back_button)

        self.help_button = QPushButton("Подсказка", self)
        self.help_button.clicked.connect(self.helping)
        self.help_button.setFixedSize(100, 30)
        self.help_button_layout.addWidget(self.help_button)

        self.check_button = QPushButton("Проверить", self)
        self.check_button.clicked.connect(self.check_word)
        self.check_button.setFixedSize(100, 30)
        self.check_button_layout.addWidget(self.check_button)


        buttons_layout.addLayout(self.del_button_layout)
        buttons_layout.addWidget(self.line_word)
        buttons_layout.addLayout(self.check_button_layout)
        buttons_layout.addLayout(self.help_button_layout)
        buttons_layout.addLayout(self.back_button_layout)


        self.board = self.matrix()

        self.labels = []
        self.word = ''
        for i in range(4):
            for j in range(4):
                btn = QPushButton(self.board[i][j])
                btn.clicked.connect(self.btn_cl)
                btn.setStyleSheet(button_style)
                matrix_layuot.addWidget(btn, i, j)
                self.labels.append(btn)


        btn_matrix = QVBoxLayout()


        btn_matrix.addLayout(matrix_layuot)
        btn_matrix.addLayout(buttons_layout)


        widget = QWidget()
        widget.setLayout(btn_matrix)
        self.setCentralWidget(widget)


        self.del_button.setStyleSheet(button_style)
        self.help_button.setStyleSheet(button_style)
        self.back_button.setStyleSheet(button_style)
        self.check_button.setStyleSheet(button_style)

    def matrix(self):
        letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        board = []
        row_letters = random.sample(letters, k = 16)
        for i in range(0, 16, 4):
            row = row_letters[i:i + 4]
            board.append(row)
        return board

    def btn_cl(self):
        sender = self.sender()
        self.word += sender.text()
        self.line_word.setText(self.word)

    def del_letter(self):
        self.word = self.word[:-1]
        self.line_word.setText(self.word)

    def check_word(self):
        pass

    def helping(self):
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

        self.label = QLabel(
            "Правила игры:\nВ начале выводится матрица 4*4, заполненная буквами русского алфавита.\nПользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\nОчки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\nВ игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится подходящее слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру",
            self)
        self.label.setStyleSheet("""
            font-size:20px;
            """)

        self.back_button_layout = QVBoxLayout()
        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(100, 30)
        self.back_button_layout.addWidget(self.back_button)

        layout.addWidget(self.label)
        layout.addLayout(self.back_button_layout)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setStyleSheet("background-color: #79D6F4;")
        button_style = """
                                                QPushButton {
                                                    font-size: 15px;
                                                    border: 2px solid #8f8f8f;
                                                    border-radius: 10px;
                                                    padding: 5px;
                                                    background-color: #d7d7d7;
                                                }
                                                QPushButton:hover {
                                                    background-color: #7FB6C3;
                                                }
                                            """
        self.back_button.setStyleSheet(button_style)

    def comeback(self):
        self.menu = MW()
        self.menu.show()
        self.close()



class Sounds(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Звук")
        self.setMinimumSize(300, 500)

        self.Music()

        layout = QVBoxLayout()

        self.music_play_button_layout = QVBoxLayout()
        self.music_stop_button_layout = QVBoxLayout()

        self.back_button_layout = QVBoxLayout()
        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(150, 50)
        self.back_button_layout.addWidget(self.back_button)

        self.music_play_button = QPushButton("Включить музыку", self)
        self.music_play_button.clicked.connect(self.sound_play)
        self.music_play_button.setFixedSize(150, 50)
        self.music_play_button_layout.addWidget(self.music_play_button)

        self.music_stop_button = QPushButton("Остановить музыку", self)
        self.music_stop_button.clicked.connect(self.sound_stop)
        self.music_stop_button.setFixedSize(150, 50)
        self.music_stop_button_layout.addWidget(self.music_stop_button)

        layout.addLayout(self.music_play_button_layout)
        layout.addLayout(self.music_stop_button_layout)
        layout.addLayout(self.back_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setStyleSheet("background-color: #79D6F4;")
        button_style = """
                                                    QPushButton {
                                                        font-size: 15px;
                                                        border: 2px solid #8f8f8f;
                                                        border-radius: 10px;
                                                        padding: 5px;
                                                        background-color: #d7d7d7;
                                                    }
                                                    QPushButton:hover {
                                                        background-color: #7FB6C3;
                                                    }
                                                """
        self.music_stop_button.setStyleSheet(button_style)
        self.music_play_button.setStyleSheet(button_style)
        self.back_button.setStyleSheet(button_style)

    def Music(self):
        self.sound = QSound("song.wav", self)

    def sound_play(self):
        self.sound.play()

    def sound_stop(self):
        self.sound.stop()

    def comeback(self):
        self.menu = MW()
        self.menu.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MW()
    menu.show()
    sys.exit(app.exec())
