from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from Character import Character

"""
Module principal du jeu d'aventure textuel.
Ce module configure et exécute un jeu d'exploration où le joueur interagit
avec des salles, des objets, et des PNJ.
"""

class Game:
    """
    Classe représentant le jeu d'aventure avec les commandes et les salles.
    """

    def __init__(self):
        """
        Initialisation du jeu avec les différentes commandes et salles.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None

    def setup(self):
        """Configure le jeu avec les salles et les commandes."""
        self._setup_commands()
        self._setup_rooms()
        self._setup_items_and_characters()

        # Configuration du joueur
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = self.rooms[0]  # Sas de décompression

    def _setup_commands(self):
        """Initialise les commandes disponibles dans le jeu."""
        self.commands = {
            "help": Command("help", " : afficher cette aide", Actions.help, 0),
            "quit": Command("quit", " : quitter le jeu", Actions.quit, 0),
            "go": Command("go", " <direction> : se déplacer", Actions.go, 1),
            "back": Command("back", " : revenir en arrière", Actions.back, 0),
            "look": Command("look", " : examiner la salle actuelle", Actions.look, 0),
            "take": Command("take", " prendre l'objet voulu", Actions.take, 1),
            "drop": Command("drop", " déposer l'objet voulu", Actions.drop, 1),
            "check": Command("check", " regarder l'inventaire", Actions.check, 0),
            "talk": Command("talk", " parler avec un PNJ", Actions.talk, 1),
        }

    def _setup_rooms(self):
        """Crée et configure les salles du jeu."""
        self.rooms = [
            Room(
                "Sas de décompression",
                "Arrivés dans la station spatiale, vous êtes dans le sas de décompression."
            ),
            Room(
                "hall1",
                "Le Hall 1 permet d'accéder à des salles importantes du vaisseau."
            ),
            Room(
                "hall2",
                "Le Hall 2 donne accès à des pièces vitales pour les expériences."
            ),
            Room("hall3", "Le Hall 3 vous mène à la nourriture."),
            Room(
                "salle_commune",
                "La salle commune, lieu de restauration et de détente."
            ),
            Room(
                "module d'amarage",
                "Le module d'amarage, pour accueillir des amis ou des pirates de l'espace."
            ),
            Room(
                "poste de commande",
                "Le poste de commande, pour gérer les systèmes et les voyages intergalactiques."
            ),
            Room("reserve", "La réserve du vaisseau pour stocker la nourriture."),
            Room("labo2", "Le deuxième laboratoire, celui de Fredo."),
            Room("labo1", "Le premier laboratoire, faites attention à Bruno."),
            Room("serre", "La serre pour faire pousser de tout."),
        ]

        # Configuration des sorties entre salles
        self.rooms[0].exits = {"N": self.rooms[2]}
        self.rooms[2].exits = {
            "N": self.rooms[9], "S": self.rooms[0], "O": self.rooms[4]
        }
        self.rooms[9].exits = {"S": self.rooms[2], "U": self.rooms[8]}
        self.rooms[4].exits = {"E": self.rooms[2], "O": self.rooms[1]}
        self.rooms[1].exits = {
            "N": self.rooms[5], "O": self.rooms[6], "D": self.rooms[3]
        }
        self.rooms[6].exits = {"E": self.rooms[1]}
        self.rooms[5].exits = {"S": self.rooms[1]}
        self.rooms[8].exits = {"D": self.rooms[9]}
        self.rooms[3].exits = {
            "N": self.rooms[7], "O": self.rooms[10], "U": self.rooms[1]
        }
        self.rooms[10].exits = {"E": self.rooms[3]}
        self.rooms[7].exits = {"S": self.rooms[3]}

    def _setup_items_and_characters(self):
        """Ajoute des objets et des personnages aux salles."""
        items = {
            "eau": Item("eau", "à boire", 1),
            "salade": Item("salade", "bien verte", 0.1),
            "combinaison": Item("combinaison", "pour sortir du véhicule", 30),
            "fiole": Item("fiole", "liquide violet suspect", 0.5),
            "cartes": Item("cartes", "pour jouer", 1),
            "bounty": Item("bounty", "à manger", 0.1),
        }

        self.rooms[2].inventory = {"eau": items["eau"]}
        self.rooms[6].inventory = {"eau": items["eau"]}
        self.rooms[10].inventory = {"salade": items["salade"]}
        self.rooms[5].inventory = {"combinaison": items["combinaison"]}
        self.rooms[8].inventory = {"fiole": items["fiole"]}
        self.rooms[4].inventory = {"cartes": items["cartes"]}
        self.rooms[7].inventory = {"bounty": items["bounty"]}

        characters = {
            "bruno": Character("Bruno", "Chimiste", ["Bonjour !"]),
            "fredo": Character("Fredo", "Chimiste", ["Attention !"]),
            "eduardo": Character("Eduardo", "Ingénieur", ["Ne touche à rien."]),
            "lolo": Character("Lolo", "Serriste", ["Bienvenue !"]),
            "elon": Character("Elon", "Visionnaire", ["Jouons aux cartes !"]),
        }

        self.rooms[9].character = {"bruno": characters["bruno"]}
        self.rooms[8].character = {"fredo": characters["fredo"]}
        self.rooms[6].character = {"eduardo": characters["eduardo"]}
        self.rooms[10].character = {"lolo": characters["lolo"]}
        self.rooms[4].character = {"elon": characters["elon"]}

    def play(self):
        """Démarre le jeu."""
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))

    def process_command(self, command_string):
        """Traite la commande entrée par le joueur."""
        list_of_words = command_string.split()
        command_word = list_of_words[0]
        if command_word not in self.commands:
            print(f"Commande '{command_word}' non reconnue. Tapez 'help'.")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        """Affiche le message de bienvenue."""
        print(f"Bienvenue {self.player.name} dans le jeu d'aventure !")
        print("Tapez 'help' pour obtenir de l'aide.")
        print(self.player.current_room.get_long_description())

def main():
    """Point d'entrée principal du jeu."""
    Game().play()

if __name__ == "__main__":
    main()
