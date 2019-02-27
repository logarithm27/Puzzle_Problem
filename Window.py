# !usr/bin/Omar/2019/NxN Puzzle
import sys
from Module1 import *
from ClasseST import *


from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QRect, QPropertyAnimation
from Ui import UiForm
import numpy
from Utility import * 

# def convert_from_buttons_to_matrix(blocks):
#     initial_puzzle_state = [[] for i in range(len(blocks))]
#     for i, array_of_buttons in enumerate(blocks):
#         for button in array_of_buttons:
#             initial_puzzle_state[i].append(int(button.text()))
#     matrix = numpy.asmatrix(initial_puzzle_state)
#     return matrix


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = UiForm()
        self.ui.setup_ui(self.main_win)
        self.main_win.setStyleSheet("background-color: rgb(178, 222, 124)")
        self.main_win.setFixedSize(self.main_win.width(), self.main_win.height())
        # TO DO : functions slot to animate the block's move

        # self.ui.buttons[0][0].clicked.connect(lambda : self.on_button_click(160, 160, self.ui.pushButton_8))

    def show(self):
        self.main_win.show()

    # TO DO : animate button's move

    def on_button_click(self, x_coordinate, y_coordinate, _button):
        self.anim = QPropertyAnimation(_button, b"geometry")
        self.anim.setDuration(100)
        # self.anim.setStartValue(QRect(_button.x(), _button.y(), 77, 77))
        self.anim.setEndValue(QRect(x_coordinate, y_coordinate, 77, 77))
        print('moving')
        self.anim.start()


if __name__ == '__main__':

    taquin = SolutionTaquin(3, 6)
    taquin.initialiser()

    while 1:
        listeEtat = taquin.frontiere.popitem(0)
        for etat in listeEtat[1]:
            taquin.expanser(etat, listeEtat[0], 6)

    instance = creerInstanceAleatoire(3)
    while not estSolvable(instance, 3):
        instance = creerInstanceAleatoire(3)

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())