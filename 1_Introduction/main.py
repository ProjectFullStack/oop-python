"""
Main.py
20210915
ProjectFullStack
"""

class Dog:
    """
    A class to represent dogs
    """

    scientific_name = "Canis lupus familiaris"

    def __init__(self, name):
        """
        Constructor method that will run every time we create a new
        dog object
        :param name: name
        :type name: str
        """
        self.name = name

    def bark(self):
        """
        Returns the string "bark bark bark!"
        :return: "bark bark bark!"
        :rtype: str
        """
        return "bark bark bark!"


dog_object1 = Dog("Basil")
dog_object2 = Dog("Bronson")

# Interact with the dog_object1 (which is "Basil")
print(dog_object1.name)
print(dog_object1.bark())

# Interact with the dog_object2 (which is "Bronson")
print(dog_object2.name)
print(dog_object2.bark())
