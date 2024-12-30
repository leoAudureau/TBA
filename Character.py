import random

class Character():
     # Define the constructor.
    def __init__(self, name,description,msgs):
        self.name = name
        self.description= description
        self.msgs = msgs[:]  # Copie de la liste pour éviter des modifications globales
        self._original_msgs = msgs[:]  # Sauvegarde des messages originaux
        
    
    def __str__(self):
        return f"{self.name} : {self.description}"

    def get_msg(self):
        """Affiche un message cyclique du personnage."""
        if not self.msgs:  # Si tous les messages ont été utilisés
            self.msgs = self._original_msgs[:]  # Réinitialise la liste
        return self.msgs.pop(0) 


