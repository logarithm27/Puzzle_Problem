from Module1 import *
from Utility import *
import numpy
import Numpy
def test():
    instance = Numpy.matrix(4)[0]
    button = BlankButton()
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

test()