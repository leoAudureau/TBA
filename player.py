"""Module player: Implements the Player class for a text-based adventure game."""

class Player:
    """Represents a player in a text-based adventure game."""

    def __init__(self, name):
        """
        Initialize a Player instance.

        :param name: str, the name of the player
        """
        self.name = name
        self.current_room = None
        self.history = []
        self.inventory = {}
        self.max_weight = 30.1  # Maximum weight the player can carry

    def get_total_weight(self):
        """
        Calculate the total weight of items in the player's inventory.

        :return: float, total weight of items
        """
        return sum(item.weight for item in self.inventory.values())

    def can_carry(self, item):
        """
        Check if the player can carry an item without exceeding max weight.

        :param item: Item, the item to check
        :return: bool, True if the player can carry the item, False otherwise
        """
        return self.get_total_weight() + item.weight <= self.max_weight

    def move(self, direction, game):
        """
        Move the player in the specified direction if possible.

        :param direction: str, the direction to move
        :param game: Game, the current game instance
        :return: bool, True if the move was successful, False otherwise
        """
        next_room = self.current_room.exits.get(direction)

        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        if self.current_room.name not in self.history:
            self.history.append(self.current_room.name)

        for room in game.rooms:
            if "eduardo" in room.character:
                room.character["eduardo"].move_to_random_room(game)

        self.current_room = next_room
        print(self.current_room.get_long_description())
        return True

    def get_history(self):
        """
        Retrieve the history of rooms visited by the player.

        :return: str, description of visited rooms
        """
        if not self.history:
            return "Vous n'avez encore visité aucune pièce."

        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        history_str += "\n".join(f"    - {room}" for room in self.history)
        return history_str

    def get_inventory(self):
        """
        Retrieve a description of the player's inventory.

        :return: str, inventory description
        """
        if not self.inventory:
            return "Votre inventaire est vide."

        inventory_str = "Vous disposez des items suivants :\n"
        for name, item in self.inventory.items():
            inventory_str += f"    - {name} : {item.description} ({item.weight} kg)\n"

        return inventory_str

    def add_item_to_inventory(self, item):
        """
        Add an item to the player's inventory if possible.

        :param item: Item, the object to add
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
        Remove an item from the player's inventory.

        :param item_name: str, the name of the object to remove
        """
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"'{item_name}' a été retiré de votre inventaire.")
        else:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
