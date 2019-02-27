#Model

from random import *

#Fonction permettant de générer une instance aléatoire 
#Elle retourne une liste de liste 
def creerInstanceAleatoire(taille):
    taquin = []

    #On remplit la variable avec des 0
    for i in range(0, taille):
        ligneType = [0 for i in range (0, taille)]
        taquin.append(ligneType)

    #On génére une liste de nombre pour remplir le taquin
    listeNombre = [i for i in range (0, taille*taille)]
    #On remplace le premier nombre 0 par -1 pour désigner la case vide
    listeNombre[0] = -1 
    colonne = 0
    ligne = 0 

    #Boucle pour remplir le taquin de manière aléatoire
    for i in range(taille*taille, 0, -1):
        #On choisit une valeur aléatoire 
        n = randint(0, i-1)
        #On la rajoute dans le taquin
        taquin[ligne][colonne] = listeNombre[n]
        #On l'enlève de la liste de nombre aléatoire
        listeNombre.pop(n)
        if colonne == taille-1:
            ligne += 1
        colonne = (colonne+1) % taille

    if estSolvable(taquin, taille):
        return taquin
    else:
        return creerInstanceAleatoire(taille)

#Méthode testant la validité d'une instance de taquin
def estSolvable(taquin, taille):

    #On commence par rechercher la position de la case vide
    for i, liste in enumerate(taquin):
        for j, nbr in enumerate(liste):
            if nbr == -1:
                ligne = i
                colonne = j
    #On réajuste la taille pour correspondre aux listes

    taille -= 1
    #On calcul le nombre de déplacements 
    caseVideNombre = (taille - colonne) + (taille - ligne)
    #On attribut la parité associé à la case vide
    if caseVideNombre % 2 == 0:
        caseVideNombre = "pair"
    else:
        caseVideNombre = "impair"

    #On transforme la liste de liste du taquin en liste
    listeTaquin = [i for liste in taquin for i in liste]

    #Compteur du nombre de permutation
    nbrPermutationNecessaire = 0

    #Boucle permettant de permuter les valeurs du taquin pour 
    #les classer dans l'ordre croissant en comptant le nombre de permutation 
    #necessaire
    for i, nbrDansListe in enumerate(listeTaquin):
        if nbrDansListe == i+1:
            pass
        else:
            for j, nbr in enumerate(listeTaquin):
                if nbr == i+1:  
                    listeTaquin[i], listeTaquin[j] = listeTaquin[j], listeTaquin[i]
                    nbrPermutationNecessaire += 1
                    break

    #On associe la parité associé 
    if nbrPermutationNecessaire % 2 == 0:
        nbrPermutationNecessaire = "pair"
    else:
        nbrPermutationNecessaire = "impair"


    if nbrPermutationNecessaire == caseVideNombre:
        return True
    else:
        return False

def creerTaquinFinal(taille):
    taquin = []

    #On remplit la variable avec des 0
    for i in range(0, taille):
        ligneType = [0 for i in range (0, taille)]
        taquin.append(ligneType)
    #On génére une liste de nombre pour remplir le taquin
    listeNombre = [i for i in range (1, taille*taille)]
    #On remplace le premier nombre 0 par -1 pour désigner la case vide
    listeNombre.append(-1)
    colonne = 0
    ligne = 0
    #Boucle pour remplir le taquin
    for i in range(taille*taille, 0, -1):
        #On rajoute les nombres dans l'ordre dans le taquin
        taquin[ligne][colonne] = listeNombre[0]
        #On l'enlève de la liste de nombre aléatoire
        listeNombre.pop(0)
        if colonne == taille-1:
            ligne += 1
        colonne = (colonne+1) % taille
    return taquin


            