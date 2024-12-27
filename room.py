# Define the Room class.


class Room:


    # Define the constructor.
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.character = {}
   
    # Define the get_exit method.
    def get_exit(self, direction):


        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
   
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: "
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string


    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"




    def add_item(self, item):
        """
        Ajoute un item à l'inventaire de la salle.
       
        :param item: Item, l'objet à ajouter
        """
        if item.name in self.inventory:
            print(f"L'objet '{item.name}' est déjà dans cette salle.")
        else:
            self.inventory[item.name] = item
            print(f"'{item.name}' a été ajouté à la salle '{self.name}'.")


    def remove_item(self, item_name):
        """
        Supprime un item de l'inventaire de la salle.
       
        :param item_name: str, le nom de l'objet à supprimer
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"'{item_name}' a été retiré de la salle '{self.name}'.")
        else:
            print(f"L'objet '{item_name}' n'est pas présent dans cette salle.")


    def get_inventory(self):
        """
        Retourne une chaîne de caractères décrivant le contenu de la pièce,
        y compris les items et les personnages non joueurs présents.
        """
        result = f"La salle '{self.name}' contient :\n"

        # Ajouter les items à l'inventaire
        if not self.inventory:
            result += "    Aucun item.\n"
        else:
            result += "    Items :\n"
            for name, item in self.inventory.items():
                result += f"        - {name} : {item.description} ({item.weight} kg)\n"

        # Ajouter les personnages à l'affichage
        if not self.characters:
            result += "    Aucun personnage.\n"
        else:
            result += "    Personnages :\n"
            for name, character in self.characters.items():
                result += f"        - {name} : {character.description}\n"

        return result

        
        

