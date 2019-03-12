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
        self.main_win.setStyleSheet("background-color: rgb(178, 222, 124)")
        self.main_win.setFixedSize(self.main_win.width(), self.main_win.height())
        self.blocks = self.ui.buttons
        self.utility = Utility()
        self.ui.label.setText(" Solved in : " + str(self.solved_in) + " s"
                              '\n' + " Expanded states : " + str(self.expansed)
                              +'\n'+ " Number of moves  : " + str(self.moves)
                              )
        # self.node = []
        # for i, node in enumerate(self.play[0]):
        #     if i == 0:
        #         continue
        #     self.node.append(node)
        self.ui.start_button.clicked.connect(lambda: self.on_button_click())
        self.ui.shuffle.clicked.connect(lambda: self.on_shuffle_click())

    def play_game(self):
        # self.puzzle = Puzzle(self.instance)
        # self.state = Play(self.puzzle)
        # self.play = self.state.play()
        self.expansed = 0
        test = True
        while test:
            listeEtat = self.taquin.frontiere.popitem(0)
            for etat in listeEtat[1]:
                test, self.listeSolution = self.taquin.expanser(etat, listeEtat[0], 7, len(self.instance))
                if not test:
                    break
            self.expansed += 1
        self.moves = 0
        self.states = []
        for i, state in enumerate(reversed(self.listeSolution)):
            self.states.append(state.matrice)
            self.moves += 1
        self.moving()

    def show(self):
        self.main_win.update()
        self.main_win.show()

    def moving(self):
        self.indices = []
        self.indices2 = []
        self.indices3 = []
        for state in self.states:
            for line_index, column_index in itertools.product(range(len(self.instance)),
                                                              range(len(self.instance))):
                if state[line_index][column_index] == -1:
                        self.indices.append((line_index, column_index))
                        self.indices3.append((line_index, column_index))
        self.indices.pop(0)
        for state in self.states:
            if self.indices:
                ind2 = self.indices3.pop(0)
                ind = self.indices.pop(0)
                direcs = {' moved Right \u2192': (ind2[0], ind2[1]-1),
                          ' moved Left \u2190': (ind2[0], ind2[1]+1),
                          ' moved Down \u2193': (ind2[0]-1, ind2[1]),
                          ' moved Up \u2191': (ind2[0]+1, ind2[1])}
                ac = ''
                for action, (line, column) in direcs.items():
                    if (line, column) == ind:
                        ac = action
                        break
                ac = str(state[ind[0]][ind[1]]) + ac
                self.indices2.append((str(state[ind[0]][ind[1]]), ac))

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
                                  '\n'+ " Number of moves  : " + str(len(self.indices2)))
            # print(str(from_) + str(self.node[0].action))
            # print(self.node[0].current_state.print_state())
            self.indices2.pop(0)

    def on_shuffle_click(self):
        taquin = SolutionTaquin(4)
        taquin.frontiere = SortedDict()
        taquin.explorer = {}
        taquin.initialiser(7, 4)
        # app = QApplication(sys.argv)
        main_window = MainWindow(taquin, taquin.creerInstanceAleatoire(4))
        main_window.show()
        self.main_win.close()
        # sys.exit(app.exec_())



if __name__ == '__main__':
    # taille = input("Donnez la taille du taquin: ")
    # taille = int(taille)
    # heuristique = input("Donnez l'heuristique: ")
    # heuristique = int(heuristique)
    #
    # testPerf6 = []
    # testPerf7 = []
    # testPerf8 = []
    # testPerf9 = []
    # for perf in range(10):
    #     for i in range(6, 10):
    #         if i==64:
    #             continue
    #         start_time = time.time()
    #         print("Heuristique: ", i)
    # taquin.frontiere = SortedDict()
    # taquin.explorer = {}
    # taquin.initialiser(7, taille)
    # taquin.instance = taquin.creerInstanceAleatoire(taille)
    #
    # test = True
    # while test:
    #     listeEtat = taquin.frontiere.popitem(0)
    #     for etat in listeEtat[1]:
    #         test, listeSolution = taquin.expanser(etat, listeEtat[0], 7, taille)
    #         if not test:
    #             break
    # if i == 6:
    #     testPerf6.append(listeSolution[0].g_E)
    # if i == 7:
    #     testPerf7.append(listeSolution[0].g_E)
    # if i == 8:
    #     testPerf8.append(listeSolution[0].g_E)
    # if i == 9:
    #     testPerf9.append(listeSolution[0].g_E)
    # print("Temps d execution : %s secondes ---" % (time.time() - start_time))
    # pause = input("Appuyez pour continuer...")
    # somme=0
    # for element in testPerf6:
    #     somme += element
    # moyenne = somme / len(testPerf6)
    # print('La moyenne de heuristique 6 vaut: ', moyenne)
    # print('Max dans 6 = ', max(testPerf6))
    #
    # somme=0
    # for element in testPerf7:
    #     somme += element
    # moyenne = somme / len(testPerf7)
    # print('La moyenne de heuristique 7 vaut: ', moyenne)
    #
    # somme=0
    # for element in testPerf8:
    #     somme += element
    # moyenne = somme / len(testPerf8)
    # print('La moyenne de heuristique 8 vaut: ', moyenne)
    #
    # somme=0
    # for element in testPerf9:
    #     somme += element
    # moyenne = somme / len(testPerf9)
    # print('La moyenne de heuristique 9 vaut: ', moyenne)

    taquin = SolutionTaquin(4)
    taquin.frontiere = SortedDict()
    taquin.explorer = {}
    taquin.initialiser(7, 4)
    app = QApplication(sys.argv)
    main_window = MainWindow(taquin, taquin.creerInstanceAleatoire(4))
    main_window.show()
    sys.exit(app.exec_())
