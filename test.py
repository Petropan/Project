import csv
import os

# Fonction pour charger tous les fichiers CSV d'un dossier donné
def load_data(folder):
    data = []  # Liste contenant toutes les lignes des fichiers CSV

    # On parcourt tous les fichiers dans le dossier spécifié
    for file_name in os.listdir(folder):
        # Vérifier si le fichier se termine par ".csv"
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder, file_name)  # On crée le chemin complet vers le fichier
            
            # Ouvrir le fichier CSV en mode lecture
            with open(file_path, mode="r", newline='', encoding="utf-8") as file:
                reader = csv.DictReader(file)  # Utiliser DictReader pour lire le fichier sous forme de dictionnaire
                data.extend(list(reader))  # Ajouter toutes les lignes du fichier CSV à la liste data
    return data  # Retourne la liste des données



# Fonction pour afficher la liste des immeubles triés
def display_buildings(data):
    # Tri des données par numéro d'immeuble (building_id) puis par nom de famille du propriétaire (lastname)
    sorted_data = sorted(data, key=lambda x: (x['building_id'], x['lastname']))
    
    # Affichage des en-têtes de colonnes pour la table
    print(f"{'Property':<20}{'Building ID':<15}{'Owner Name':<30}{'Street':<30}{'City':<20}{'Zip':<10}")
    print("=" * 125)  # Ligne de séparation
    
    # Parcours de chaque ligne de données triées pour les afficher
    for row in sorted_data:
        owner_name = f"{row['firstname']} {row['lastname']}"
        # Affichage des données formatées pour chaque immeuble
        print(f"{row['property']:<20}{row['building_id']:<15}{owner_name:<30}{row['street1']:<30}{row['city']:<20}{row['zip']:<10}")
    
    print("=" * 125)  # Ligne de séparation à la fin de l'affichage



# Fonction pour rechercher dans une colonne spécifique
def search_data(data, column, value):
    # Utilisation d'une compréhension de liste pour filtrer les lignes dont la valeur de 'column' correspond à 'value'
    result = [row for row in data if row[column].lower() == value.lower()]
    
    # Affichage des résultats
    if result:
        display_buildings(result)
    else:
        print("Aucun résultat trouvé.")  # Message si aucun résultat ne correspond à la recherche



# Fonction principale qui gère l'interaction avec l'utilisateur
def main():
    folder = "data"  # Chemin vers le dossier contenant les fichiers CSV
    data = load_data(folder)  # Chargement de toutes les données à partir des fichiers CSV dans le dossier
    
    # Boucle principale pour afficher le menu et interagir avec l'utilisateur
    while True:
        # Affichage du menu
        print("\nMenu:")
        print("1. Afficher les immeubles")
        print("2. Rechercher")
        print("3. Quitter")
        choice = input("Choisissez une option (1/2/3): ")

        if choice == "1":
            display_buildings(data)  # Appel à la fonction pour afficher les immeubles si l'utilisateur choisit "1"
        elif choice == "2":
            column = input("Sur quelle colonne voulez-vous rechercher (ex: email) ?: ")
            # Si la colonne saisie n'est pas valide (pas dans les clés du dictionnaire), afficher un message d'erreur
            if column not in data[0]:
                print(f"Colonne invalide. Les colonnes valides sont: {', '.join(data[0].keys())}")
                continue  # Retourne au menu principal
            value = input(f"Entrez la valeur à rechercher pour la colonne {column}: ")
            search_data(data, column, value)  # Appel à la fonction de recherche avec la colonne et la valeur spécifiées
        elif choice == "3":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")



main()