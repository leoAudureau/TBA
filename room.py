"""Module room: Implements the Room class for a text-based adventure game."""

class Room:
    """Represents a room in a text-based adventure game."""

    def __init__(self, name, description):
        """
        Initialize a Room instance.

        :param name: str, the name of the room
        :param description: str, a description of the room
        """
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = {}
        self.character = {}

    def get_exit(self, direction):
        """
        Retrieve the room in the given direction if it exists.

        :param direction: str, the direction to check
        :return: Room or None
        """
        return self.exits.get(direction)

    def get_exit_string(self):
        """
        Generate a string describing the room's exits.

        :return: str, exits description
        """
        exit_string = "Sorties: "
        for key in self.exits:
            if self.exits[key] is not None:
                exit_string += key + ", "
        return exit_string.strip(", ")

    def get_long_description(self):
        """
        Generate a long description of the room including its exits.

        :return: str, room description
        """
        return f"\nVous êtes dans {self.description}\n\n{self.get_exit_string()}\n"

    def add_item(self, item):
        """
        Add an item to the room's inventory.

        :param item: Item, the object to add
        """
        if item.name in self.inventory:
            print(f"L'objet '{item.name}' est déjà dans cette salle.")
        else:
            self.inventory[item.name] = item
            print(f"'{item.name}' a été ajouté à la salle '{self.name}'.")

    def remove_item(self, item_name):
        """
        Remove an item from the room's inventory.

        :param item_name: str, the name of the object to remove
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"'{item_name}' a été retiré de la salle '{self.name}'.")
        else:
            print(f"L'objet '{item_name}' n'est pas présent dans cette salle.")

    def get_inventory(self):
        """
        Generate a string describing the contents of the room.

        :return: str, inventory description
        """
        inventory_str = ""

        if self.inventory:
            inventory_str += "Les objets présents dans cette pièce sont :\n"
            for item in self.inventory.values():
                inventory_str += (
                    f"    - {item.name} : {item.description} ({item.weight} kg)\n"
                )

        if self.character:
            inventory_str += "Les personnages présents dans cette pièce sont :\n"
            for character in self.character.values():
                inventory_str += (
                    f"    - {character.name} : {character.description}\n"
                )

        return inventory_str or "Cette pièce est vide."
