from PyQt5 import QtCore, QtWidgets
from Numpy import matrix

class UiForm(object):

    def setup_ui(self, form, block):
        num_blocks = len(block)
        gaming_block = block

        # next access to the values inside generator, 0 is the shuffled matrix,
        # 1 is the goal state or ordered matrix, 2 is the number of blocks
        initial_puzzle_state = gaming_block
        form.setObjectName("Puzzle Game AI")
        form.setWindowTitle("Puzzle Game AI")
        # width and height of each button ( or block )
        width = 77
        height = 77
        # limit the window's size to the number of blocks
        # i.e : 77 * 3 = 231 ==> we'll have a windows of 231px x 231px
        form.resize(width * num_blocks + 300, width * num_blocks + 45)
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
                button.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(84, 219, 252, 255));\n"
                                     "border-radius:25px;\n"
                                     "font: 18pt \"Segoe UI Semilight\";")
                # the object name of each button is the number generated in the shuffled matrix
                button.setObjectName(str(j))
                button.setText(str(j))

                # hide the last element (last element should be the empty square)
                if j == -1:
                    button.setVisible(False)
                self.buttons[y_position].append(button)

        self.start_button = QtWidgets.QPushButton(form)
        self.start_button.setGeometry(QtCore.QRect(1,width * num_blocks +10, width * num_blocks +10,38))
        self.start_button.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(150, 252, 84, 255));\n"
                                        "border-radius:25px;\n"
                                        "font: 18pt \"Segoe UI Semilight\";")
        self.start_button.setObjectName('Move')
        self.start_button.setText('Play')

        self.shuffle = QtWidgets.QPushButton(form)
        self.shuffle.setGeometry(QtCore.QRect(width * num_blocks +17, width * num_blocks+9, width * num_blocks + 35,38))
        self.shuffle.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:1 rgba(255, 118, 165, 255));\n"
                                   "border-radius:25px;\n"
                                   "font: 18pt \"Segoe UI Semilight\";")
        self.shuffle.setObjectName('SH')
        self.shuffle.setText('Shuffle')

        self.label = QtWidgets.QLabel(form)
        self.label.setGeometry(width * num_blocks + 10,0,300,width * num_blocks)
        self.label.setObjectName('Action')
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n")




