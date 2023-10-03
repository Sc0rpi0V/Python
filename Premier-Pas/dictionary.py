
'Création de dictionnaire'
nouvelle_campagne = {
    "responsable_de_campagne": "Jeanne d'Arc",
    "nom_de_campagne": "Campagne nous aimons les chiens",
    "date_de_début": "01/01/2020",
    "influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}

taux_de_conversion = {}
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2

'Accès à une valeur dans dictionnaire'
print(nouvelle_campagne['responsable_de_campagne'])
print(taux_de_conversion['facebook'])

'Ajout paire clé-valeur'
infos_labradoodle = {
    "poids": "13 à 16 kg",
    "origine": "États-Unis"
}
infos_labradoodle['nom_scientifique'] = "Canis lupus familiaris"
print(infos_labradoodle)

'Suppression paire clé-valeur : del ou pop'
'Vérification clé spécifique : in'