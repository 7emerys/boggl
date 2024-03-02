import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout
from PyQt5.QtMultimedia import QSound



class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")

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
        layout.setContentsMargins(100, 100, 100, 100)

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

        self.board = self.matrix()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.labels = []
        for i in range(4):
            for j in range(4):
                btn = QPushButton(self.board[i][j])
                btn.clicked.connect(self.btn_cl)
                layout.addWidget(btn, i, j)
                self.labels.append(btn)

        self.current_letter_label = QLabel("")
        layout.addWidget(self.current_letter_label, 5, 0, 1, 4)

        self.setLayout(layout)

    def matrix(self):
        letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        board = []
        for _ in range(4):
            row = [random.choice(letters) for _ in range(4)]
            board.append(row)
        return board

    def btn_cl(self):
        sender = self.sender()
        text = sender.text()
        self.current_letter_label.setText(text)

        podskazka = QPushButton("Подсказать", self)
        #self.podskazka.clicked.connect дописать то что будет происходить
        podskazka.move(900, 400)


class Rules(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setWindowTitle("Правила")
        self.label = QLabel("Правила игры:\nВ начале выводится матрица 4*4, заполненная буквами русского алфавита.\nПользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\nОчки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\nВ игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится подходящее слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру",self)
        self.label.setStyleSheet("""
        font-size:20px;
        """)
        layout.addWidget(self.label)
        self.setLayout(layout)

class Sounds(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Звук")
        self.resize(1000, 450)

        self.sound = QSound("song.wav", self)

        self.music_play_button = QPushButton("Включить музыку", self)
        self.music_play_button.clicked.connect(self.sound.play)
        self.music_play_button.move(450, 100)

        self.music_stop_button = QPushButton("Остановить музыку", self)
        self.music_stop_button.clicked.connect(self.sound.stop)
        self.music_stop_button.move(450, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MW()
    menu.show()
    sys.exit(app.exec())

