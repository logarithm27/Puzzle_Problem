# !usr/bin/Omar/2019/NxN Puzzle
import sys
import threading
import time

from time import sleep

from ClasseST import *
import timeit
from Puzzle import *
from Node import *
from Play import *
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
    def __init__(self, taquin, instance):
        self.instance = instance
        self.taquin = taquin
        self.solved_in = float(timeit.timeit(lambda: self.play_game(), number=1))
        self.solved_in = round(self.solved_in, 6)
        self.main_win = QMainWindow()
        self.ui = UiForm()
        self.ui.setup_ui(self.main_win, self.states[0])
        self.main_win.setStyleSheet("background-color: rgb(66, 81, 80)")
        self.main_win.setFixedSize(self.main_win.width(), self.main_win.height())
        self.blocks = self.ui.buttons
        self.utility = Utility()
        self.ui.label.setText(" Solved in : " + str(self.solved_in) + " s"
                              '\n' + " Expanded states : " + str(self.expansed)
                              + '\n' + " Number of moves  : " + str(self.moves - 1))
        # self.node = []
        # for i, node in enumerate(self.play[0]):
        #     if i == 0:
        #         continue
        #     self.node.append(node)
        self.ui.start_button.clicked.connect(lambda: self.on_button_click())
        self.ui.shuffle.clicked.connect(lambda: self.on_shuffle_click())

    def play_game(self):
         self.puzzle = Puzzle(self.instance)
         self.state = Play(self.puzzle)
         self.play = self.state.play()


    def show(self):
        self.main_win.update()
        self.main_win.show()


    def on_button_click(self):
        self.move()

    def move(self):
        if self.indices2:
            the_action = self.indices2[0]
            from_ = the_action[0]
            where_it_moved = the_action[1]
            get_button = self.utility.function(from_, self.blocks)
            get_blank_button = self.utility.function(-1, self.blocks)
            x_neighbor = get_button.x()
            y_neighbor = get_button.y()
            self.anim = QPropertyAnimation(get_button, b"geometry")
            self.anim.setDuration(100)
            self.anim.setStartValue(QRect(get_button.x(), get_button.y(), 77, 77))
            self.anim.setEndValue(QRect(get_blank_button.x(), get_blank_button.y(), 77, 77))
            self.anim.start()
            self.anim2 = QPropertyAnimation(get_blank_button, b"geometry")
            self.anim2.setStartValue(QRect(get_blank_button.x(), get_blank_button.y(), 77, 77))
            self.anim2.setEndValue(QRect(x_neighbor, y_neighbor, 77, 77))
            self.anim2.start()
            self.blocks = self.utility.permute_buttons(get_blank_button, get_button, self.blocks)
            self.ui.label.setText(" Solved in : " + str(self.solved_in) + " s"
                                  '\n' + " Expanded states : " + str(self.expansed)
                                    +'\n'+" " + where_it_moved +
                                  '\n'+ " Number of moves  : " + str(len(self.indices2)-1))
            # print(str(from_) + str(self.node[0].action))
            # print(self.node[0].current_state.print_state())
            self.indices2.pop(0)

    def on_shuffle_click(self):
        num_blocks = 4
        taquin = SolutionTaquin(num_blocks)
        taquin.frontiere = SortedDict()
        taquin.explorer = {}
        taquin.initialiser(7, num_blocks)
        # app = QApplication(sys.argv)
        main_window = MainWindow(taquin, taquin.creerInstanceAleatoire(num_blocks))
        main_window.show()
        self.main_win.close()
        # sys.exit(app.exec_())



if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = MainWindow(taquin, taquin.instance)
    main_window.show()
    sys.exit(app.exec_())
