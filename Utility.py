import numpy


class BlankButton:
    def __init__(self):
        self.line_index = 0
        self.column_index = 0
        self.left_neighbors = []
        self.left_neighbor = None
        self.right_neighbors = []
        self.right_neighbor = None
        self.up_neighbors = []
        self.up_neighbor = None
        self.down_neighbors = []
        self.down_neighbor = None
        self.matrix = None
        self.x = 0
        self.y = 0

    # convert graphical buttons to a matrix

    def convert_from_buttons_to_matrix(self, blocks):
        initial_puzzle_state = [[] for i in range(len(blocks))]
        for i, array_of_buttons in enumerate(blocks):
            for button in array_of_buttons:
                initial_puzzle_state[i].append(int(button.text()))
        self.matrix = numpy.asmatrix(initial_puzzle_state)

    # get graphical coordinate of the blank button

    def get_blank_button(self, matrix, buttons):
        self.get_button_indices(matrix, -1)
        button = buttons[self.line_index][self.column_index]
        self.x = button.x()
        self.y = button.y()

    # get the indices on the matrix of the blank button

    def get_button_indices(self, matrix, value):
        index = numpy.argwhere(matrix == value)
        self.line_index = index[0][0]
        self.column_index = index[0][1]

    # pour avoir les voisins de la case vide du taquin

    def get_neighbor_buttons_of_blank_button(self, matrix):
        # chercher les indices de la case vide
        self.get_button_indices(matrix, -1)
        if self.line_index == 0 or 0 < self.line_index < len(matrix):
            for i in range(self.line_index, len(matrix) - self.line_index):
                if matrix[self.line_index + i][self.column_index] == -1:
                    continue
                self.down_neighbors.append(matrix[self.line_index + i][self.column_index])
            if len(self.down_neighbors) != 0:
                self.down_neighbor = self.down_neighbors[0]
        if self.column_index == 0 or 0 < self.column_index < len(matrix):
            self.right_neighbors = matrix[self.line_index][self.column_index + 1::]
            if len(self.right_neighbors) != 0:
                self.right_neighbor = self.right_neighbors[0]
        if 0 < self.column_index < len(matrix) or self.column_index == len(matrix) - 1:
            self.left_neighbors = matrix[self.line_index][self.column_index - 1::-1]
            if len(self.left_neighbors) != 0:
                self.left_neighbor = self.left_neighbors[0]
        if self.line_index == len(matrix) - 1 or 0 < self.line_index < len(matrix):
            for i in range(self.line_index, 0, -1):
                if matrix[self.line_index - i][self.column_index] == -1:
                    continue
                self.up_neighbors.append(matrix[self.line_index - i][self.column_index])
                if len(self.up_neighbors) != 0:
                    self.up_neighbor = self.up_neighbors[0]
