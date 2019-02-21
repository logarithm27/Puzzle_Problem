from PyQt5 import QtCore, QtWidgets
from Numpy import matrix


class UiForm(object):
    def setup_ui(self, form):
        num_blocks = 3
        gaming_block = matrix(num_blocks)
        # next access to the values inside generator, 0 is the shuffled matrix,
        # 1 is the goal state or ordered matrix, 2 is the number of blocks
        initial_puzzle_state = next(gaming_block)[0]
        form.setObjectName("Puzzle Game AI")
        form.setWindowTitle("Puzzle Game AI")
        # width and height of each button ( or block )
        width = 77
        height = 77
        # limit the window's size to the number of blocks
        # i.e : 77 * 3 = 231 ==> we'll have a windows of 231px x 231px
        form.resize(width * num_blocks, width * num_blocks)
        # initialize matrix of buttons similar to the shuffled matrix
        self.buttons = [[] for i in range(num_blocks)]
        y_coordinate = 0
        for y_position, i in enumerate(initial_puzzle_state):
            # x coordinate set back to 0 each time we've done building the current line
            x_coordinate = 0
            if not y_position == 0:
                y_coordinate += 80
                # x_position is the index, j is the value on that index
                # i.e : array[x_position] = j
            for x_position, j in enumerate(i):
                # if button is the first element, then x coordinate will be set to 0
                if not x_position == 0:
                    x_coordinate += 80
                button = QtWidgets.QPushButton(form)
                button.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, width, height))
                button.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
                # the object name of each button is the number generated in the shuffled matrix
                button.setObjectName(str(j))
                button.setText(str(j))
                # hide the last element (last element should be the empty square)
                if j == -1:
                    button.setVisible(False)
                self.buttons[y_position].append(button)



