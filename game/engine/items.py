from game import data

class Item:
    def __init__(self, name, quantity: int=1) -> None:
        self.name = name
        self.quantity = quantity
    
    def __str__(self) -> str:
        if self.quantity == 1:
            if self.name[0] in data.VOWELS:
                return "an " + str(self.name)
            return "a " + str(self.name)
        return str(self.quantity) + " " + self.name + "s"

    def __repr__(self) -> str:
        return str(self)

    def __iadd__(self, n: int) -> object:
        return type(self)(self.name, quantity + n)

    def __isub__(self, n: int) -> object:
        return type(self)(self.name, quantity - n)