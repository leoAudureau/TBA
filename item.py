class Item:
    def __init__(self, name,description,weigh):
        self.name = name
        self.description = description
        self.weight = weigh
   
    def __str__(self):
        return f"{self.name} : {self.description} ({self.weight} kg)"




