from typing import Union
from beta.engine import npc

class Dungeon:
    def __init__(self, entryID: str) -> None:
        self.rooms = []
    
    def add(self, room: object) -> None:
        self.rooms.append(room)

class Room:
    def __init__(self, parent: Dungeon, id: str, name: str, desc: str, npcs: list[npc.NPC], adjacents: list[str]) -> None:
        self.parent = parent
        self.parent.add(self)
        self.id = id
        self.name = name
        self.description = self.desc = desc
        self.npcs = npcs
        self.adjacents = adjacents

    def removeNPC(self, identifier: Union[str, npc.NPC]) -> None:
        target = None
        for char in self.npcs:
            if char == identifier or char.name == identifier:
                target = char
                break
        self.npcs = [char for char in self.npcs if char != target]