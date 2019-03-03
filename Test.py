from Module1 import *
from Utility import *
import numpy
from Numpy import *
import time
import timeit
from hashlib import *

def test():
    instance = matrix(5)
    print(instance)
    button = Utility()
    button.get_neighbor_buttons_of_blank_button(instance)
    print("Taquin :")
    print(instance)
    print("Voisin de gauche :")
    print(button.left_neighbor)
    print("Voisin de droite :")
    print(button.right_neighbor)
    print("Voisin du haut:")
    print(button.up_neighbor)
    print("Voisin du bas :")
    print(button.down_neighbor)
    print("tout les voisins :")
    for i in button.all_neighbors:
        print(i)

    # indices_initial_state = get_indices_of_elements(instance[0])
    # indices_final_state = get_indices_of_elements(matrix(3)[1])
    # for element in indices_initial_state:
    #     print(element, indices_initial_state[element])
    #
    # for element in indices_final_state:
    #     print(element, indices_final_state[element])
    #
    # for i in range(0, 3, 1):
    #     print(i)

    # print(instance[2])

print("executed in : ", timeit.timeit(test, number = 1))

