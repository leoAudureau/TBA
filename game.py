# Description: Game class


# Import modules


from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from Character import Character

class Game:


    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
   
    # Setup the game
    def setup(self):
     
        # Setup commands


        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir dans la salle précédente", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : examiner la salle actuelle et voir les objets présents", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " prendre l'objet voulu", Actions.take,1)
        self.commands["take"] = take
        drop = Command("drop", " déposer l'objet voulu", Actions.drop,1)
        self.commands["drop"] = drop
        check = Command("check", " regarder inventaire", Actions.check,0)
        self.commands["check"] = check
        talk= Command("talk","parler avec un pnj", Actions.talk,1)
        self.commands["talk"] = talk
        # Setup rooms


        sas_de_decompression= Room("Sas de décompression", "arrivés dans la station spatiale intercontinantale oû les meilleurs astronautes de chaque continent cohabitent, vous êtes dans le sas de décompression")
        self.rooms.append(sas_de_decompression)
       
        hall1= Room("hall1", " le Hall 1, ce hall vous permettra d'entrer dans des salles importantes du vaisseau, du commandemement au voyage extravéhiculaire")
        self.rooms.append(hall1)
       
        hall2=Room("hall2","le Hall 2, ce Haull vous permettra d'acceder à différentes pièces vitales du vaisseau vous permettant d'expérimenter ce que bon vous semble")
        self.rooms.append(hall2)
       
        hall3=Room("hall3","le Hall 3, à vous la nourriture, c'est assez important dans l'espace...")
        self.rooms.append(hall3)
       
        salle_commune=Room("salle_commune"," la salle commune du vaisseau, tout le monde s'y restaure et prend du bon temps ")
        self.rooms.append(salle_commune)
       
        module_amarage=Room("module d'amarage","le module d'amarage, ici vous pouvez acceuilir des amis ou avoir la surprise de tomber sur des pirates de l'espace")
        self.rooms.append(module_amarage)
       
        poste_de_commandes= Room("poste de commande","le poste de commande, à vous le voyage intergalactique ! C'est aussi ici que tout les sytèmes dans le vaisseau sont gérés")
        self.rooms.append(poste_de_commandes)
       
        reserve=Room("reserve", "la réserve du vaisseau, c'est ici qu'on entrepose la nourriture")
        self.rooms.append(reserve)
       
        labo2=Room("labo2","le deuxième laboratoire, celui de Fredo")
        self.rooms.append(labo2)
       
        labo1=Room("labo1", "le premier laboratoire du vaisseau, faites attention Bruno travaille")
        self.rooms.append(labo1)

        serre = Room("serre", "ici vous pouvez faire pousser à peut près tout ce que vous voulez")
        self.rooms.append(serre)




        # Create exits for rooms


        sas_de_decompression.exits = {"N" : hall2, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        hall2.exits = {"N" :labo1, "E" : None, "S" : sas_de_decompression, "O" : salle_commune, "U" : None, "D" : None}
        labo1.exits = {"N" : None, "E" : None, "S" : hall2, "O" : None,"U" : labo2, "D" : None}
        salle_commune.exits = {"N" : None, "E" : hall2, "S" : None, "O" : hall1, "U" : None, "D" : None}
        hall1.exits = {"N" : module_amarage, "E" : salle_commune, "S" : None, "O" : poste_de_commandes, "U" : None, "D" : hall3}
        poste_de_commandes.exits = {"N" : None, "E" : hall1, "S" : None, "O" : None, "U" : None, "D" : None}
        module_amarage.exits = {"N" : None, "E" : None, "S" : hall1, "O" : None, "U" : None, "D" : None}
        labo2.exits = {"N" : None, "E" : None, "S" : None, "O": None,"U" : None, "D" : labo1}
        hall3.exits = {"N" : None, "E" : None, "S" : reserve, "O": serre,"U" : None, "D" : labo1}
        serre.exits = {"N" : None, "E" : hall3, "S" : None, "O": None,"U" : None, "D" : None}
        reserve.exits = {"N" : hall3, "E" : None, "S" : None, "O": None,"U" : None, "D" : None}
        # Setup player and starting room

        #Spawn
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = sas_de_decompression
       
        #Items

        hall2.inventory = {"eau": Item("eau", "à boire", 1)}
        poste_de_commandes.inventory = {"eau": Item("eau", "à boire", 1)}
        serre.inventory = {"salade": Item("salade", "bien verte", 0.1)}
        module_amarage.inventory = {"combinaison spatiale": Item("combinaison spatiale", "vous permet de sortir du véhicule", 30)}
        labo2.inventory = {"fiole": Item("fiole", "contient un liquide violet qui semble suspect", 0.5)}
        salle_commune.inventory = {"jeu de cartes": Item("jeu de cartes", "pour s'amuser entre collègues", 1)}


        #PNJ
        
        bruno = Character("Bruno", "un chimiste de l'espace qui n'aime pas trop son voisin du dessus", ["Bonjour !"])
        fredo = Character("Fredo", "un autre chimiste de l'espace qui n'aime pas son voisin du dessous", ["Attention en bas ça va chauffer !"])

        # Ajouter les personnages aux salles avec des clés en minuscules
        labo1.character[bruno.name.lower()] = bruno
        labo2.character[fredo.name.lower()] = fredo

        
        

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None


    # Process the command entered by the player
    def process_command(self, command_string) -> None:


        # Split the command string into a list of words
        list_of_words = command_string.split(" ")


        command_word = list_of_words[0]


        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)


    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
   


def main():
    # Create a game object and play the game
    Game().play()
   


if __name__ == "__main__":
    main()
