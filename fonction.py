def afficher_message():
    print("Bonjour comment ça va ?")

afficher_message()

def afficher_nom_prenom(nom,prenom):
    print("Nom : ", nom)
    print("Prenom : ", prenom)

afficher_nom_prenom("Dupont","Jean")

def calculer_somme(a,b):
    resultat = a + b
    return resultat

somme = calculer_somme(12,14)
print(somme)

