from sortedcontainers import SortedDict
from ClasseET import *
from random import *

class SolutionTaquin(object):

    def __init__(self, taille):

        #Contient instance de départ
        self.instance = self.creerInstanceAleatoire(taille)
        #self.instance = [[1, 2, 3], [4, 5, 6], [7, -1, 8]]

        #Contient taquin final recherché
        self.matriceTaquinFinal = self.creerTaquinFinal(taille)

        #Contient le hash du taquin recherché
        self.hashTaquinFinal = self.creerHashTaquinFinal(self.matriceTaquinFinal)

        #Contient l'ensemble des états explorés
        self.explorer = {}

        #Contient l'ensembles des états à explorer
        self.frontiere = SortedDict()
        
        #Taille du taquin
        self.taille = taille


    def initialiser(self, heuristique, taille):
        #Ici on recherche la position de la case -1 (case vide)
        for i, liste in enumerate(self.instance):
            for j, nbr in enumerate(liste):
                if nbr == -1:
                    ligne = i
                    colonne = j
                    break
        #Tableau utilisé pour certaines heuristiques
        tabPonderation = [[36, 12, 12, 4, 1, 1, 4, 1, 0], [8, 7, 6, 5, 3, 2, 4, 1, 0]]

        #A chaque heuristique on attribu ses coeficients

        if heuristique == 1:
            self.ponderation = tabPonderation[0]
            self.coefNorm = 4
        elif heuristique == 2:
            self.ponderation = [i for i in range(self.taille*self.taille, 0, -1)]
            self.coefNorm = 2
        elif heuristique == 3:
            self.ponderation = [i for i in range(self.taille*self.taille, 0, -1)]
            self.coefNorm = 4
        elif heuristique == 4:
            self.ponderation = tabPonderation[1]
            self.coefNorm = 1
        elif heuristique == 5:
            self.ponderation = tabPonderation[1]
            self.coefNorm = 4
        elif heuristique == 6:
            self.ponderation = [1 for i in range(0, self.taille*self.taille)]
            self.coefNorm = 1
        elif heuristique == 7:
            nbrDiagonale = taille*2 -2
            self.ponderation = []
            for i in range(0, taille):
                for j in range(0, taille):
                    self.ponderation.append( nbrDiagonale - (i+j) )
            self.coefNorm = 1
        elif heuristique == 8:
            nbrDiagonale = taille*2 -2
            self.ponderation = []
            for i in range(0, taille):
                for j in range(0, taille):
                    self.ponderation.append( nbrDiagonale - (i+j) )
            self.coefNorm = 2
        elif heuristique == 9:
            self.ponderation = [4, 4, 4, 4, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 0]
            self.coefNorm = 1
        
        #Calcul du hachage de l'instance de départ
        hash = self.convertMatrixToInt3(self.instance)
        
        #On crée l'état de départ
        etatInitial = EtatTaquin(self.instance, None, (ligne, colonne), 0, hash)

        #On lui attribut une évaluation de départ
        evaluation = self.calculEvaluation(etatInitial, heuristique)
        
        #Le dictionnaire frontière contient des liste d'états à expanser classé selon
        #leurs clé(=évaluation) qui peuvent contenir plusieurs états différents
        self.frontiere[evaluation] = []
        self.frontiere[evaluation].append(etatInitial)

    #Fonction retournant la valeur du hachage qui servira comme
    #clé dans le dictionnaire explorer
    #Elle retourne un tuple obtenu à partir de la matrice
    def convertMatrixToInt3(self, matrice):
        hash = [str(i) for list in matrice for i in list]
        return tuple(hash)

    #Fonction permettant d'expanser chaque état
    def expanser(self, taquin, evaluation, numH, tailleTaquin):

        #On récupère en premier lieu la position de la case vide
        caseV = taquin.positionCaseVide

        #On vérifie si l'état n'a pas déja été explorer
        if not taquin.hash in self.explorer:

            #On rajoute l'état dans le dictionnaire d'états explorés
            self.explorer[taquin.hash] = taquin

            #Les 2 for et la condition if renvoie 4 valeurs de i et j:
            # i=-1 et j=0
            # i=0 et j=-1
            # i=0 et j=1
            # i=1 et j=0
            #Elle corespondent aux quatres déplacements possibles de la case vide
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if abs(i) != abs(j):

                        #On teste si le déplacement est réalisable
                        if caseV[0]+i < tailleTaquin and caseV[0]+i > -1 and caseV[1] + j < tailleTaquin and caseV[1]+j > -1:

                            #On va créer la nouvelle matrice en appliquant le déplacement
                            nvxMatrice = []
                            for list in taquin.matrice:
                                nvxMatrice.append(list.copy())
                            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]+i][caseV[1]+j]
                            nvxMatrice[caseV[0]+i][caseV[1]+j] = -1

                            #On calcul la nouvelle clé de hachage
                            hash = self.convertMatrixToInt3(nvxMatrice)

                            #On vérifie si la nouvelle matrice n'a pas deja était explorer
                            if not hash in self.explorer:

                                #On créer le nouvel état 
                                nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0]+i, caseV[1]+j), taquin.g_E +1, hash)
                                
                                #On lui calcul son évaluation
                                nvlEvaluation = self.calculEvaluation(nvxEtat, numH)

                                #On test si un état possède deja cette évaluation
                                #Si oui on rajoute l'état crée dans cette liste
                                if nvlEvaluation in self.frontiere:
                                    self.frontiere[nvlEvaluation].append(nvxEtat)
                                #Sinon on créer une nouvelle liste et y place le premier état
                                else: 
                                    self.frontiere[nvlEvaluation] = []
                                    self.frontiere[nvlEvaluation].append(nvxEtat)

                                #On test à chaque fois s'il s'agit de l'état final 
                                if self.isSolution(nvxEtat.hash):
                                    print("Nombre de deplacement requis = ", nvxEtat.g_E)
                                    #self.afficherSolution(nvxEtat)
                                    #pause = input("...")
                                    return False
        #On retourne vrai s'il faut continuer à chercher la solution                  
        return True
                                
    #On vérifie s'il s'agit de la solution en comparant les clé de hash avec la solution recherché
    def isSolution(self, hash):
        if hash == self.hashTaquinFinal:
            return True
        else:
            return False

    #Fonction permettant d'afficher la solution
    #Elle génére une liste contenant tout les états de transition entre l'instance et la solution 
    def afficherSolution(self, etat):

        #On initialise cette liste
        listeSolution = []

        #On y rajoute le premier état
        listeSolution.append(etat)

        #On la remplit
        while etat.parent != None:
            etat = etat.parent
            listeSolution.append(etat)

        #On l'affiche
        for etat in reversed(listeSolution):
            self.afficherEtat(etat)
            
    #Fonction permettant d'afficher un état sur l'écran
    def afficherEtat(self, etat):
        for list in etat.matrice:
            print(list)
        print()

    #Fonction permettant de calculer l'évaluation d'un état
    def calculEvaluation(self, etat, numeroH):

        #On récupère g(E)
        g_E = etat.g_E

        #On va calculer h(E)
        somme = 0
        #Pour chaque case on calcul l'éloignement et on le pondère
        for i, liste in enumerate(etat.matrice):
            for j, num in enumerate(liste):
                if num != -1:
                    somme += self.distanceElementaire(num, (i, j)) * self.ponderation[num-1]
        #On divise le tout par le coeficient de normalisation
        h_E = somme // self.coefNorm

        #On somme g(e) et h(e) pour obtenir notre évaluation
        Evaluation = g_E + h_E

        #Permet résolution sans tenir compte de g(e)
        #Evaluation = h_E

        return Evaluation

    #Fonction retournant la distance élémentaire entre une case et sa position final 
    def distanceElementaire(self, valeur, position):

        #On cherche la position de la valeur dans la matrice final recherché
        found = False
        for i, liste in enumerate(self.matriceTaquinFinal):
            for j, num in enumerate(liste):
                if num == valeur:
                    positionRecherche = (i, j)
                    found = True
                    break
            if found:
                break

        #On calcul l'écart donc la distance
        distanceE = abs(position[0] - positionRecherche[0]) + abs(position[1] - positionRecherche[1])
        return distanceE
    

    #Fonction permettant de générer une instance aléatoire 
    #Elle retourne une liste de liste 
    def creerInstanceAleatoire(self, taille):
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

        if self.estSolvable(taquin, taille):
            return taquin
        else:
            return self.creerInstanceAleatoire(taille)

        #Méthode testant la validité d'une instance de taquin
    def estSolvable(self, taquin, taille):
   
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

    #Fonction calculant le hash du taquin recherché
    def creerHashTaquinFinal(self, matrice):
        return self.convertMatrixToInt3(matrice)

    def creerTaquinFinal(self, taille):
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




        



 




