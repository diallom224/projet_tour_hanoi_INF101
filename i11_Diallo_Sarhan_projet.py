import time
import random 
import turtle
from colorama import Fore, Style
import colorama
colorama.init()
# -------------------------------------Partie_A-------------------------------- :
# Q1
def init(n):
    # Creation du plateau avec la condition initiale
    plateau = [list(range(n, 0, -1)), [], []]
    return plateau

# Q2
def nbDisques(plateau, numtour):
    # Vérification : si le numéro de la tour est valide
    if numtour < 0 or numtour > 2:
        print("Numéro de tour invalide.")
        return None
    # Renvoi le nombre de disques sur la tour spécifiée
    return len(plateau[numtour])

# Q3
def disqueSup(plateau, numtour):
    # Vérification : si le numéro de la tour est valide
    if numtour < 0 or numtour > 2:
        print("Numéro de tour invalide.")
        return -1
    # Vérification si la tour est vide
    if not plateau[numtour]:
        print("La tour est vide.")
        return -1
    # Renvoyer le numéro du disque supérieur
    return plateau[numtour][-1]


# Q4
def posDisque(plateau, numdisque):
    # Vérification : si le numéro de disque est valide
    if numdisque < 1 or numdisque > len(plateau[0]):
        print("Numéro de disque invalide.")
        return -1

    # Parcourir les tours pour trouver la position du disque
    for numtour, tour in enumerate(plateau):
        if numdisque in tour:
            return numtour

    # Si le disque n'est pas trouvé (ce qui ne devrait pas arriver si numdisque est correct)
    return -1



# Q5
def disqueSup(tour, disque):
    """
    Fonction axilaire qui renvoie True si la tour contient
    un disque plus grand que celui donné en argument.
    """
    if tour:
        return tour[-1] > disque
    else:
        return True


def verifDepl(plateau, nt1, nt2):
    # Fonction qui vérifie si le déplacement d'un disque de la tour nt1 vers la tour nt2 est autorisé.
    if 0 <= nt1 < len(plateau) and 0 <= nt2 < len(plateau):
        if plateau[nt1]:
            disque = plateau[nt1][-1]
            return disqueSup(plateau[nt2], disque)
        else:
            return False
    else:
        return False


# Q6

def verifVictoire(plateau, n):
    """
    Fonction qui vérifie si la configuration du plateau correspond à la victoire.
    """
    if len(plateau) < 3:
        return False  # Il doit y avoir au moins trois tours pour qu'il y ait une tour de droite

    # Vérifier si la tour de droite contient exactement n disques empilés dans l'ordre décroissant
    return plateau[-1] == list(range(n, 0, -1)) and all(not tour for tour in plateau[:-1])


# --------------------------------Partie_B--------------------------------------

# Q1



def dessiner_tour(x, hauteur, couleur, largeur):
    turtle.penup()
    turtle.goto(x - largeur / 2, -200)
    turtle.pendown()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    for _ in range(2):
        if hauteur != 0:  # Ajout de la condition pour éviter la division par zéro
            turtle.forward(largeur)
            turtle.left(90)
            turtle.forward(hauteur)
            turtle.left(90)
    turtle.end_fill()

def dessiner_base_plateau():
    " fonction auxilaire qui dessin la base du plateau."
    turtle.penup()
    turtle.goto(-180, -200)  # Ajustement de la position pour réduire la taille de la base à gauche
    turtle.pendown()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(360)  # Réduction de la largeur de la base
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()

# Q2

def dessiner_disque(x, y, rayon, couleur):
    turtle.penup()
    turtle.goto(x, y - rayon)  # Ajustement pour centrer le disque
    turtle.pendown()
    turtle.fillcolor(couleur)
    turtle.begin_fill()
    turtle.circle(rayon)
    turtle.end_fill()

def dessiner_tours_hanoi(plateau, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours):
    turtle.clear()
    "fonction auxilaire qui dessin la tour apres chaque etape du jeu,en gros une sorte de mise a jour"
    dessiner_base_plateau()

    x_tour1 = -ecart_tours / 2
    x_tour2 = x_tour1 + ecart_tours
    x_tour3 = x_tour2 + ecart_tours

    hauteur_tour = 160
    dessiner_tour(x_tour1, hauteur_tour, "brown", epaisseur_tour)
    dessiner_tour(x_tour2, hauteur_tour, "brown", epaisseur_tour)
    dessiner_tour(x_tour3, hauteur_tour, "brown", epaisseur_tour)

    for i, tour in enumerate(plateau):
        x_tour = [x_tour1, x_tour2, x_tour3][i]
        for j, disque in enumerate(tour):
            rayon_disque = taille_disque - j * 5
            y_disque = -200 + (j + 1) * taille_disque
            dessiner_disque(x_tour, y_disque, rayon_disque, couleurs_disques[disque])

#Q3

def effaceDisque(nd, plateau, n, taille_disque, couleurs_disques, epaisseur_tour, ecart_tours):
    for i, tour in enumerate(plateau):
        if nd in tour:
            nouveau_tour = [disque for disque in tour if disque != nd]
            plateau[i] = nouveau_tour
            dessineConfig(plateau, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)
            turtle.update()
            return
# Q4

def dessineConfig(plateau, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours):
    # Effacer les tours actuelles
    turtle.clear()

    # Dessiner la base du plateau
    dessiner_base_plateau()

    # Position initiale des tours
    x_tour1 = -ecart_tours / 2
    x_tour2 = x_tour1 + ecart_tours
    x_tour3 = x_tour2 + ecart_tours

    # Dessiner les tours
    hauteur_tour = 160  # Hauteur de la tour
    dessiner_tour(x_tour1, hauteur_tour, "brown", epaisseur_tour)
    dessiner_tour(x_tour2, hauteur_tour, "brown", epaisseur_tour)
    dessiner_tour(x_tour3, hauteur_tour, "brown", epaisseur_tour)

    # Dessiner les disques sur les tours
    for i, tour in enumerate(plateau):
        x_tour = [x_tour1, x_tour2, x_tour3][i]
        for j, disque in enumerate(tour):
            rayon_disque = taille_disque - j * 5  # Ajustement du diamètre du disque
            y_disque = -200 + (j + 1) * taille_disque
            dessiner_disque(x_tour, y_disque, rayon_disque, couleurs_disques[disque])


#Q5
def effaceTout(plateau, n):
    for i in range(n):
        effaceDisque(i + 1, plateau, n)



# --------------------------------Partie_C--------------------------------------

# Q1
def lireCoords(plateau):
    "initialisation des variables tou_depart et tour_darriver a None"
    tour_depart = None
    tour_arrivee = None

    while tour_depart is None or nbDisques(plateau, tour_depart) == 0:
        "dans les conditons de while on verifie bien que la tour de depart soit 0"
        try:#permet de faire une execption dans le cas ou utilisateur rentre pas une bonne valeur cela evite le bugs
            tour_depart = int(input("Tour de d'epart? : "))
            if not (0 <= tour_depart <= 2):
                print("Tour de départ invalide. Entrez un numéro entre 0 et 2.")
                tour_depart = None
        except ValueError:# fair exception a se message d'erreur : ValueError. pour eviter le bugs
            print("Veuillez entrer un numéro de tour valide.")

    while tour_arrivee is None or not verifDepl(plateau, tour_depart, tour_arrivee):
        try:
            tour_arrivee = int(input("Tour de d'arriver? : "))
            if not (0 <= tour_arrivee <= 2): # le cas ou la tour d'arriver n'est compris 0 et 2
                print("Tour d'arrivée invalide. Entrez un numéro entre 0 et 2.")
                tour_arrivee = None
            elif not verifDepl(plateau, tour_depart, tour_arrivee):# le cas ou il a deja un autre disque plus petit dans la tour darriver.
                print("Déplacement non autorisé. Choisissez une tour d'arrivée valide.")
                tour_arrivee = None
        except ValueError:#permet de fair une exception.
            print("Veuillez entrer un numéro de tour valide.")

    return tour_depart, tour_arrivee


# Q2

def jouerUnCoup(plateau, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours):
    # Afficher le plateau actuel
    dessineConfig(plateau, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)

    # Récupérer les coordonnées du mouvement
    tour_depart, tour_arrivee = lireCoords(plateau)

    # Vérifier si le déplacement est autorisé
    if verifDepl(plateau, tour_depart, tour_arrivee):
        # Récupérer le disque à déplacer
        disque_deplace = plateau[tour_depart][-1]

        # Effacer le disque de la tour de départ
        effaceDisque(disque_deplace, plateau, n, taille_disque, couleurs_disques, epaisseur_tour, ecart_tours)

        # Déplacer le disque vers la tour d'arrivée
        plateau[tour_arrivee].append(disque_deplace)

        # Afficher la nouvelle configuration du plateau
        dessineConfig(plateau, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)

    else:
        print("Déplacement non autorisé. Choisissez une autre action.")


# Q3

def boucleJeu(plateau, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours, limite_coups=None):
    coups_joues = 0
    victoire = False
    print(" Binevenue dans la tour de hanoi :)")
    while not verifVictoire(plateau, 3):
        jouerUnCoup(plateau, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)

        coups_joues += 1

        if limite_coups is not None and coups_joues >= limite_coups:
            print(f"Limite de coups atteinte. Vous avez perdu.")
            return coups_joues, False

    print(f"Félicitations! Vous avez gagné en {coups_joues} coups.")
    return coups_joues, True


# Q4 jai combiner cette question avec la question 3

# --------------------------------Partie_D--------------------------------------

# Q1
def dernierCoup(coups):
    dernier_num_coup = max(coups.keys())
    dernier_coup = coups[dernier_num_coup]
    return dernier_coup[0], dernier_coup[-1]

def annulerDernierCoup(coups):
    if len(coups) > 1:
        dernier_num_coup = max(coups.keys())
        del coups[dernier_num_coup]


# Q3
def boucleJeuAvecAnnulation(plateau, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours,
                            limite_coups=None):
    coups_joues = 0
    victoire = False
    coups = {0: [tour.copy() for tour in plateau]}

    print("Bienvenue dans la tour de Hanoï :)")

    while not verifVictoire(plateau, 3):
        jouerUnCoup(plateau, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)
        coups_joues += 1

        if limite_coups is not None and coups_joues >= limite_coups:
            print(f"Limite de coups atteinte. Vous avez perdu.")
            return coups_joues, False

        coups[coups_joues] = [tour.copy() for tour in plateau]

        annuler = input("Voulez-vous annuler le dernier coup? (o/n): ").lower()

        if annuler == 'o':
            annulerDernierCoup(coups)
            if coups_joues >= 1:
                coups_joues -= 1
                plateau = [tour.copy() for tour in coups[coups_joues]]
                print("Dernier coup annulé.")
            else:
                print("Impossible d'annuler le dernier coup. Pas assez de coups joués.")

    print(f"Félicitations! Vous avez gagné en {coups_joues} coups.")
    return coups_joues, True



""""

# Configuration des disques et des tours
plateau_exemple = [[3, 2, 1], [], []]
couleurs_disques = {1: "red", 2: "green", 3: "blue"}
epaisseur_tour = 10  # Ajustement de l'épaisseur de la tour
taille_disque = 30  # Ajustement du diamètre du disque
ecart_tours = 60

turtle.speed(10)
limite_coups = 50
resultat = boucleJeuAvecAnnulation(plateau_exemple, nbDisques, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours, limite_coups)
turtle.mainloop()

"""

# --------------------------------Partie_E--------------------------------------

# Q1


def sauvScore(scores, nom_joueur, nb_disques, nb_coups):
    if nom_joueur not in scores:
        scores[nom_joueur] = []

    scores[nom_joueur].append((nb_disques, nb_coups))

# Q3
def boucleJeuAvecAnnulationEtScore(plateau_initial, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours,
                                    limite_coups=None, scores=None):
    coups_joues = 0
    coups = {0: [tour.copy() for tour in plateau_initial]}

    print("Bienvenue dans la tour de Hanoï :)")

    while not verifVictoire(plateau_initial, 3):
        jouerUnCoup(plateau_initial, n, couleurs_disques, epaisseur_tour, taille_disque, ecart_tours)
        coups_joues += 1

        if limite_coups is not None and coups_joues >= limite_coups:
            print(f"Limite de coups atteinte. Vous avez perdu.")
            return coups_joues, False  # Suppression de la valeur de retour redondante

        coups[coups_joues] = [tour.copy() for tour in plateau_initial]

        annuler = input("Voulez-vous annuler le dernier coup? (o/n): ").lower()

        if annuler == 'o':
            annulerDernierCoup(coups)
            if coups_joues >= 1:
                coups_joues -= 1
                plateau_initial = [tour.copy() for tour in coups[coups_joues]]
                print("Dernier coup annulé.")
            else:
                print("Impossible d'annuler le dernier coup. Pas assez de coups joués.")

    print(f"Félicitations! Vous avez gagné en {coups_joues} coups.")
    
    nom_joueur = input("Entrez votre nom: ")
    sauvScore(scores, nom_joueur, n, coups_joues)  # Utilisation du paramètre n
    
    recommencer = input("Voulez-vous recommencer une nouvelle partie? (o/n): ").lower()
    if recommencer == 'o':
        plateau_initial = init(n)
        print("Nouvelle partie commencée.")
    else:
        print("Merci d'avoir joué!")

    return coups_joues, True  # Suppression de la valeur de retour redondante


"""
# Exemple d'utilisation
scores_exemple = {
    "Joueur1": [(3, 20), (4, 30)],
    "Joueur2": [(3, 18), (4, 25)],
    "Joueur3": [(3, 22), (5, 40)],
}

# Affichage des scores pour un nombre de disques donné
afficheScores(scores_exemple, nb_disques=4)

# Affichage de tous les scores
afficheScores(scores_exemple)
"""
#4

def afficheScores(scores, nb_disques=None):
    if nb_disques is not None:
        scores = {joueur: infos for joueur, infos in scores.items() if any(nb == nb_disques for nb, _ in infos)}
    else:
        scores = {joueur: infos for joueur, infos in scores.items()}

    if not scores:
        print(f"Aucun score disponible pour {nb_disques} disques.")
        return

    print(f"Tableau des scores{' pour ' + str(nb_disques) + ' disques' if nb_disques is not None else ''} :")
    print("Joueur\t\tNombre de coups")

    for joueur, infos in sorted(scores.items(), key=lambda x: min(y[1] for y in x[1])):
        for nb, coups in sorted(infos, key=lambda x: x[1]):
            print(f"{joueur}\t\t{coups} coups (Nombre de disques: {nb})")
"""
# Exemple d'utilisation
scores_exemple = {
    "Joueur1": [(3, 20), (4, 30)],
    "Joueur2": [(3, 18), (4, 25)],
    "Joueur3": [(3, 22), (5, 40)],
}

# Affichage des scores pour un nombre de disques donné
afficheScores(scores_exemple, nb_disques=4)

# Affichage de tous les scores
afficheScores(scores_exemple)
"""

#Q5


def afficheChronos(scores):
    chronos = {}

    # Calculer la durée totale de jeu pour chaque joueur
    for joueur, infos in scores.items():
        duree_totale = sum(duree for _, duree in infos)
        chronos[joueur] = duree_totale

    # Afficher le classement par durée de jeu
    print("Classement par durée de jeu :")
    print("Joueur\t\tDurée totale de jeu")

    for joueur, duree in sorted(chronos.items(), key=lambda x: x[1]):
        print(f"{joueur}\t\t{duree} secondes")
"""
# Exemple d'utilisation
scores_exemple_chronos = {
    "Joueur1": [(3, 20), (4, 30)],
    "Joueur2": [(3, 18), (4, 25)],
    "Joueur3": [(3, 22), (5, 40)],
}

# Affichage du classement par durée de jeu
afficheChronos(scores_exemple_chronos)
"""

#Q6


def reflexionMoy(scores, nom_joueur):
    if nom_joueur not in scores or not scores[nom_joueur]:
        print(f"Aucune partie enregistrée pour le joueur {nom_joueur}.")
        return None

    total_coups = 0

    # Récupérer les informations de toutes les parties gagnées par le joueur
    parties_joueur = scores[nom_joueur]

    for _, nb_coups in parties_joueur:
        total_coups += nb_coups

    temps_moyen_par_coup = total_coups / len(parties_joueur)  # Utilisation de len(parties_joueur) au lieu de total_coups

    print(f"Temps moyen de réflexion par coup pour {nom_joueur} : {temps_moyen_par_coup:.2f} unités de temps par coup.")
    
    return temps_moyen_par_coup
"""
# Exemple pour le test.
scores_exemple_reflexion = {
    "Joueur1": [(3, 20), (4, 30)],
    "Joueur2": [(3, 18), (4, 25)],
    "Joueur3": [(3, 22), (5, 40)],
}

# Calcule et affichage du temps moyen de réflexion par coup pour un joueur spécifique
reflexionMoy(scores_exemple_reflexion, "Joueur1")
"""


#Q7


def classementJoueursRapides(scores):
    classement = []

    for joueur, parties in scores.items():
        total_temps = 0
        total_coups = 0

        for nb_disques, nb_coups in parties:
            total_temps += nb_coups  # Utilisation du nombre de coups comme indicateur de temps
            total_coups += nb_coups

        temps_moyen_par_coup = total_temps / total_coups

        classement.append((joueur, temps_moyen_par_coup))

    # Tri du classement en fonction du temps moyen par coup (plus rapide en premier)
    classement = sorted(classement, key=lambda x: x[1])

    # Affichage du classement
    print("Classement des joueurs les plus rapides (moins de réflexion par coup):")
    for i, (joueur, temps_moyen) in enumerate(classement, start=1):
        print(f"{i}. {joueur} - Temps moyen par coup : {temps_moyen:.2f} unités de temps par coup")
"""
# Exemple pour le test.
scores_exemple_classement = {
    "Joueur1": [(3, 20), (4, 30)],
    "Joueur2": [(3, 18), (4, 25)],
    "Joueur3": [(3, 22), (5, 40)],
}

# Affichage du classement des joueurs les plus rapides
classementJoueursRapides(scores_exemple_classement)
"""
 
#Q8

def menuPrincipal():
    scores = {}
    couleurs_disques = ["red", "green", "blue", "purple", "orange"]
    epaisseur_tour = 10
    taille_disque = 30
    ecart_tours = 50

    while True:
        plateau_initial = init(3)
        n = len(plateau_initial)

        print("\n" + Fore.YELLOW + "Menu Principal:" + Style.RESET_ALL)
        print("1. " + Fore.CYAN + "Jouer une partie" + Style.RESET_ALL)
        print("2. " + Fore.CYAN + "Afficher les scores" + Style.RESET_ALL)
        print("3. " + Fore.CYAN + "Afficher les chronos" + Style.RESET_ALL)
        print("4. " + Fore.CYAN + "Afficher le classement des joueurs rapides" + Style.RESET_ALL)
        print("5. " + Fore.RED + "Quitter" + Style.RESET_ALL)

        choix = input(Fore.YELLOW + "Choisissez une option (1-5): " + Style.RESET_ALL)

        if choix == '1':
            try:
                limite_coups = int(input("Entrez le nombre maximal de coups autorisés (0 pour illimité): "))
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            partie_gagnee, victoire = boucleJeuAvecAnnulationEtScore(plateau_initial, n, couleurs_disques,
                                                                      epaisseur_tour, taille_disque, ecart_tours,
                                                                      limite_coups, scores)
            if partie_gagnee and victoire:
                print(Fore.GREEN + "Partie enregistrée dans les scores." + Style.RESET_ALL)

        elif choix == '2':
            afficheScores(scores)

        elif choix == '3':
            afficheChronos(scores)

        elif choix == '4':
            classementJoueursRapides(scores)

        elif choix == '5':
            print(Fore.RED + "Merci d'avoir joué! Au revoir." + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "Option invalide. Veuillez choisir une option entre 1 et 5." + Style.RESET_ALL)

# Exemple d'utilisation
menuPrincipal()
