'Condition if/else'
ensoleille = True
if ensoleille:
    print("on va à la plage !")
else:
    print("on reste à la maison !")

'Condition alternatives elif'
ensoleille = False
neige = True
if ensoleille:
    print("on va à la plage !")
elif neige:
    print("on fait un bonhomme de neige")
else:
    print("on reste à la maison !")

'Condition mutiples avec opérateurs logiques'
avec_soleil = True
en_semaine = False
if avec_soleil and not en_semaine:
    print("on va à la plage !")
elif avec_soleil and en_semaine:
    print("on va au travail !")
else:
    print("on reste à la maison !")

'Condition complexes avec expressions comparatives'
nombre_de_sieges = 30
nombre_dinvites = 25

if nombre_dinvites < nombre_de_sieges:
    print("autoriser plus d’invités")
else:
    print("ne pas autoriser plus d’invités")

'Boucle For'
races_de_chien = ["golden retriever", "chihuahua", "terrier", "carlin"]
for chien in races_de_chien:
    print(chien)

'Fonctionnement for'
for x in range(5):
    print(x, 'range')

'Boucle While'
capacite_maximale = 10
capacite_actuelle = 3
while capacite_actuelle < capacite_maximale:
    capacite_actuelle += 1
    print(capacite_actuelle)

'Utilisation break et continue'
for i in range(10):
    if i == 5:
        break
    print(i)

    liste = [1, 2, 3, 4, 5]
# Boucle for sur la liste
for element in liste:
    if element == 3:
        # Si l'élément vaut 3, on passe à l'itération suivante sans exécuter le reste du code
        continue
    # Dans tous les autres cas, on exécute le reste du code
    print(element)