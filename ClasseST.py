from Module1 import *
from sortedcontainers import SortedDict
from ClasseET import *

class SolutionTaquin(object):

    def __init__(self, taille, heuristique):
        self.instance = creerInstanceAleatoire(taille)
        self.taquinFinal = creerTaquinFinal(taille)
        self.explorer = {}
        self.frontiere = SortedDict()
        self.tabPonderation = [[36, 12, 12, 4, 1, 1, 4, 1, 0],
                               [8, 7, 6, 5, 4, 3, 2, 1, 0],
                               [8, 7, 6, 5, 3, 2, 4, 1, 0],
                               [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.heuristique = heuristique

    def initialiser(self):
        
        for i, liste in enumerate(self.instance):
            for j, nbr in enumerate(liste):
                if nbr == -1:
                    ligne = i
                    colonne = j
                    break
        etatInitial = EtatTaquin(self.instance, None, (ligne, colonne), 0)
        evaluation = self.calculEvaluation(etatInitial, 6)
        
        self.frontiere[evaluation] = []
        self.frontiere[evaluation].append(etatInitial)

    def expanser(self, taquin, evaluation, numH):
        caseV = taquin.positionCaseVide
        if caseV[0]+1 < 3:
            nvxMatrice = []
            for list in taquin.matrice:
                nvxMatrice.append(list.copy())
            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]+1][caseV[1]]
            nvxMatrice[caseV[0]+1][caseV[1]] = -1
            nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0]+1, caseV[1]), taquin.g_E +1)
           
            nvlEvaluation = self.calculEvaluation(nvxEtat, numH)
            if nvlEvaluation in self.frontiere:
                self.frontiere[nvlEvaluation].append(nvxEtat)
            else: 
                self.frontiere[nvlEvaluation] = []
                self.frontiere[nvlEvaluation].append(nvxEtat)
            if self.isSolution(nvxEtat.matrice):
                print("Solution trouver!!!!!!!!!!!!!!")
                print("Eval= ", nvlEvaluation, " et g_E =", nvxEtat.g_E)
                self.afficherSolution(nvxEtat)
                pause = input("...")
                exit(0) 
            
        if caseV[0]-1 > -1:
            nvxMatrice = []
            for list in taquin.matrice:
                nvxMatrice.append(list.copy())
            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]-1][caseV[1]]
            nvxMatrice[caseV[0]-1][caseV[1]] = -1
            nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0]-1, caseV[1]), taquin.g_E +1)
            nvlEvaluation = self.calculEvaluation(nvxEtat, numH)
            if nvlEvaluation in self.frontiere:
                self.frontiere[nvlEvaluation].append(nvxEtat)
            else: 
                self.frontiere[nvlEvaluation] = []
                self.frontiere[nvlEvaluation].append(nvxEtat)
            if self.isSolution(nvxEtat.matrice):
                print("Solution trouver!!!!!!!!!!!!!!")
                print("Eval= ", nvlEvaluation, " et g_E =", nvxEtat.g_E)
                self.afficherSolution(nvxEtat)
                pause = input("...")
                exit(0)

        if caseV[1]+1 < 3:
            nvxMatrice = []
            for list in taquin.matrice:
                nvxMatrice.append(list.copy())
            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]][caseV[1]+1]
            nvxMatrice[caseV[0]][caseV[1]+1] = -1
            nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0], caseV[1]+1), taquin.g_E +1)
            nvlEvaluation = self.calculEvaluation(nvxEtat, numH)
            if nvlEvaluation in self.frontiere:
                self.frontiere[nvlEvaluation].append(nvxEtat)
            else: 
                self.frontiere[nvlEvaluation] = []
                self.frontiere[nvlEvaluation].append(nvxEtat)
            if self.isSolution(nvxEtat.matrice):
                print("Solution trouver!!!!!!!!!!!!!!")
                print("Eval= ", nvlEvaluation, " et g_E =", nvxEtat.g_E)
                self.afficherSolution(nvxEtat)
                pause = input("...")
                exit(0)

        if caseV[1]-1 > -1:
            nvxMatrice = []
            for list in taquin.matrice:
                nvxMatrice.append(list.copy())
            nvxMatrice[caseV[0]][caseV[1]] = nvxMatrice[caseV[0]][caseV[1]-1]
            nvxMatrice[caseV[0]][caseV[1]-1] = -1
            nvxEtat = EtatTaquin(nvxMatrice, taquin, (caseV[0], caseV[1]-1), taquin.g_E +1)
            nvlEvaluation = self.calculEvaluation(nvxEtat, numH)
            if nvlEvaluation in self.frontiere:
                self.frontiere[nvlEvaluation].append(nvxEtat)
            else: 
                self.frontiere[nvlEvaluation] = []
                self.frontiere[nvlEvaluation].append(nvxEtat)
            if self.isSolution(nvxEtat.matrice):
                print("Solution trouver!!!!!!!!!!!!!!")
                print("Eval= ", nvlEvaluation, " et g_E =", nvxEtat.g_E)
                self.afficherSolution(nvxEtat)
                pause = input("...")
                exit(0)

        if evaluation in self.explorer:
                self.explorer[evaluation].append(taquin)
        else: 
            self.explorer[evaluation] = []
            self.explorer[evaluation].append(taquin)
        
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
            ponderation = self.tabPonderation[1]
            coefNorm = 1
        elif numeroH == 3:
            ponderation = self.tabPonderation[1]
            coefNorm = 4
        elif numeroH == 4:
            ponderation = self.tabPonderation[2]
            coefNorm = 1
        elif numeroH == 5:
            ponderation = self.tabPonderation[2]
            coefNorm = 4
        elif numeroH == 6:
            ponderation = self.tabPonderation[3]
            coefNorm = 1
        for i, liste in enumerate(etat.matrice):
            for j, num in enumerate(liste):
                if num != -1:
                    somme += self.distanceElementaire(num, (i, j)) * ponderation[num-1]
        h_E = somme // coefNorm

        Evaluation = g_E + h_E

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






        



 




