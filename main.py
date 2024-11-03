import random

#Liste de mots
liste_mot = ["SAUCE", "POMME", "LISTE", "WEISS", "ORDRE"]

#Définition des variables et listes
liste_joueur = []
mot_joueur= ""
mot_secret= ""

#Choix aléatoire du mot secret
def mot_random(liste_mot):
  return random.choice(liste_mot)

#L'attribution du mot aléatoire à la variable mot_secret
mot_secret = mot_random(liste_mot)

#Le joueur entre un mot de 5 lettres qu'on attribue à la variable mot_joueur 
def input_mot():
  mot_joueur = input("Entrer un mot de 5 lettres: ").upper()
  return mot_joueur 

#Vérification de la longueur du mot choisi par le joueur et redemande d'un mot si le mot
#choisi n'est pas de 5 lettres
def verification_mot(mot_joueur):
  mot_faux = True
  while mot_faux:
    if len(mot_joueur) != 5:
      print("Le mot doit contenir 5 lettres")
      mot_joueur = input_mot()
    else: 
      mot_faux = False
  return mot_joueur

#Attribution des couleurs au lettres du mot choisi par le joueur qui sont ensuite 
#stockées dans la variable réponse qu'on affiche à l'écran
def affichage(mot_joueur, mot_secret):
  reponse = ""
  for i in range(5):
    if mot_joueur[i] == mot_secret[i]:
      reponse += f"{mot_joueur[i]} (vert) "
    elif mot_joueur[i] in mot_secret:
      reponse += f"{mot_joueur[i]} (jaune) "
    else: 
      reponse += f"{mot_joueur[i]} (gris) "
  liste_joueur.append(reponse)
  print(reponse) 

#Vérification et annonce de victoire quand le bon mot est trouvé
def victoire(mot_joueur, mot_secret):
  if mot_joueur == mot_secret:
    print("Vous avez gagné!")
    return True
  return False
  
# Boucle principale du jeu qui permet de faire des essais, suit le nombre d'essais, et 
# détermine si le jeu est fini ou non
def boucle_de_jeu():
  essais = 0
  while essais < 6:
    mot_joueur = input_mot()
    mot_joueur = verification_mot(mot_joueur)
    affichage(mot_joueur, mot_secret)
    if victoire(mot_joueur, mot_secret):
      return
    essais += 1
    print(f"Vous avez {6-essais} essais restants")
  print(f"Vous avez perdu! Le mot était: {mot_secret}")

boucle_de_jeu()
