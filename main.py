import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtMultimedia import QSound
from PyQt5.QtCore import Qt


class MW(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Боггл")
        self.resize(1000, 450)

        start_button = QPushButton("Начало игры", self)
        start_button.clicked.connect(self.open_Wgame)
        start_button.move(450, 100)

        rules_button = QPushButton("Правила", self)
        rules_button.clicked.connect(self.open_Rules)
        rules_button.move(450, 150)

        sound_button = QPushButton("Звук", self)
        sound_button.clicked.connect(self.open_Sounds)
        sound_button.move(450, 200)

        quit_button = QPushButton("Выход", self)
        quit_button.clicked.connect(self.close)
        quit_button.move(450, 250)



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

        self.board = self.generate_board()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignLeft)
        self.label.setText(self.get_board_text())
        layout.addWidget(self.label, 0, 0)

        self.setLayout(layout)

    def generate_board(self):
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                    'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        board = []
        for _ in range(4):
            row = [random.choice(alphabet) for _ in range(4)]
            board.append(row)
        return board

    def get_board_text(self):
        text = ''
        for row in self.board:
            text += ' '.join(row) + '\n'
        return text



        podskazka = QPushButton("Подсказать", self)
        #self.podskazka.clicked.connect дописать то что будет происходить
        podskazka.move(900, 400)


class Rules(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.resize(1000, 450)
        label6 = QLabel("Правила игры:\nВ начале выводится матрица 4*4, заполненная буквами русского алфавита.\nПользователь должен вписывать в поле ответа слово, состоящее из букв, которые есть в матрице.\nОчки зависят от длины и количества слов. За каждую букву начисляется 1 очко.\nВ игре есть кнопка подсказки слова, при нажатии на которую пользователю выводится подходящее слово.\nОчки за такое слово начисляются с коэффициентом 0,5, кнопка будет доступна 3 раза за 1 игру",self)
        label6.move(250, 100)


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

