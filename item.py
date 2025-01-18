"""
This module defines the Item class used in a text-based adventure game.
"""

class Item:  # pylint: disable=too-few-public-methods
    """Represents an item in a text-based adventure game."""

    def __init__(self, name, description, weight):
        """
        Initialize an Item instance.

        :param name: str, the name of the item
        :param description: str, a brief description of the item
        :param weight: float, the weight of the item
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        Return a string representation of the item.

        :return: str, formatted string describing the item
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
