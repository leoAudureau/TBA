import random

class Character():
     # Define the constructor.
    def __init__(self, name,description,msgs):
        self.name = name
        self.description= description
        self.msgs = msgs[:]  # Copie de la liste pour éviter des modifications globales
        self._original_msgs = msgs[:]  # Sauvegarde des messages originaux
        self.move_counter = 0  # Compteur de déplacements
        
    
    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        """Affiche un message cyclique du personnage."""
        if not self.msgs:  # Si tous les messages ont été utilisés
            self.msgs = self._original_msgs[:]  # Réinitialise la liste
        return self.msgs.pop(0) 


    def move_to_random_room(self, game):
        '''
        Fait changer Eduardo de salle (une fois sur deux) lorsque nous changeons de salle.
        '''
        self.move_counter += 1
        if self.move_counter % 2 == 0:
            possible_rooms = ["poste_de_commandes", "salle_commune"]
            new_room_name = random.choice(possible_rooms)
            new_room = next(room for room in game.rooms if room.name == new_room_name)
            for room in game.rooms:
                if self.name.lower() in room.character:
                    del room.character[self.name.lower()]
            new_room.character[self.name.lower()] = self
            print(f"Eduardo vient de se déplacer vers : {new_room.name}")