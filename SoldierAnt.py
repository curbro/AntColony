import random
from enum import Enum

from Ant import Ant
from ColonyNode import ColonyNode


class SoldierAnt(Ant):
    def __init__(self, colony_node: ColonyNode):
        super().__init__(colony_node)

    def take_turn(self):
        if self.current_node.bala_count > 0:
            self.attack()
        else:
            self.move()

    def move(self):
        nodes = list(node for node in self.current_node.adjacent_colony_nodes.values() if node.node_visible)
        nodes_with_bala_ants = [n for n in nodes if n.bala_count > 0]

        if len(nodes_with_bala_ants) > 0:
            next_node = random.choice(nodes_with_bala_ants)
        else:
            next_node = random.choice(nodes)

        self.current_node.remove_ant(self)
        self.current_node = next_node
        self.current_node.add_ant(self)

    def attack(self):
        attack_successful = random.randint(0, 1) == 0
        if attack_successful:
            self.current_node.remove_random_bala_ant()
        else:
            print(f'Soldier attacked a bala ant in node {self.current_node.node_id} but missed.')