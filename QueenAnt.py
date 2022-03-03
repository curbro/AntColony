import random

from Ant import Ant
from ColonyNode import ColonyNode
from ForagerAnt import ForagerAnt
from AntColonyExceptions import NoFoodException
from ScoutAnt import ScoutAnt
from SoldierAnt import SoldierAnt


class QueenAnt(Ant):
    def __init__(self, colony_node: ColonyNode):
        super().__init__(colony_node)
        self.lifespan_in_turns = 20 * 365 * 10
        assert self.id == 0, "Queen's Id is not 0!"

    def hatch_ant(self):
        ant_chance = random.randint(0, 3)
        hatched_ant = None
        if ant_chance < 2:
            # Create a forager and add it to the colony
            hatched_ant = ForagerAnt(self.current_node)
        elif ant_chance == 2:
            # Create a scout ant and add it to the colony
            hatched_ant = ScoutAnt(self.current_node)
        else:
            # Create a soldier and add it to the colony
            hatched_ant = SoldierAnt(self.current_node)
        if hatched_ant:
            self.current_node.add_ant(hatched_ant)
            self.current_node.colony.hatched_ant = hatched_ant
            print(f'Queen hatched a {type(hatched_ant)}')

    def eat(self):
        try:
            self.current_node.remove_food()
        except NoFoodException:
            self.die()

    def take_turn(self):
        print(f'Ant {self.id} is taking its turn.')
        if self.turn_count % 10 == 0:
            self.hatch_ant()
        self.eat()

    def move(self):
        """The queen never moves from her square"""
        pass


