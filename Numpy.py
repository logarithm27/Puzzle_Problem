
from Utility import *
import numpy


def matrix(num_blocks):
    # matrix that takes value from 1 to 10 (10 - 1 = 9 = 3²)
    # reshape function takes first arg as number of lines and second as columns
    # We want to build a matrix of a range equal to n²,
    # hence, to reach n², we add 1 because we start from 1 and not 0
    # max_range - start range = 10 - 1 = 9 = n²
    max_range = numpy.square(num_blocks)+1
    final_puzzle_state = \
        numpy.arange(1, max_range).reshape(num_blocks, num_blocks)
    # creer un tableau d'une seule dimension et remplir entre 1 et n² +1
    initial_puzzle_state = numpy.arange(1, max_range)
    # chercher la dernière valeur et remplacer par -1 pour représenter la case vide
    numpy.place(initial_puzzle_state, initial_puzzle_state == max_range - 1, -1)
    # mélanger les valeurs du tableau aléatoirement
    numpy.random.shuffle(initial_puzzle_state)
    # convertir le tableau d'une dimension en une matrice 
    initial_puzzle_state = numpy.reshape(initial_puzzle_state, (num_blocks, num_blocks))
    return [initial_puzzle_state, final_puzzle_state]


def get_indices_of_elements(current_state):
    current_state_indices = {}
    for line in current_state:
        for column in line:
            global_index = numpy.argwhere(current_state == column)
            line_index = global_index[0][0]
            column_index = global_index[0][1]
            current_state_indices[column] = [line_index, column_index]
    return current_state_indices