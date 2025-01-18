from room import Room  
from player import Player  
from command import Command  
from actions import Actions  
from item import Item  
from Character import Character

# Module docstring  
"""
Jeu d'aventure textuel où l'utilisateur explore des salles et interagit avec des objets.
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
        # Setup commands  
        help_command = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help_command  
        quit_command = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit_command  
        go_command = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go_command  
        back_command = Command("back", " : revenir dans la salle précédente", Actions.back, 0)
        self.commands["back"] = back_command  
        look_command = Command("look", " : examiner la salle actuelle et voir les objets présents", Actions.look, 0)
        self.commands["look"] = look_command  
        take_command = Command("take", " prendre l'objet voulu", Actions.take, 1)
        self.commands["take"] = take_command  
        drop_command = Command("drop", " déposer l'objet voulu", Actions.drop, 1)
        self.commands["drop"] = drop_command  
        check_command = Command("check", " regarder inventaire", Actions.check, 0)
        self.commands["check"] = check_command  
        talk_command = Command("talk", "parler avec un pnj", Actions.talk, 1)
        self.commands["talk"] = talk_command

        # Setup rooms  
        sas_de_decompression = Room(
            "Sas de décompression", 
            "arrivés dans la station spatiale intercontinantale où les meilleurs astronautes de chaque continent cohabitent, vous êtes dans le sas de décompression"
        )
        self.rooms.append(sas_de_decompression)

        hall1 = Room(
            "hall1", 
            "le Hall 1, ce hall vous permettra d'entrer dans des salles importantes du vaisseau, du commandement au voyage extravéhiculaire"
        )
        self.rooms.append(hall1)

        hall2 = Room(
            "hall2", 
            "le Hall 2, ce Hall vous permettra d'accéder à différentes pièces vitales du vaisseau vous permettant d'expérimenter ce que bon vous semble"
        )
        self.rooms.append(hall2)

        hall3 = Room("hall3", "le Hall 3, à vous la nourriture, c'est assez important dans l'espace...")
        self.rooms.append(hall3)

        salle_commune = Room("salle_commune", "la salle commune du vaisseau, tout le monde s'y restaure et prend du bon temps")
        self.rooms.append(salle_commune)

        module_amarage = Room("module d'amarage", "le module d'amarage, ici vous pouvez accueillir des amis ou avoir la surprise de tomber sur des pirates de l'espace")
        self.rooms.append(module_amarage)

        poste_de_commandes = Room("poste de commande", "le poste de commande, à vous le voyage intergalactique ! C'est aussi ici que tous les systèmes dans le vaisseau sont gérés")
        self.rooms.append(poste_de_commandes)

        reserve = Room("reserve", "la réserve du vaisseau, c'est ici qu'on entrepose la nourriture")
        self.rooms.append(reserve)

        labo2 = Room("labo2", "le deuxième laboratoire, celui de Fredo")
        self.rooms.append(labo2)

        labo1 = Room("labo1", "le premier laboratoire du vaisseau, faites attention Bruno travaille")
        self.rooms.append(labo1)

        serre = Room("serre", "la serre, ici vous pouvez faire pousser à peu près tout ce que vous voulez")
        self.rooms.append(serre)

        # Create exits for rooms  
        sas_de_decompression.exits = {"N": hall2, "E": None, "S": None, "O": None, "U": None, "D": None}
        hall2.exits = {"N": labo1, "E": None, "S": sas_de_decompression, "O": salle_commune, "U": None, "D": None}
        labo1.exits = {"N": None, "E": None, "S": hall2, "O": None, "U": labo2, "D": None}
        salle_commune.exits = {"N": None, "E": hall2, "S": None, "O": hall1, "U": None, "D": None}
        hall1.exits = {"N": module_amarage, "E": salle_commune, "S": None, "O": poste_de_commandes, "U": None, "D": hall3}
        poste_de_commandes.exits = {"N": None, "E": hall1, "S": None, "O": None, "U": None, "D": None}
        module_amarage.exits = {"N": None, "E": None, "S": hall1, "O": None, "U": None, "D": None}
        labo2.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": labo1}
        hall3.exits = {"N": None, "E": None, "S": reserve, "O": serre, "U": hall1, "D": None}
        serre.exits = {"N": None, "E": hall3, "S": None, "O": None, "U": None, "D": None}
        reserve.exits = {"N": hall3, "E": None, "S": None, "O": None, "U": None, "D": None}

        # Setup player and starting room  
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = sas_de_decompression

        # Items  
        hall2.inventory = {"eau": Item("eau", "à boire", 1)}
        poste_de_commandes.inventory = {"eau": Item("eau", "à boire", 1)}
        serre.inventory = {"salade": Item("salade", "bien verte", 0.1)}
        module_amarage.inventory = {"combinaison": Item("combinaison", "vous permet de sortir du véhicule", 30)}
        labo2.inventory = {"fiole": Item("fiole", "contient un liquide violet qui semble suspect", 0.5)}
        salle_commune.inventory = {"cartes": Item("cartes", "pour s'amuser entre collègues", 1)}
        reserve.inventory = {"bounty": Item("bounty", "à manger", 0.1)}

        # PNJ  
        bruno = Character("Bruno", "un chimiste de l'espace qui n'aime pas trop son voisin du dessus", ["Bonjour !"])
        fredo = Character("Fredo", "un autre chimiste de l'espace qui n'aime pas son voisin du dessous", ["Attention en bas ça va chauffer !"])
        eduardo = Character("Eduardo", "un ingénieur en propulsion peu sympathique", ["Ne touche à rien ici ! On devine à ta tête que tu ne sais même pas ce que tu fais ici."])
        lolo = Character("Lolo", "un serriste très accueillant et souriant", ["Ah, enfin quelqu'un qui vient traîner par ici ! Allez viens goûter toutes ces merveilles."])
        elon = Character("Elon", "un homme qui, après la politique, essaye encore quelque chose qu'il ne connaît pas...", ["Come on man! I feel like playing cards."])

        # Ajouter les personnages aux salles avec des clés en minuscules  
        labo1.character[bruno.name.lower()] = bruno  
        labo2.character[fredo.name.lower()] = fredo  
        poste_de_commandes.character[eduardo.name.lower()] = eduardo  
        serre.character[lolo.name.lower()] = lolo  
        salle_commune.character[elon.name.lower()] = elon

    def play(self):
        """Démarre le jeu."""
        self.setup()
        self.print_welcome()
        while not self.finished:
            self.process_command(input("> "))
        return None

    def process_command(self, command_string) -> None:
        """Traite la commande entrée par le joueur."""
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0]

        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def print_welcome(self):
        """Affiche le message de bienvenue."""
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

def main():
    """Point d'entrée principal du jeu."""
    Game().play()

if __name__ == "__main__":
    main()
