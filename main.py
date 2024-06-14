import sys
import random
import math
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

        self.setStyleSheet("background-color: #F5F5F5;")
        button_style = """
            font-weight:bold;
            font-size: 15px;
            border: none;
            border-radius: 15px;
            padding: 15px;
            background-color: #2196F3;
            color: white;
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
        self.setStyleSheet("background-color: #F5F5F5;")
        button_style = """
            font-weight:bold;
            font-size: 18px;
            border: none;
            border-radius: 15px;
            padding: 6px;
            background-color: #2196F3;
            color: white;
                        """
        self.helping_btn = 0
        self.used_words = []
        self.score = 0
        self.open_cur_words()

        matrix_layout = QGridLayout()
        buttons_layout = QHBoxLayout()
        buttons_layout2 = QVBoxLayout()
        buttons_layout3 = QVBoxLayout()


        self.label_score = QLabel(f"Счёт: ")
        self.label_score.setStyleSheet("""
                                    font-size: 15px;
                                    padding: 10px;
                                    font-weight:bold;
                                    margin-bottom: 15px;
                                    border: 1px solid lightgrey;
                                    border-radius: 5px;
                                """)

        self.label_used_words = QLabel(f"Последнее слово: ")
        self.label_used_words.setStyleSheet("""
                                            font-size: 15px;
                                            padding: 10px;
                                            font-weight:bold;
                                            margin-bottom: 15px;
                                            border: 1px solid lightgrey;
                                            border-radius: 5px;
                                        """)

        self.line_word = QLineEdit("")
        self.line_word.setStyleSheet("""
                            font-size: 15px;
                            padding: 10px;
                            font-weight:bold;
                            margin-bottom: 15px;
                            border: 1px solid lightgrey;
                            border-radius: 5px;
                        """)

        self.del_button = QPushButton("Удалить", self)
        self.del_button.clicked.connect(self.del_letter)
        self.del_button.setFixedSize(180, 40)

        self.back_button = QPushButton("Назад", self)
        self.back_button.clicked.connect(self.comeback)
        self.back_button.setFixedSize(180, 40)

        self.help_button = QPushButton("Подсказка", self)
        self.help_button.clicked.connect(self.helping)
        self.help_button.setFixedSize(180, 40)

        self.check_button = QPushButton("Проверить", self)
        self.check_button.clicked.connect(self.check_word)
        self.check_button.setFixedSize(180, 40)

        self.label_timer = QLabel("90", self)
        self.label_timer.setStyleSheet("""
                                                            font-size: 25px;
                                                            padding: 10px;
                                                            font-weight:bold;
                                                            margin-bottom: 15px;
                                                            border: 1px solid lightgrey;
                                                            border-radius: 5px;
                                                        """)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        buttons_layout.addWidget(self.del_button)
        buttons_layout.addWidget(self.check_button)
        buttons_layout.addWidget(self.help_button)
        buttons_layout.addWidget(self.back_button)


        buttons_layout2.addWidget(self.label_timer)
        buttons_layout2.addWidget(self.label_score)
        self.board = self.matrix()


        self.labels = []
        self.word = ''
        for i in range(4):
            for j in range(4):
                btn = QPushButton(self.board[i][j])
                btn.clicked.connect(self.btn_cl)
                btn.setStyleSheet(button_style)
                matrix_layout.addWidget(btn, i, j)
                self.labels.append(btn)


        buttons_layout2.addLayout(matrix_layout)
        buttons_layout2.addWidget(self.line_word)
        buttons_layout3.addLayout(buttons_layout2)
        buttons_layout3.addWidget(self.label_used_words)


        btn_matrix = QVBoxLayout()


        btn_matrix.addLayout(buttons_layout3)
        btn_matrix.addLayout(buttons_layout)


        widget = QWidget()
        widget.setLayout(btn_matrix)
        self.setCentralWidget(widget)


        self.del_button.setStyleSheet(button_style)
        self.help_button.setStyleSheet(button_style)
        self.back_button.setStyleSheet(button_style)
        self.check_button.setStyleSheet(button_style)

    def matrix(self):
        letters = [chr(i) for i in range(1040, 1072)]
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

    def open_cur_words(self):
        with open('words.txt', 'r', encoding='utf-8') as self.wd:
            self.current_words = []
            self.current_words = self.wd.read().lower().split()

    def check_word(self):
        if self.current_words.count(str(self.word.lower())) == 1 and self.used_words.count(str(
            self.word.upper())) == 0:
            self.score += len(self.word)
            self.used_words.append(self.word)
            self.word = ''
            self.label_used_words.setText(f"Последнее слово: {''.join(self.used_words[-1:])}")
            self.label_score.setText(f"Счёт: {self.score}")
            self.timer.start()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Такого слова в словаре нет или оно уже было использовано!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def helping(self):
        if self.helping_btn <= 2:
            self.rand_word = random.choice(self.current_words)
            if self.rand_word not in self.used_words:
                self.score += math.ceil(len(self.rand_word)*0.5)
                self.used_words.append(self.rand_word)
                self.label_used_words.setText(f"Последнее слово: {self.rand_word.upper()}")
                self.label_score.setText(f"Счёт: {self.score}")
                self.helping_btn += 1
                self.timer.start()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы израсходовали подсказки!")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def comeback(self):
        self.menu = MW()
        self.menu.show()
        self.close()

    def update_timer(self):
        seconds = int(self.label_timer.text())
        seconds -= 1
        self.label_timer.setText(str(seconds))

        if seconds == 0:
            self.timer.stop()
            self.game_over()

    def game_over(self):
        msg = QMessageBox()
        msg.setWindowTitle("Конец")
        msg.setText("Время вышло, пора подводить итоги!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.game_window = Wgame()
        self.game_window.show()
        self.close()


class Rules(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.setMinimumSize(200, 300)

        layout = QVBoxLayout()

        self.label = QLabel(
            "Правила игры:\nВ начале выводится матрица 4*4, заполненная буквами русского алфавита.\nПользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\nОчки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\nВ игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится случайное слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру",
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

        self.setStyleSheet("background-color: #F5F5F5;")
        button_style = """
            font-weight:bold;
            font-size: 15px;
            border: none;
            border-radius: 15px;
            padding: 6px;
            background-color: #2196F3;
            color: white;
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
        self.back_button.setFixedSize(175, 50)
        self.back_button_layout.addWidget(self.back_button)

        self.music_play_button = QPushButton("Включить музыку", self)
        self.music_play_button.clicked.connect(self.sound_play)
        self.music_play_button.setFixedSize(175, 50)
        self.music_play_button_layout.addWidget(self.music_play_button)

        self.music_stop_button = QPushButton("Остановить музыку", self)
        self.music_stop_button.clicked.connect(self.sound_stop)
        self.music_stop_button.setFixedSize(175, 50)
        self.music_stop_button_layout.addWidget(self.music_stop_button)

        layout.addLayout(self.music_play_button_layout)
        layout.addLayout(self.music_stop_button_layout)
        layout.addLayout(self.back_button_layout)

        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setStyleSheet("background-color: #F5F5F5;")
        button_style = """
            font-weight:bold;
            font-size: 15px;
            border: none;
            border-radius: 15px;
            padding: 10px;
            background-color: #2196F3;
            color: white;
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
