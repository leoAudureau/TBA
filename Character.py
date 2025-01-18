# Character.py
"""
This module contains the Character class.
"""
import random

class Character:
    """ 
    This class represents a character in the game. 
    Each character has a name, a description, and a set of messages to display.
    """

    # Define the constructor.
    def __init__(self, name, description, msgs):
        self.name = name
        self.description = description
        self.msgs = msgs[:]  # Copie de la liste pour éviter des modifications globales
        self._original_msgs = msgs[:]  # Sauvegarde des messages originaux
        self.move_counter = 0  # Compteur de déplacements (pour Eduardo)

    def __str__(self):
        """Returns the string representation of the character."""
        return f"{self.name} : {self.description}"

    def get_msg(self):
        """Displays a cyclic message from the character."""
        if not self.msgs:  # If all messages have been used
            self.msgs = self._original_msgs[:]  # Resets the message list
        return self.msgs.pop(0)

    def move_to_random_room(self, game):
        """
        Moves the character to a specific room every second time.
        """
        self.move_counter += 1
        if self.move_counter % 2 == 0:
            new_room_name = random.choice(["poste_de_commandes", "salle_commune"])
            new_room = next((room for room in game.rooms if room.name == new_room_name), None)
            if new_room:
                # Remove character from the current room
                for room in game.rooms:
                    if self.name.lower() in room.character:
                        del room.character[self.name.lower()]
                # Add character to the new room
                new_room.character[self.name.lower()] = self
                print(f"{self.name} vient de se déplacer vers : {new_room.name}")
