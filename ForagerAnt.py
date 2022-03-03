import random
from collections import deque
from enum import Enum
from ordered_set import OrderedSet

from Ant import Ant
from ColonyNode import ColonyNode


class ForagerMode(Enum):
    FORAGE = 1
    RETURN_TO_NEST = 2


class ForagerAnt(Ant):
    def __init__(self, colony_node: ColonyNode):
        super().__init__(colony_node)
        self.mode = ForagerMode.FORAGE
        self.path = deque()
        self.unique_path = []
        # self.previous_node = None

    def move(self):
        if self.mode == ForagerMode.FORAGE:
            next_node = self.get_next_node_in_forage_mode()
        else:
            next_node = self.get_next_node_in_return_to_nest_mode()

        if next_node:
            if self.mode == ForagerMode.FORAGE:
                self.path.append(self.current_node)
                if self.current_node not in self.unique_path:
                    self.unique_path.append(self.current_node)

            self.current_node.remove_ant(self)
            next_node.add_ant(self)
            self.current_node = next_node
        else:
            print("Forager can't move.")

    def get_next_node_in_forage_mode(self) -> ColonyNode:
        # TODO: Monitor for potential endless loop
        next_node = None

        # Get all adjacent nodes that are visible
        nodes = [n for n in list(self.current_node.adjacent_colony_nodes.values()) if n.node_visible]

        # Remove any nodes already visited
        if len(self.unique_path) > 0 and len(nodes) > 1:
            nodes = [node for node in nodes if node not in self.unique_path]

        # Sort any remaining nodes
        if len(nodes) > 0:
            nodes = sorted(nodes, key=lambda n: n.pheromone_count, reverse=True)

            # Get the node with the most pheromone
            nodes_with_highest_pheromone_count = []
            highest_pheromone_count = 0
            for node in nodes:
                if node.pheromone_count > highest_pheromone_count:
                    highest_pheromone_count = node.pheromone_count
                    nodes_with_highest_pheromone_count.clear()
                    nodes_with_highest_pheromone_count.append(node)
                elif node.pheromone_count == highest_pheromone_count:
                    nodes_with_highest_pheromone_count.append(node)

            if nodes_with_highest_pheromone_count:
                if len(nodes_with_highest_pheromone_count) > 1:
                    next_node = random.choice(nodes_with_highest_pheromone_count)
                elif len(nodes_with_highest_pheromone_count) == 1:
                    next_node = nodes_with_highest_pheromone_count[0]
            else:
                if len(nodes) > 1:
                    next_node = random.choice(nodes)
                else:
                    next_node = nodes[0]

        else:
            # If all possible nodes have been visited, start over
            nodes = [n for n in list(self.current_node.adjacent_colony_nodes.values()) if n.node_visible]

            # Randomly return a node from the visible adjacent nodes
            next_node = random.choice(nodes)

        return next_node

    def get_next_node_in_return_to_nest_mode(self) -> ColonyNode:
        next_node = self.path.pop()
        # node_with_queen = [n for n in list(self.current_node.adjacent_colony_nodes.values()) if n.is_queen_present]
        # if len(node_with_queen) == 1:
        #     return node_with_queen[0]
        # else:
        #     return next_node
        return next_node

    def take_turn(self):
        print(f'Ant {self.id} is taking its turn.')
        self.move()
        if self.mode == ForagerMode.FORAGE:
            if self.current_node.food_count > 0 and not self.current_node.is_queen_present:
                self.current_node.remove_food()
                self.add_pheramone_to_current_node()
                self.mode = ForagerMode.RETURN_TO_NEST
        else:
            if self.current_node.is_queen_present:
                self.current_node.add_food()
                self.path.clear()
                self.unique_path.clear()
                self.mode = ForagerMode.FORAGE
            else:
                self.add_pheramone_to_current_node()

    def add_pheramone_to_current_node(self):
        if self.current_node.pheromone_count == 0:
            self.current_node.colony.ant_sim_gui.register_degradation_event_listener(
                self.current_node.decrease_pheromone_by_half
            )
            self.current_node.activated_turn_number = self.current_node.colony.turn_count

        if self.current_node.pheromone_count < 1000:
            self.current_node.add_pheromone()

    def die(self):
        if self.mode == ForagerMode.RETURN_TO_NEST:
            self.current_node.add_food()
            super().die()
