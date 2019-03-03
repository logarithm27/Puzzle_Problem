# matrix that takes value from 1 to 10 (10 - 1 = 9 = 3²)
# reshape function takes first arg as number of lines and second as columns
# We want to build a matrix of a range equal to n²,
# hence, to reach n², we add 1 because we start from 1 and not 0
# max_range - start range = 10 - 1 = 9 = n²
import numpy
HORIZONTAL = 0
VERTICAL = 1


def matrix(num_blocks):
    max_range = numpy.square(num_blocks)+1
    # creer un tableau d'une seule dimension et remplir entre 1 et n² +1
    initial_puzzle_state = numpy.arange(1, max_range)
    # mélanger les valeurs du tableau aléatoirement
    numpy.random.shuffle(initial_puzzle_state)
    while not solvable(initial_puzzle_state):
        numpy.random.shuffle(initial_puzzle_state)
    # chercher la dernière valeur et remplacer par -1 pour représenter la case vide
    numpy.place(initial_puzzle_state, initial_puzzle_state == max_range - 1, 0)
    # convertir le tableau d'une dimension en une matrice
    initial_puzzle_state = numpy.reshape(initial_puzzle_state, (num_blocks, num_blocks))
    return initial_puzzle_state


def get_indices_of_elements(current_state):
    current_state_indices = {}
    for line in current_state:
        for column in line:
            global_index = numpy.argwhere(current_state == column)
            line_index = global_index[0][0]
            column_index = global_index[0][1]
            current_state_indices[column] = [line_index, column_index]
    return current_state_indices


def solvable(initial_input):
    inversion_count = 0
    array_length = len(initial_input)
    width = int(numpy.sqrt(array_length))
    for i in range(0, array_length, 1):
        if initial_input[i] == array_length:
            continue
        for j in range(i+1, len(initial_input), 1):
            if initial_input[j] == array_length:
                continue
            if initial_input[i] > initial_input[j]:
                inversion_count += 1
    if array_length % 2 != 0 and inversion_count % 2 == 0:
        return True
    if array_length % 2 == 0:
        matrix = numpy.reshape(initial_input, (width, width))
        blank_position = len(matrix) - numpy.argwhere(matrix == array_length)[0][0]
        odd_position = blank_position % 2 != 0 and inversion_count % 2 == 0
        even_position = blank_position % 2 == 0 and inversion_count % 2 != 0
        if even_position or odd_position:
            return True
    return False


def count_manhattan_distance(current_state_matrix):
    current_state_matrix_indices = get_indices_of_elements(current_state_matrix)
    goal_state_indices = get_indices_of_elements(generate_goal_state(len(current_state_matrix)))
    manhattan_distance = 0
    for key_number in current_state_matrix_indices:
        if current_state_matrix_indices[key_number] == goal_state_indices[key_number]:
            continue
        manhattan_distance += manhattan_distance_conditions(
            current_state_matrix_indices, goal_state_indices, key_number, HORIZONTAL, VERTICAL)
        manhattan_distance += manhattan_distance_conditions(
            current_state_matrix_indices, goal_state_indices, key_number, VERTICAL, HORIZONTAL)
        if current_state_matrix_indices[key_number][HORIZONTAL] != goal_state_indices[key_number][HORIZONTAL] and \
                current_state_matrix_indices[key_number][VERTICAL] != goal_state_indices[key_number][VERTICAL]:
            manhattan_distance += manhattan_distance_conditions_2(
                current_state_matrix_indices, goal_state_indices, key_number, HORIZONTAL)
            manhattan_distance += manhattan_distance_conditions_2(
                current_state_matrix_indices, goal_state_indices, key_number, VERTICAL)
    return manhattan_distance


def count_misplaced_blocks(current_state):
    misplaced_blocks = 0
    current_state_blocks_position = get_indices_of_elements(current_state)
    goal_state_blocks_position = get_indices_of_elements(generate_goal_state(len(current_state)))
    for key_number in current_state_blocks_position:
        if current_state_blocks_position[key_number] != goal_state_blocks_position[key_number]:
            misplaced_blocks += 1
    return misplaced_blocks


def generate_goal_state(length):
    goal_state = numpy.arange(1, numpy.square(length)+1)
    goal_state = numpy.reshape(goal_state, (length, length))
    numpy.place(goal_state, goal_state == numpy.square(length), 0)
    return goal_state


def manhattan_distance_conditions(current_state_indices, goal_state_indices, key_number, h_indice, v_indice):
    manhattan_distance = 0
    if current_state_indices[key_number][h_indice] == goal_state_indices[key_number][h_indice]:
        if current_state_indices[key_number][v_indice] > goal_state_indices[key_number][v_indice]:
            manhattan_distance += (current_state_indices[key_number][v_indice] - goal_state_indices[key_number][v_indice])
        elif goal_state_indices[key_number][v_indice] > current_state_indices[key_number][v_indice]:
            manhattan_distance += (goal_state_indices[key_number][v_indice] - current_state_indices[key_number][v_indice])
    return manhattan_distance


def manhattan_distance_conditions_2(current_state_indices, goal_state_indices, key_number, h_v_value):
    manhattan_distance = 0
    if current_state_indices[key_number][h_v_value] > goal_state_indices[key_number][h_v_value]:
        manhattan_distance += (current_state_indices[key_number][h_v_value] - goal_state_indices[key_number][h_v_value])
    if goal_state_indices[key_number][h_v_value] > current_state_indices[key_number][h_v_value]:
        manhattan_distance += (goal_state_indices[key_number][h_v_value] - current_state_indices[key_number][h_v_value])
    return manhattan_distance


def from_matrix_to_number(block):
    matrix_as_unique_number = ''
    for line in block:
        for column in line:
            matrix_as_unique_number += str(column)
    return int(matrix_as_unique_number)


def move(new_state, down_up_left_right_value):
    numpy.place(new_state, new_state == down_up_left_right_value, -2)
    numpy.place(new_state, new_state == 0, down_up_left_right_value)
    numpy.place(new_state, new_state == -2, 0)
    return new_state