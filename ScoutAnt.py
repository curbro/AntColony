import random

from Ant import Ant
from ColonyNode import ColonyNode


class ScoutAnt(Ant):
    def __init__(self, colony_node: ColonyNode):
        super().__init__(colony_node)

    def take_turn(self):
        self.move()

    def move(self):
        next_node = random.choice(list(self.current_node.adjacent_colony_nodes.values()))
        if next_node:
            self.current_node.remove_ant(self)
            self.current_node = next_node
            self.current_node.add_ant(self)

            if not self.current_node.node_visible:
                # self.current_node.set_random_food_level()
                print(f'Node {self.current_node.node_id} was opened with {self.current_node.food_count} units of food')
                self.current_node.show_node()

