# usr/bin/Omar/2019/NxN Puzzle

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, QPropertyAnimation
from Ui import UiForm

class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = UiForm()
        self.ui.setup_ui(self.main_win)
        self.main_win.setStyleSheet("background-color: rgb(178, 222, 124)")
        self.main_win.setFixedSize(self.main_win.width(), self.main_win.height())
        # self.ui.buttons[2][2].clicked.connect(lambda : self.on_button_click(160, 160, self.ui.pushButton_8))

    def show(self):
        self.main_win.show()

    def on_button_click(self, x_coordinate, y_coordinate, _button):
        self.anim = QPropertyAnimation(_button, b"geometry")
        self.anim.setDuration(100)
        # self.anim.setStartValue(QRect(_button.x(), _button.y(), 77, 77))
        self.anim.setEndValue(QRect(x_coordinate, y_coordinate, 77, 77))
        print('mooving')
        self.anim.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

