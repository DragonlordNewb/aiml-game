import blessed

from game.engine import items

term = blessed.Terminal()

class Room:
    def __init__(self, description: str, items: list[engine.items.Item]=[]) -> None:
        self.description = description
        self.items = items
        
    def describe(self) -> None:
        print(term.clear())

    def deposit(self, item: items.Item or list[items.Item]) -> None:
        self.