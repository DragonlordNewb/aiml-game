import blessed

term = blessed.Terminal()

class Game:
    def __init__(self, *rooms: list[object]) -> None:
        self.rooms = rooms
        for room in self.rooms:
            room.parent = self
            
    def __getitem__(self, ident: str) -> object:
        for room in self:
            if room.ident == ident:
                return room
        raise KeyError("Room not found, invalid location.")
        
    def play(self) -> None:
        currentRoom = self.rooms[0]
        while True:
            currentRoom = self.room.next()

class Room:
    def __init__(self, ident: str, mappings: dict[str: str], description: str) -> None:
        self.description = description
        self.items = items
        self.ident = ident
        self.mappings = mappings
        self.parent = None
        
    def describe(self) -> None:
        print(term.clear())
        print(self.description)
            
    def next(self) -> None:
        self.describe()
        while True:
            usr = input(" > ")
            if usr in self.mappings.keys():
                return self.parent[usr]
            print("Invalid input, try again.")
