# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:

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

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

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
            "U": "U", "haut": "U", "HAUT": "U", "h": "U", "up" : "U", "UP" : "U", 
            "D": "D", "bas": "D", "BAS": "D", "b": "D" , "down" : "D", "DOWN" : "D"
        }
        if direction in d:
            player.move(d[direction])
        else:
            print("vous devez renseigner une direction valide")
        return True
    
    
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

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

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    
    def back(game, list_of_words, number_of_parameters):
        # Vérifier si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(f"Commande '{command_word}' invalide. Utilisez la commande correctement.")
            return False

        # Retirer la salle actuelle de l'historique
        self.history.pop()  
        # La salle précédente devient la salle actuelle
        previous_room_name = self.history[-1]
        previous_room = next((room for room in self.game.rooms if room.name == previous_room_name), None)

        # Vérifier si l'historique contient assez de salles pour un retour
        if len(player.history) < 1:
            print("\nIl n'y a pas de salle précédente à laquelle revenir.\n")
            return False

        # Récupérer la salle précédente dans l'historique (la dernière salle visitée)
        previous_room_name = player.history[-1]  # La dernière salle dans l'historique

        # Rechercher l'objet Room correspondant au nom de la salle précédente
        previous_room = next((room for room in game.rooms if room.name == previous_room_name), None)

        # Vérifier si la salle précédente existe
        if not previous_room:
            print("\nErreur : La salle précédente est introuvable dans le jeu.\n")
            return False

        # Déplacer le joueur dans la salle précédente
        player.current_room = previous_room

        # Supprimer la salle actuelle de l'historique (avant de se déplacer)
        player.history.pop()

        # Afficher le message approprié et l'historique mis à jour
        print(f"\nVous êtes revenu(e) dans {previous_room.get_long_description()}.\n")
        print(player.get_history())  # Afficher l'historique mis à jour

        return True



        def back(game, list_of_words, number_of_parameters):
            """
            Commande pour revenir à la salle précédente dans le jeu.

            Args:
                game (Game): L'objet du jeu.
                list_of_words (list): La liste des mots dans la commande.
                number_of_parameters (int): Le nombre de paramètres attendu par la commande.

            Returns:
                bool: True si le retour en arrière a été effectué, False sinon.
            """
            player = game.player
            l = len(list_of_words)

            # Vérifier le nombre correct de paramètres
            if l != number_of_parameters + 1:
                command_word = list_of_words[0]
                print(MSG0.format(command_word=command_word))
                return False

            # Tenter de revenir en arrière avec la méthode moveback
            success = player.moveback()

            if not success:
                print("Impossible de revenir en arrière.")
                return False

            return True