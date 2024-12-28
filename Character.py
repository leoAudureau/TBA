class Character():
     # Define the constructor.
    def __init__(self, name,description,msg):
        self.name = name
        self.description= description
        self.msg= msg
    
    def __str__(self):
        return f"{self.name} : {self.description}"


