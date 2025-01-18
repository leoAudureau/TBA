# actions.py
"""
Description: The actions module.

The actions module contains the functions that are called when a command is executed.
Each function takes 3 parameters:
- game: the game object  
- list_of_words: the list of words in the command  
- number_of_parameters: the number of parameters expected by the command

The functions return True if the command was executed successfully, False otherwise.
The functions print an error message if the number of parameters is incorrect.
The error message is different depending on the number of parameters expected by the command.
"""
# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """Class containing all the actions available in the game."""

    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Get the direction from the list of words.
        direction = list_of_words[1]

        # Move the player in the direction specified by the parameter.
        d = {
            "N": "N", "nord": "N", "NORD": "N", "n": "N",
            "O": "O", "ouest": "O", "OUEST": "O", "o": "O",
            "E": "E", "est": "E", "EST": "E", "e": "E",
            "S": "S", "sud": "S", "SUD": "S", "s": "S",
            "U": "U", "haut": "U", "HAUT": "U", "h": "U", "up": "U", "UP": "U", "u": "U",
            "D": "D", "bas": "D", "BAS": "D", "b": "D", "down": "D", "DOWN": "D", "d": "D"
        }
        if direction in d:
            player.move(d[direction], game)
        else:
            print("Vous devez renseigner une direction valide.")
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles :")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Go back to the previous room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"Commande '{command_word}' invalide. Utilisez la commande correctement. Si besoin utilisez la fonction help.")
            return False

        player = game.player

        # Check if the history contains enough rooms to go back
        if len(player.history) < 1:
            print("\nIl n'y a pas de salle précédente à laquelle revenir.\n")
            return False

        # Get the previous room from the history (the last room visited)
        previous_room_name = player.history[-1]  # The last room in the history

        # Look for the Room object corresponding to the name of the previous room
        previous_room = next((room for room in game.rooms if room.name == previous_room_name), None)

        # Check if the previous room exists
        if not previous_room:
            print("\nErreur : La salle précédente est introuvable dans le jeu.\n")
            return False

        # Move the player to the previous room
        player.current_room = previous_room

        # Remove the current room from the history (before moving)
        player.history.pop()

        # Display the appropriate message and the updated history
        print(f"\nVous êtes revenu(e) dans {previous_room.get_long_description()}.\n")
        print(player.get_history())  # Show the updated history

        return True

    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """Look around the current room."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        current_room = game.player.current_room
        print(current_room.get_inventory())  # Show items and NPCs

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Take an item from the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        current_room = game.player.current_room

        if len(list_of_words) < 2:
            print("Vous devez spécifier quel objet prendre.")
            return

        # Get the name of the item the player wants to take
        item_name = list_of_words[1]

        # Check if the current room's inventory is empty
        if not current_room.inventory:
            print("Il n'y a pas d'objet à prendre ici.")
            return

        # Search for the item in the room's inventory
        if item_name in current_room.inventory:
            item = current_room.inventory[item_name]

            if game.player.can_carry(item):
                game.player.add_item_to_inventory(item)
                del current_room.inventory[item_name]

            else:
                print(f"Vous ne pouvez pas porter '{item.name}', votre sac devient trop lourd pour vous...")

        else:
            # If the item is not found
            print(f"L'objet '{item_name}' n'est pas présent dans cette pièce.")

    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Drop an item from the player's inventory into the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        current_room = game.player.current_room

        if len(list_of_words) < 2:
            print("Vous devez spécifier quel objet déposer.")
            return

        # Get the name of the item the player wants to drop
        item_name = list_of_words[1]

        # Check if the item is in the player's inventory
        if item_name not in game.player.inventory:
            print(f"L'objet '{item_name}' n'est pas dans votre inventaire.")
            return

        # Move the item from the player's inventory to the room's inventory
        item = game.player.inventory.pop(item_name)
        current_room.inventory[item_name] = item
        print(f"Vous avez déposé {item_name}.")

    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """Check the player's inventory."""
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player

        if player.inventory:
            print("Vous avez actuellement :")
            for item in player.inventory:
                if isinstance(item, str):  # If the item is a string
                    print(f"    - {item}")
                else:  # If the item is an object with attributes
                    print(f"    - {item.name} : {item.description} ({item.weight} kg)")
        else:
            print("Votre inventaire est vide.")

    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Talk to a character in the current room.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        current_room = game.player.current_room

        if len(list_of_words) < 2:
            print("Vous devez spécifier avec qui parler.")
            return

        # Get the name of the character specified by the user
        character_name = list_of_words[1].lower()  # Convert to lowercase

        # Search for the character in the dictionary
        character = current_room.character.get(character_name)
        if not character:
            print(f"{character_name.capitalize()} n'est pas ici.")
            return

        # Special condition for Elon
        elif character_name == "elon" and "cartes" in game.player.inventory:
            print("Elon : Aaah finally something interesting to do in this station!")

        # Victory condition
        elif character_name == "eduardo" and "combinaison" in game.player.inventory and "bounty" in game.player.inventory:
            print("Eduardo : Parfait ! Donne moi cette barre chocolatée et je te ramène sur Terre.")
            game.finished = True

        # Defeat condition
        elif character_name == "bruno" and "fiole" in game.player.inventory:
            print("Bruno : Attention ne fait pas tomber cette fiole ! \n \nVous avez fait tomber la fiole... Malheureusement le vaisseau vient d'exploser, Fredo aimait un peu trop les liquides explosifs.")
            game.finished = True

        else:
            # If conditions are not met, then normal message
            print(character.get_msg())
