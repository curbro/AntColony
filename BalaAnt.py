import random

from Ant import Ant
from ColonyNode import ColonyNode


class BalaAnt(Ant):
    def __init__(self, colony_node: ColonyNode):
        super().__init__(colony_node)

    def take_turn(self):
        if self.current_node.is_queen_present \
                or self.current_node.scout_count > 0\
                or self.current_node.forager_count > 0\
                or self.current_node.soldier_count > 0:
            self.attack()
        else:
            self.move()

    def move(self):
        next_node = random.choice(list(self.current_node.adjacent_colony_nodes.values()))
        self.current_node.remove_ant(self)
        self.current_node = next_node
        self.current_node.add_ant(self)

    def attack(self):
        attack_successful = random.randint(0, 1) == 0
        if attack_successful:
            self.current_node.remove_random_non_bala_ant()
        else:
            print(f'Bala attacked in node {self.current_node.node_id} but missed.')
