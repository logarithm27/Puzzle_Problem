import numpy


class BlankButton:
    def __init__(self):
        self.line_index = 0
        self.column_index = 0
        self.left_neighbors = None
        self.left_neighbor = None
        self.right_neighbors = None
        self.right_neighbor = None
        self.up_neighbors = None
        self.up_neighbor = None
        self.down_neighbors = None
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

    # pour avoir les voisins du boutton vide

    def get_neighbor_buttons_of_blank_button(self, matrix):
        # si la case est vide se trouve au debut du taquin
        if self.line_index == 0 and self.column_index == 0:
            # avoir tous les voisins de la case vide qui se trouvent à droite
            self.right_neighbors = matrix[self.line_index][self.column_index+1::]
            # le premier voisin de la case vide à droite
            self.right_neighbor = self.right_neighbors[0]
            # tous les voisins du bas
            for i in range(1, len(matrix)):
                self.down_neighbors.apend(matrix[self.line_index+i][self.column_index])
            # le voisin du bas
            self.down_neighbor = self.down_neighbors[0]

        # si la case est vide se trouve dans les derniers indices du taquin
        if self.line_index == len(matrix)-1 and self.column_index == len(matrix)-1:
            # voisins de gauche
            self.left_neighbors = matrix[self.line_index][self.column_index-1::]
            # voisin de gauche
            self.left_neighbor = self.left_neighbors[0]
            # tous les voisins du haut
            for i in range(1, len(matrix)):
                self.up_neighbors.apend(self.matrix[self.line_index-i][self.column_index])
            self.up_neighbor = self.down_neighbors[0]

            # TO DO FOR OTHER CASES (pas encore complet)

