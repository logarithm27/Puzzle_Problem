import numpy

#Test


def matrix(num_blocks):
    # matrix that takes value from 1 to 10 (10 - 1 = 9 = 3²)
    # reshape function takes first arg as number of lines and second as columns
    # We want to build a matrix of a range equal to n²,
    # hence, to reach n², we add 1 because we start from 1 and not 0
    # max_range - start range = 10 - 1 = 9 = n²
    max_range = numpy.square(num_blocks)+1
    final_puzzle_state = \
        numpy.arange(1, max_range).reshape(num_blocks, num_blocks)
    initial_puzzle_state = numpy.arange(1, max_range).reshape(num_blocks, num_blocks)
    # get index of last element
    index = numpy.where(initial_puzzle_state == max_range-1)[0][0]
    initial_puzzle_state[index][index] = -1
    final_puzzle_state[index][index] = -1
    # shuffling columns
    for i in range(num_blocks):
        numpy.random.shuffle(initial_puzzle_state[i])
    # shuffling lines
    numpy.random.shuffle(initial_puzzle_state)
    yield [initial_puzzle_state, final_puzzle_state]

    # # initial shuffled puzzle
    # print("initial state : ")
    # print(initial_puzzle_state)
    # # final or goal state
    # print("goal state : ")
    # print(final_puzzle_state)
    # # have we reached the final state ? :
    # print(numpy.array_equal(final_puzzle_state, initial_puzzle_state))

