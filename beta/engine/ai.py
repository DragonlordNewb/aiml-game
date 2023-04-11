from typing import Callable, Iterable, Union
from x1 import ent
from random import choice

Number = Union[int, float]

class Agent:
    def __init__(self, *entities: set[ent.Entity], function: Callable=None) -> None:
        if function:
            self.function = function

        if not hasattr(self, "function"):
            raise SyntaxError("Must supply a \"function\" callable to Agent by subclassing or adding the keyword argument at initialization.")

        self.entities = list(entities)

        self.parent = None

    def __repr__(self) -> str:
        return "<Agent running " + repr(self.function) + " with args " + ", ".join([repr(ent) for ent in self])

    def __len__(self) -> int:
        return len(self.entities)

    def __del__(self) -> None:
        if self.parent:
            self.parent.remove(self)

    def duplicate(self) -> object:
        agent = Agent(*self.entities, function=self.function)
        agent.parent = self.parent

    def evaluate(self, **kwargs: dict[str: any]) -> any:
        return self.function(*self.entities, **kwargs)

    def vary(self, count: int=1, magnitude: Number=1) -> None:
        while count > 0:
            choice(self.entities).vary(magnitude)
            count -= 1

    def variants(self, variantCount: int=1, mutationCount: int=1 magnitude: Number=1) -> None:
        variants = []
        for _ in range(count):
            variants.append(self.duplicate())
        
        for variant in variants:
            variant.vary(mutationCount, magnitude)

        return variants

class SingleParentGeneticIntelligence:
    def __init__(self, *precursors: set[Agent], evaluator: Callable=None, expansionRate: Number=2, extinctionRate: Number=0.5, mutationRate: Number=1, mutationMagnitude: Number=1) -> None:
        self.generations = [list(precursors)]
        self.expansionRate = expansionRate
        self.extinctionRate = extinctionRate
        self.mutationRate = mutationRate
        self.mutationMagnitude = mutationMagnitude

        if evaluator:
            self.evaluator = evaluator

        if not hasattr(self, "evaluator"):
            raise SyntaxError("Must supply a \"evaluator\" callable to GeneticIntelligence by subclassing or adding the keyword argument at initialization.")

        for agent in self.agents():
            agent.parent = self

    def __repr__(self) -> str:
        return "<GeneticIntelligence>"

    def __len__(self) -> int:
        return len(self.[-1])

    def __iter__(self) -> Iterable:
        return iter(self.generations)

    def __getitem__(self, index: int) -> list[Agent]:
        return self.generations[index]

    def agents(self) -> Iterable:
        output = []
        for generation in self:
            for agent in generation:
                output.append(agent)
        return iter(output)

    def remove(self, agent: Agent) -> None:
        for index, generation in enumerate(self):
            if agent in generation:
                self.generations[index] = [x for x in self[index] if x != agent]

    def latest(self) -> list[Agent]:
        return self[-1]

    def produceNewGeneration(self, expansionRate: Number=None, extinctionRate: Number=None, mutationRate: Number=None, mutationMagnitude: Number=None) -> None:
        expansionRate = expansionRate or self.expansionRate
        extinctionRate = extinctionRate or self.extinctionRate
        mutationRate = mutationRate or self.mutationRate
        mutationMagnitude = mutationMagnitude or self.mutationMagnitude
        if not (expansionRate and extinctionRate and mutationRate and mutationMagnitude):
            raise SyntaxError("Must supply expansionRate, extinctionRate, etc variables at function call or init")

        parents = self.latest()
        children = []
        for parent in parents:
            for variant in parent.variants(self.expansionRate, mutationRate, mutationMagnitude):
                children.append(variant)

        childrenByScore = {self.evaluator(child.function): child for child in children}
        minimum = extinctionRate * max(childrenByScore.keys())
        survivors = [childrenByScore[key] for key in childrenByScore.keys() if key >= minimum]
        for child in childrenByScore.values():
            if child not in survivors:
                del child
        
        self.generations.append(survivors)

    def predict(self, **kwargs: dict[str, any]) -> any:
        agentsByScore = {self.evaluator(agent.function): agent for agent in self.latest()}
        best = agentsByScore[max(agenstByScore.keys())]
        return best.evaluate(**kwargs)