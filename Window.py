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
    def __init__(self, instance):
        self.instance = instance
        self.solved_in = timeit.timeit(lambda: self.play_game(), number=1)
        self.main_win = QMainWindow()
        self.ui = UiForm()
        self.ui.setup_ui(self.main_win, self.instance)
        self.main_win.setStyleSheet("background-color: rgb(178, 222, 124)")
        self.main_win.setFixedSize(self.main_win.width(), self.main_win.height())
        self.blocks = self.ui.buttons
        self.utility = Utility()
        print("solved in : " + str(self.solved_in) + " s"
                              '\n' + "expansed states : " + str(self.play[1]) + '\n'
                              + "visited states " + str(self.play[2]))
        self.node = []
        for i, node in enumerate(self.play[0]):
            if i == 0:
                continue
            self.node.append(node)
        self.ui.start_button.clicked.connect(lambda: self.on_button_click())
        print("numebr of moves  : " + str(len(self.node)))

    def play_game(self):
        self.puzzle = Puzzle(self.instance)
        self.state = Play(self.puzzle)
        self.play = self.state.play()

    def show(self):
        self.main_win.show()

    def on_button_click(self):
        self.move()

    def move(self):
        if self.node:
            from_ = self.node[0].from_
            get_button = self.utility.function(from_, self.blocks)
            get_blank_button = self.utility.function(0, self.blocks)
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
            self.ui.label.setText(str(from_) + str(self.node[0].action))
            # print(str(from_) + str(self.node[0].action))
            # print(self.node[0].current_state.print_state())
            self.node.pop(0)



if __name__ == '__main__':

    
    taille = input("Donnez la taille du taquin: ")
    taille = int(taille)
    #heuristique = input("Donnez l'heuristique: ")
    #heuristique = int(heuristique)

    taquin = SolutionTaquin(taille)

    for i in range(6, 10):
        if i==6:
            continue
        start_time = time.time()
        print("Heuristique: ", i)
        taquin.frontiere = SortedDict()
        taquin.explorer = {}
        taquin.initialiser(i, taille)
        
        test = True
        while test:
            listeEtat = taquin.frontiere.popitem(0)
            for etat in listeEtat[1]:
                test = taquin.expanser(etat, listeEtat[0], i, taille)
                if not test:
                    break
                
        print("Temps d execution : %s secondes ---" % (time.time() - start_time))
        pause = input("Appuyez pour continuer...")
       

    app = QApplication(sys.argv)
    main_window = MainWindow(matrix(3))
    main_window.show()
    sys.exit(app.exec_())



