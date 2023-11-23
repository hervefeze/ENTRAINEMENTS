# Ce fichier utilise les fonctions créées par herve et effectue des opérations

# Le fichier operations.py n'esiste pas encore, mais il sera disponible plus tard
import operations # cette ligne permet d'utiliser les fonctions contenues dans le fichier operations.py

def main():
    print("Quelle opération voulez-vous effectuer ?")
    print("Entrez 1 pour l'addition")
    print("Entrez 2 pour la soustraction")
    print("Entrez 3 pour la multiplication")
    print("Entrez 4 pour la division")
    print()
    choix = int(input())
    if choix == 1:
        print("Entrez le premier nombre")
        nb1 = int(input())
        print("Entrez le deuxième nombre")
        nb2 = int(input())
        resultat = operations.addition(nb1, nb2)
        print("L'addition de", nb1, "et", nb2, "vaut", resultat)
    if choix == 2:
        print("Entrez le premier nombre")
        nb1 = int(input())
        print("Entrez le deuxième nombre")
        nb2 = int(input())
        resultat = operations.soustraction(nb1, nb2)
        print("La soustraction de", nb1, "dans", nb2, "vaut", resultat)
    if choix == 3:
        print("Entrez le premier nombre")
        nb1 = int(input())
        print("Entrez le deuxième nombre")
        nb2 = int(input())
        resultat = operations.multiplication(nb1, nb2)
        print("La multiplication de", nb1, "par", nb2, "vaut", resultat)
    if choix == 4:
        print("Entrez le premier nombre")
        nb1 = int(input())
        print("Entrez le deuxième nombre")
        nb2 = int(input())
        resultat = operations.division(nb1, nb2)
        print("La division de", nb1, "par", nb2, "vaut", resultat)
if __name__ == "__main__":
    main()

