# Define the Player class.
class Player():



    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 30.1  # Poids maximal que le joueur peut porter



    def get_total_weight(self):
        return sum(item.weight for item in self.inventory.values())


    def can_carry(self, item):
        return self.get_total_weight() + item.weight <= self.max_weight

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




    def get_inventory(self):
        """
        Retourne une chaîne de caractères décrivant le contenu de l'inventaire.
        """
        if not self.inventory:
            return "Votre inventaire est vide."
       
        inventory_str = "Vous disposez des items suivants :\n"
        for name, item in self.inventory.items():
            inventory_str += f"    - {name} : {item.description} ({item.weight} kg)\n"


        return inventory_str


        
   
    def add_item_to_inventory(self, item):
        """
        Ajoute un item à l'inventaire du joueur.
           
        :param item: Item, l'objet à ajouter
        """
        if item.name in self.inventory:
            print(f"L'objet '{item.name}' est déjà dans votre inventaire.")
        elif not self.can_carry(item):
            print(f"Vous ne pouvez pas porter '{item.name}' car il est trop lourd.")
        else:
            self.inventory[item.name] = item
            print(f"'{item.name}' a été ajouté à votre inventaire.")



    def remove_item_from_inventory(self, item_name):
        """
        Supprime un item de l'inventaire du joueur.
       
        :param item_name: str, le nom de l'objet à supprimer
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"'{item_name}' a été retiré de votre inventaire.")

        else:

            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")