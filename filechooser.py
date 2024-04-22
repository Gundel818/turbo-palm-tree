import os

class FileChooser:
    def __init__(self) -> None:
        pass

    def choosingFile(self) -> str :
        dir = os.getcwd() + "/input"
        files = {}
        for i, file in enumerate(os.listdir(dir), start=1):
            if file.endswith('.csv'):
                files[i] = file
                print(f"{i}. {file}")

        # Demander à l'utilisateur de saisir le numéro du fichier désiré
        num_fichier_cells = int(input("Entrez le numéro du fichier que vous souhaitez sélectionner ou entrez 0 pour quitter: "))
        
        if num_fichier_cells == 0:
            exit(0)
        
        # Vérifier si le numéro de fichier est valide
        if num_fichier_cells in files:
            filename = files[num_fichier_cells]
            print("Vous avez sélectionné le fichier :", filename)
            
        else:
            print("Numéro de fichier invalide.")
            exit(1)
        return os.path.join(dir, filename)
