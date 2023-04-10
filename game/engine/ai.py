from typing import Union, Iterable
import warnings

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

def lev(a: str, b: str) -> int:
    if len(b) == 0:
        return len(a)
    if len(a) == 0:
        return len(b)
    