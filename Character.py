class Character():
     # Define the constructor.
    def __init__(self, name,current_room,description,msg):
        self.name = name
        self.current_room = None
        self.description= description
        self.msg= []
    
    def __str__(self):
        return f"{self.name} : {self.description} {self.current_room} {self.msg}"


