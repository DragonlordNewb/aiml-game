from typing import Union, Iterable
import warnings
import random

Number = Union[int, float]

class ArtificialIntelligenceWarning(Warning):
    pass

class Minnow:
    """
    Simple binary classification algorithm that
    can learn even when redundant/irrelevant 
    inputs abound. Based on Winnow2.
    """
    def __init__(self, length: int, threshold: Number, alpha: Number=2) -> None:
        if alpha <= 1:
            warnings.warn("Alpha of 1 or less may yield abberant behavior in Winnow2 instance.")

        self.alpha = alpha
        self.length = length
        self.threshold = threshold
        self.weights = [1] * len(self)

        self.lastInput = None
        self.lastOutput = None

    def __repr__(self) -> str:
        return "<Minnow length=" + str(len(self)) + " threshold=" + str(self.threshold) + " alpha=" + str(self.alpha) + ">"

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterable:
        return iter(self.weights)

    def __getitem__(self, index: int) -> Number:
        return self.weights[index]
    
    def __setitem__(self, index: int, value: Number) -> None:
        self.weights[index] = value

    def _getIndices(self, threshold: Number) -> list[int]:
        return [index for index, value in enumerate(self) if value >= threshold]

    def predict(self, *data: set[Number]) -> bool:
        data = list(data) # just to make sure
        self.lastInput = data

        output = sum([x * w for x, w in zip(self, data)]) >= self.threshold
        self.lastOutput = output

        return self.lastOutput

    def feedback(self, answer: bool) -> None:
        if self.lastOutput and not answer: # correct answer was False
            mean = sum(self.lastInput) / len(self.lastInput)
            indices = self._getIndices(mean)
            for index in indices:
                self[index] /= self.alpha
        if answer and not self.lastOutput: # correct answer was True
            mean = sum(self.lastInput) / len(self.lastOutput)
            indices = self._getIndices(mean)
            for index in indices:
                self[index] *= self.alpha

# pathfinding for some reason

class Node:
    def __init__(self, key: str, **distances: dict[str, Number]) -> None:
        self.key = key
        self.distances = distances
        self.weights = {k: 1 for k in self.keys()}

    def _getIndex(self, key: str) -> int:
        for index, otherKey in enumerate(self.distances.keys()):
            if key == otherKey:
                return index

    def keys(self) -> list[str]:
        return list(self.distances.keys())
    
    def weights(self) -> list[Number]:
        return self.weights.values()
    
    def weight(self, key: str, value: Number) -> None:
        self.weights[key] += value
    
    def connects(self, key: str) -> bool:
        return key in self.keys()

    def distance(self, key: str) -> Number:
        return self.distances[key]
    
    def weightedRandom(self) -> str:
        return random.choices(self.keys(), weights=self.weights())
    
class IntelligentPathfinder:
    def __init__(self, *nodes: set[Node]) -> None:
        self.nodes = list[nodes]

    def __iter__(self) -> Iterable:
        return iter(self.nodes)
    
    def __getitem__(self, key: str) -> Node:
        for node in self:
            if node.key == key:
                return node
        raise KeyError("No node with key \"" + str(key) + "\".")
    
    def addNode(self, *nodes: set[Node]) -> None:
        for node in nodes:
            self.nodes.append(node)

class EphemeralIntelligentPathfinder(IntelligentPathfinder):
    def pathfind(self, start: str, end: str, iterations: int) -> None:
        end = self[end]

        path: list[str] = []
        currentLocation = self[start]
        while currentLocation != end:
            currentLocation = self[currentLocation.weightedRandom()]
            path.append(currentLocation)

        distance = []

        weighted = []
        for index, node in path[:-1]:
            if node not in weighted:
                node.weight(path[index + 1], )

def tail(s: Iterable) -> Iterable:
    return s[1:]

def lev(a: Iterable, b: Iterable) -> int:
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    if a[0] == b[0]:
        return lev(tail(a), tail(b))
    return min(
        lev(tail(a), b),
        lev(b, tail(a)),
        lev(tail(a), tail(b))
    )

class StringMatcher:
    def __init__(self, **strings: dict[str: str]) -> None:
        self.strings = strings
        for key in self.strings.keys():
            self.strings[key] = self.strings[key].split(" ")
        print(self.strings)
    
    def match(self, string: str) -> None:
        string = string.split(" ")
        stringsByLev = {}
        for key in self.strings.keys():
            otherString = self.strings[key]
            stringsByLev[lev(string, otherString)] = key
        print(stringsByLev)
        return stringsByLev[min(stringsByLev.keys())]