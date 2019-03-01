from Module1 import *
from sortedcontainers import SortedDict
from ClasseET import *

class SolutionTaquin(object):

    def __init__(self, taille, heuristique):
        #Contient instance de départ
        self.instance = creerInstanceAleatoire(taille)
        #self.instance = [[1, 2, 3, 4], [5, -1, 6, 8], [9, 10, 7, 11], [13, 14, 15, 12]]
        #Contient taquin final recherché
        self.taquinFinal = creerTaquinFinal(taille)
        #Contient l'ensemble des états explorés
        self.explorer = {}
        #Contient l'ensembles des états à explorer
        self.frontiere = SortedDict()
        #Contient les valeurs des heuristiques
        self.tabPonderation = [[36, 12, 12, 4, 1, 1, 4, 1, 0], [8, 7, 6, 5, 4, 3, 2, 1, 0], [8, 7, 6, 5, 3, 2, 4, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        #Contient l'heuristique utilisé
        self.heuristique = heuristique

        self.taille = taille

    def initialiser(self, heuristique, taille):
        #Ici on recherche la position de la case -1
        for i, liste in enumerate(self.instance):
            for j, nbr in enumerate(liste):
                if nbr == -1:
                    ligne = i
                    colonne = j
                    break
        hash = self.convertMatrixToInt2(self.instance, taille)
        #On crée l'état de départ
        etatInitial = EtatTaquin(self.instance, None, (ligne, colonne), 0, hash)
        #On lui attribut une évaluation de départ
        evaluation = self.calculEvaluation(etatInitial, heuristique)
        
        #Le dictionnaire frontière contient des liste d'états puisque
        #plusieurs clé(=évaluation) peuvent correspondre à des états différents
        self.frontiere[evaluation] = []
        self.frontiere[evaluation].append(etatInitial)


    def convertMatrixToInt(self, matrice, taille):
        hash = [str(i) for list in matrice for i in list]
        for j, i in enumerate(hash):
            if int(i)==-1:
                i=str(taille*taille)
                hash[j] = i
                break
        hash = int("".join(hash))
        return hash

    def convertMatrixToInt2(self, matrice, taille):
        hash = []
        for list in matrice:
            for i in list:
                hash.append(str(i))
                hash.append(str(9))

        for j, i in enumerate(hash):
            if int(i)==-1:
                i=str(taille*taille)
                hash[j] = i
                break
        hash = int("".join(hash))
        return hash


    def expanser(self, taquin, evaluation, numH, tailleTaquin):
        caseV = taquin.positionCaseVide

        #hash = self.convertMatrixToInt(taquin.matrice, tailleTaquin)
        if not taquin.hash in self.explorer:

            self.explorer[taquin.hash] = taquin

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if abs(i) != abs(j):
                        if caseV[0]+i < tailleTaquin and caseV[0] > -1 and caseV[1] + j < tailleTaquin and caseV[1] > -1:
                            nvxMatrice = []
                            for list in taquin.matrice:
                                nvxMatrice.append(list.copy())
                            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]+i][caseV[1]+j]
                            nvxMatrice[caseV[0]+i][caseV[1]+j] = -1
                            hash = self.convertMatrixToInt2(nvxMatrice, tailleTaquin)
                            if not hash in self.explorer:

                                nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0]+i, caseV[1]+j), taquin.g_E +1, hash)
                                nvlEvaluation = self.calculEvaluation(nvxEtat, numH)

                                if nvlEvaluation in self.frontiere:
                                    self.frontiere[nvlEvaluation].append(nvxEtat)
                                else: 
                                    self.frontiere[nvlEvaluation] = []
                                    self.frontiere[nvlEvaluation].append(nvxEtat)

                                if self.isSolution(nvxEtat.matrice):
                                    print("Eval= ", nvlEvaluation, " et g_E =", nvxEtat.g_E)
                                    self.afficherSolution(nvxEtat)
                                    pause = input("...")
                                    exit(0)
        
    #A optimiser
    def isSolution(self, etat):
        test = True
        for i, ligne in enumerate(etat):
            t = self.taquinFinal[i]
            if ligne != t:
                test = False
                break
        return test

    def afficherSolution(self, etat):
        listeSolution = []
        listeSolution.append(etat)
        while etat.parent != None:
            etat = etat.parent
            listeSolution.append(etat)
        for etat in reversed(listeSolution):
            self.afficherEtat(etat)
            

    def afficherEtat(self, etat):
        for list in etat.matrice:
            print(list)
        print()


            
    def calculEvaluation(self, etat, numeroH):
        #On récupère g(E)
        g_E = etat.g_E

        #On va calculer h(E)

        somme = 0
        if numeroH == 1:
            ponderation = self.tabPonderation[0]
            coefNorm = 4
        elif numeroH == 2:
            ponderation = [i for i in range(self.taille*self.taille, 0, -1)]
            #ponderation = self.tabPonderation[1]
            coefNorm = 1
        elif numeroH == 3:
            ponderation = [i for i in range(self.taille*self.taille, 0, -1)]
            coefNorm = 4
        elif numeroH == 4:
            ponderation = self.tabPonderation[2]
            coefNorm = 1
        elif numeroH == 5:
            ponderation = self.tabPonderation[2]
            coefNorm = 4
        elif numeroH == 6:
            ponderation = [1 for i in range(0, self.taille*self.taille)]
            #ponderation = self.tabPonderation[3]
            coefNorm = 1
        for i, liste in enumerate(etat.matrice):
            for j, num in enumerate(liste):
                if num != -1:
                    somme += self.distanceElementaire(num, (i, j)) * ponderation[num-1]
        h_E = somme // coefNorm

        Evaluation = g_E + h_E


        #Permet résolution taquin 4*4 et 5*5 en utilisant ligne suivante
        #Evaluation = h_E


        return Evaluation

    def distanceElementaire(self, valeur, position):

        found = False
        for i, liste in enumerate(self.taquinFinal):
            for j, num in enumerate(liste):
                if num == valeur:
                    positionRecherche = (i, j)
                    found = True
                    break
            if found:
                break

        distanceE = abs(position[0] - positionRecherche[0]) + abs(position[1] - positionRecherche[1])
        return distanceE



