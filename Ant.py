import itertools
from abc import ABC, abstractmethod

from ColonyNode import ColonyNode


class Ant(ABC):
    id_iterator = itertools.count()

    def __init__(self, colony_node: ColonyNode):
        self.id = next(self.id_iterator)
        self.turn_count = 0
        self.current_node = colony_node
        self.lifespan_in_turns = 365 * 10
        self._is_dead = False

    def is_dead(self):
        return self._is_dead or self.turn_count >= self.lifespan_in_turns

    def die(self):
        self._is_dead = True
        self.current_node.remove_ant(self)
        self.current_node.colony.ants.remove(self)

    @abstractmethod
    def take_turn(self):
        pass

    @abstractmethod
    def move(self):
        pass


