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
from PyQt5 import QtCore, QtWidgets

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
        self.blocks = self.ui.buttons
        self.utility = Utility()
        # TO DO : functions slot to animate the block's move
        self.blocks[0][0].clicked.connect(lambda: self.on_button_click())
        # self.utility.blank_button.clicked.connect(lambda: self.on_button_click(self.utility.blank_button))

    def show(self):
        self.main_win.show()

    # TO DO : animate button's move

    def on_button_click(self):
        print("click")
        self.utility.get_neighbor_buttons_of_blank_button(self.blocks)
        y = self.blocks
        for i in self.blocks:
            for j in i:
                print(j.text(), j.x(), j.y())
        neighbor = self.utility.down_neighbors.pop(0)
        x_neighbor = neighbor.x()
        y_neighbor = neighbor.y()
        self.anim = QPropertyAnimation(neighbor, b"geometry")
        self.anim.setDuration(100)
        self.blocks = self.utility.permute_buttons(self.utility.blank_button, neighbor, self.blocks)
        self.anim.setStartValue(QRect(neighbor.x(), neighbor.y(), 77, 77))
        self.anim.setEndValue(QRect(self.utility.blank_button.x(), self.utility.blank_button.y(), 77, 77))
        self.anim.start()
        print('moving')
        self.anim2 = QPropertyAnimation(self.utility.blank_button, b"geometry")
        self.anim2.setStartValue(QRect(self.utility.blank_button.x(), self.utility.blank_button.y(), 77, 77))
        self.anim2.setEndValue(QRect(x_neighbor, y_neighbor, 77, 77))
        self.anim2.start()
    # print(y == self.blocks)

if __name__ == '__main__':

    # taquin = SolutionTaquin(3, 6)
    # taquin.initialiser()
    #
    # while 1:
    #     listeEtat = taquin.frontiere.popitem(0)
    #     for etat in listeEtat[1]:
    #         taquin.expanser(etat, listeEtat[0], 6)
    #
    # instance = creerInstanceAleatoire(3)
    # while not estSolvable(instance, 3):
    #     instance = creerInstanceAleatoire(3)

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())