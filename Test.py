from Module1 import *
from Utility import *
import numpy
from Numpy import *


def test():
    instance = matrix(3)[0]
    button = Utility()
    button.get_neighbor_buttons_of_blank_button(instance)
    print("Taquin :")
    print(instance)
    print("Voisins de gauche :")
    print(button.left_neighbors)
    print("Voisins de droite :")
    print(button.right_neighbors)
    print("Voisins du haut:")
    print(button.up_neighbors)
    print("Voisins du bas :")
    print(button.down_neighbors)

    indices_initial_state = get_indices_of_elements(instance)
    indices_final_state = get_indices_of_elements(matrix(3)[1])
    for element in indices_initial_state:
        print(element, indices_initial_state[element])

    for element in indices_final_state:
        print(element, indices_final_state[element])




test()