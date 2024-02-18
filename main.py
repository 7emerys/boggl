import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel


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


        # Создаем виджет, устанавливаем layout и устанавливаем виджет как основной виджет главного окна
        widget=QWidget()
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


class Rules(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Правила")
        self.resize(1000, 450)
        label = QLabel("...", self)
        label.move(500, 200)
class Sounds(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Звук")
        self.resize(1000, 450)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu = MW()
    menu.show()
    sys.exit(app.exec())
