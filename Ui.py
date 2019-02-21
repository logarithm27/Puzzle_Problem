from PyQt5 import QtCore, QtGui, QtWidgets
import numpy


class UiForm(object):
    def setup_ui(self, form):
        # number of blocks on the puzzle
        num_blocks = 3

        # matrix that takes value from 1 to 10 (10 - 1 = 9 = 3²)
        # reshape function takes first arg as number of lines and second as columns
        # We want to build a matrix of a range equal to n²,
        # hence, to reach n², we add 1 because we start from 1 and not 0
        # max_range - start range = 10 - 1 = 9 = n²

        max_range = numpy.square(num_blocks) + 1
        final_puzzle_state = \
            numpy.arange(1, max_range).reshape(num_blocks, num_blocks)

        initial_puzzle_state = numpy.arange(1, max_range).reshape(num_blocks, num_blocks)
        # get index of last element
        index = numpy.where(initial_puzzle_state == max_range - 1)[0][0]
        initial_puzzle_state[index][index] = -1
        final_puzzle_state[index][index] = -1
        # shuffling columns
        for i in range(num_blocks):
            numpy.random.shuffle(initial_puzzle_state[i])
        # shuffling lines
        numpy.random.shuffle(initial_puzzle_state)
        form.setObjectName("Puzzle Game AI")
        form.setWindowTitle("Puzzle Game AI")
        width = 77
        height = 77
        form.resize(width * num_blocks, width * num_blocks)
        self.buttons = []
        for i in range(num_blocks):
            self.buttons.append([])
        y_coordinate = 0
        for y_position, i in enumerate(initial_puzzle_state):
            x_coordinate = 0
            if not y_position == 0:
                y_coordinate += 80
            for x_position, j in enumerate(i):
                if not x_position == 0:
                    x_coordinate += 80
                button = QtWidgets.QPushButton(form)
                button.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, height))
                button.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
                button.setObjectName(str(j))
                button.setText(str(j))
                # hide the last element (last element should be the empty square)
                if j == -1:
                    button.setVisible(False)
                # self.buttons[y_position][x_position] = button



