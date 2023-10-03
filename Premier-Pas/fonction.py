def afficher_message():
    print("Bonjour, comment ça va ?")

afficher_message()

def afficher_nom_prenom(nom, prenom):
    print("Nom :", nom)
    print("Prénom :", prenom)

afficher_nom_prenom("Dupont", "Jean")

def calculer_somme(a, b):
  resultat = a + b
  return resultat

somme = calculer_somme(2, 3)
print(somme) #Ce print affichera 5

premiere_campagne = {
    'visiteurs': 1000,
    'conversions': 50
}

seconde_campagne = {
    'visiteurs': 1500,
    'conversions': 75
}

troisieme_campagne = {
    'visiteurs': 800,
    'conversions': 40
}

def calculer_taux_de_conversion(campagne):
    taux_de_conversion = campagne['visiteurs'] / campagne['conversions']
    return taux_de_conversion

resultat_premiere_campagne = calculer_taux_de_conversion(premiere_campagne)
resultat_seconde_campagne = calculer_taux_de_conversion(seconde_campagne)
resultat_troisieme_campagne = calculer_taux_de_conversion(troisieme_campagne)

print("Taux de conversion première campagne :", resultat_premiere_campagne)
print("Taux de conversion seconde campagne :", resultat_seconde_campagne)
print("Taux de conversion troisième campagne :", resultat_troisieme_campagne)

def somme(a, b):
    """
    Cette fonction calcule la somme de deux nombres et retourne le résultat.

    Parameters:
    a (int): le premier nombre
    b (int): le deuxième nombre

    Returns:
    int: la somme de a et b
    """
    return a + b

help(somme)

while True:
    try:
        x = int(input("Entrez un nombre entier : "))
        break
    except ValueError:
        print("Oops ! Ce n'est pas un nombre entier. Essayez encore...")