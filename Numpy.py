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
    return convert_from_numpy_to_list(initial_puzzle_state)


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


def count_manhattan_distance_and_misplaced_blocks(current_state_matrix):
    goal_state = generate_goal_state(len(current_state_matrix))
    misplaced = 0
    distance = 0
    for i in range(len(current_state_matrix)):
        for j in range(len(current_state_matrix)):
            if current_state_matrix[i][j] != goal_state[i][j]:
                misplaced += 1
            if current_state_matrix[i][j] != 0:
                x, y = divmod(current_state_matrix[i][j] - 1, len(current_state_matrix))
                distance += abs(x - i) + abs(y - j)
    return distance + misplaced


def generate_goal_state(length):
    goal_state = []
    goal_state_using_numpy = numpy.arange(1, numpy.square(length)+1)
    numpy.place(goal_state_using_numpy, goal_state_using_numpy == numpy.square(length), 0)
    goal_state_using_numpy = numpy.reshape(goal_state_using_numpy, (length, length))
    for line in goal_state_using_numpy:
        line = line.tolist()
        goal_state.append(line)
    return goal_state


def convert_from_numpy_to_list(blocks):
    state = []
    for line in blocks:
        line = line.tolist()
        state.append(line)
    return state

