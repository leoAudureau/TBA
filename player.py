# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history= []
    
    # Define the move method.
    

    def move(self, direction):
        # Récupérer la salle suivante à partir des sorties de la salle actuelle.
        next_room = self.current_room.exits.get(direction)

        # Si aucune salle n'est trouvée dans cette direction, afficher un message d'erreur et retourner False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Ajouter la salle actuelle à l'historique si elle n'y est pas déjà.
        if self.current_room.name not in self.history:
            self.history.append(self.current_room.name)

        # Déplacer le joueur dans la salle suivante.
        self.current_room = next_room

        # Afficher la description complète de la nouvelle salle.
        print(self.current_room.get_long_description())

        # Afficher l'historique après la mise à jour.
        print(self.get_history())

        return True


    def get_history(self):
        if not self.history:
            return "Vous n'avez encore visité aucune pièce."
        
        # Construction de la chaîne d'affichage des pièces visitées
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        for room in self.history:
            history_str += f"    - {room}\n"
        return history_str

