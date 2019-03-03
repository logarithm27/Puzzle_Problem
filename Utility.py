import numpy
from Button import *


class Utility:
    def __init__(self):
        self.line_index_blank_button = 0
        self.column_index_blank_button = 0
        self.left_neighbors = []
        self.right_neighbors = []
        self.up_neighbors = []
        self.down_neighbors = []
        self.matrix = None
        self.x = 0
        self.y = 0
        self.column_index = 0
        self.line_index = 0
        self.blank_button = None
    # convert graphical buttons to a matrix

    def convert_from_buttons_to_matrix(self, blocks):
        initial_puzzle_state = []
        for i, array_of_buttons in enumerate(blocks):
            for button in array_of_buttons:
                initial_puzzle_state.append(int(button.text()))
        self.matrix = numpy.reshape(initial_puzzle_state, (len(blocks), len(blocks)))

    # get graphical coordinate of the blank button

    def get_blank_button_coordinates(self, matrix, buttons):
        self.get_blank_button_indices(matrix)
        self.blank_button = buttons[self.line_index_blank_button][self.column_index_blank_button]

    def get_button_coordinates(self, matrix, value, buttons):
        self.get_button_indices(matrix, value)
        button = buttons[self.line_index][self.column_index]
        self.x = button.x()
        self.y = button.y()
    # get the indices on the matrix of the blank button

    def get_blank_button_indices(self, matrix):
        index = numpy.argwhere(matrix == -1)
        self.line_index_blank_button = index[0][0]
        self.column_index_blank_button = index[0][1]

    def get_button_indices(self, matrix, value):
        index = numpy.argwhere(matrix == int(value))
        self.line_index = index[0][0]
        self.column_index = index[0][1]

    def permute_buttons(self, button_1, button_2, blocks):
        self.get_button_indices(self.matrix, button_1.text())
        line_index_1 = self.line_index
        column_index_1 = self.column_index
        self.get_button_indices(self.matrix, button_2.text())
        line_index_2 = self.line_index
        column_index_2 = self.column_index
        buff = blocks[line_index_2][column_index_2]
        blocks[line_index_2][column_index_2] = blocks[line_index_1][column_index_1]
        blocks[line_index_1][column_index_1] = buff
        return blocks
    # pour avoir les voisins de la case vide du taquin

    def get_neighbor_buttons_of_blank_button(self, blocks):
        # chercher les indices de la case vide
        # self.convert_from_buttons_to_matrix(blocks)
        self.matrix = blocks
        self.get_blank_button_indices(self.matrix)
        # self.get_blank_button_coordinates(self.matrix, blocks)
        if self.line_index_blank_button == 0 or 0 < self.line_index_blank_button < len(self.matrix):
            for i in range(self.line_index_blank_button, len(self.matrix), 1):
                if self.matrix[i][self.column_index_blank_button] == -1:
                    continue
                self.down_neighbors.append(self.matrix[i][self.column_index_blank_button])
        if self.column_index_blank_button == 0 or 0 < self.column_index_blank_button < len(self.matrix):
            self.right_neighbors = self.matrix[self.line_index_blank_button][self.column_index_blank_button + 1::]
        if 0 < self.column_index_blank_button < len(self.matrix) or self.column_index_blank_button == len(self.matrix) - 1:
            self.left_neighbors = self.matrix[self.line_index_blank_button][self.column_index_blank_button - 1::-1]
        if self.line_index_blank_button == len(self.matrix) - 1 or 0 < self.line_index_blank_button < len(self.matrix):
            for i in range(self.line_index_blank_button, -1, -1):
                if self.matrix[i][self.column_index_blank_button] == -1:
                    continue
                self.up_neighbors.append(self.matrix[i][self.column_index_blank_button])

