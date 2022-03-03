import math
import random
from functools import total_ordering

from ColonyNodeView2 import ColonyNodeView2
from AntColonyExceptions import NoFoodException, AntNotFoundException
import Ant


class ColonyNode:
    def __init__(self, colony_node_view: ColonyNodeView2, x_coordinate, y_coordinate, colony):
        self.colony_node_view = colony_node_view
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.colony = colony
        self.node_id = None
        self.node_visible = False
        self.food_count = 0
        self.pheromone_count = 0
        self.is_queen_present = False
        self.forager_count = 0
        self.scout_count = 0
        self.soldier_count = 0
        self.bala_count = 0
        self.hide_node()
        self.node_id = str(x_coordinate) + ", " + str(y_coordinate);
        self.colony_node_view.set_id(self.node_id)
        self.adjacent_colony_nodes = {}
        self.activated_turn_number = None
        self.ants = []

    def __eq__(self, other):
        return isinstance(other, ColonyNode) and self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate

    def notify_hover_text(func):
        def format_hover_text(self, *args, **kwargs):
            func(self, *args, **kwargs)
            hover_text = str.join('\n', [
                'Forager: ' + str(self.forager_count),
                'Scouts: ' + str(self.scout_count),
                'Soldiers: ' + str(self.soldier_count),
                'Bala: ' + str(self.bala_count),
                'Food: ' + str(self.food_count),
                'Pheramone: ' + str(self.pheromone_count)
            ])
            self.colony_node_view.setToolTip(hover_text)
        return format_hover_text

    def hide_node(self):
        self.node_visible = False
        self.colony_node_view.hide_node()

    def show_node(self):
        self.node_visible = True
        self.colony_node_view.show_node()

    @notify_hover_text
    def set_food_count(self, food_count):
        self.food_count = food_count
        self.colony_node_view.set_food_count(self.food_count)

    @notify_hover_text
    def add_food(self):
        self.food_count += 1
        self.colony_node_view.set_food_count(self.food_count)

    @notify_hover_text
    def remove_food(self):
        if self.food_count == 0:
            raise NoFoodException()
        else:
            self.food_count -= 1
            self.colony_node_view.set_food_count(self.food_count)

    @notify_hover_text
    def set_random_food_level(self):
        food_chance = random.randint(0, 3)
        food_count = random.randint(500, 1000)

        ## 25% chance of this node containing food
        if food_chance == 0:
            self.food_count = food_count
            self.colony_node_view.set_food_count(self.food_count)

    @notify_hover_text
    def set_pheromone_count(self, pheromone_count):
        self.pheromone_count = pheromone_count
        self.colony_node_view.set_pheromone_count(self.pheromone_count)

    @notify_hover_text
    def add_pheromone(self):
        self.pheromone_count += 10
        self.colony_node_view.set_pheromone_count(self.pheromone_count)

    @notify_hover_text
    def decrease_pheromone_by_half(self, current_turn_number):
        if self.activated_turn_number and self.pheromone_count > 0 and math.ceil(self.pheromone_count/2) > 0:
            if (self.activated_turn_number - current_turn_number) % 10 == 0:
                self.pheromone_count = math.ceil(self.pheromone_count/2)
                self.colony_node_view.set_pheromone_count(self.pheromone_count)

    @notify_hover_text
    def add_ants(self, ants: list[Ant]):
        for ant in ants:
            self.add_ant(ant)

    @notify_hover_text
    def add_ant(self, ant: Ant):
        from QueenAnt import QueenAnt
        from ForagerAnt import ForagerAnt
        from ScoutAnt import ScoutAnt
        from SoldierAnt import SoldierAnt
        from BalaAnt import BalaAnt

        if isinstance(ant, QueenAnt):
            self.is_queen_present = True
            self.colony_node_view.set_queen(self.is_queen_present)
            self.colony_node_view.show_queen()
        elif isinstance(ant, ForagerAnt):
            self.forager_count += 1
            self.colony_node_view.set_forager_count(self.forager_count)
        elif isinstance(ant, ScoutAnt):
            self.scout_count += 1
            self.colony_node_view.set_scout_count(self.scout_count)
        elif isinstance(ant, SoldierAnt):
            self.soldier_count += 1
            self.colony_node_view.set_soldier_count(self.soldier_count)
        elif isinstance(ant, BalaAnt):
            self.bala_count += 1
            self.colony_node_view.set_bala_count(self.bala_count)

        self.ants.append(ant)

    @notify_hover_text
    def remove_ant(self, ant: Ant):
        from QueenAnt import QueenAnt
        from ForagerAnt import ForagerAnt
        from ScoutAnt import ScoutAnt
        from SoldierAnt import SoldierAnt
        from BalaAnt import BalaAnt

        if isinstance(ant, QueenAnt):
            self.is_queen_present = False
            self.colony_node_view.set_queen(self.is_queen_present)
            self.colony_node_view.hide_queen()
        elif isinstance(ant, ForagerAnt):
            self.forager_count -= 1
            self.colony_node_view.set_forager_count(self.forager_count)
        elif isinstance(ant, ScoutAnt):
            self.scout_count -= 1
            self.colony_node_view.set_scout_count(self.scout_count)
        elif isinstance(ant, SoldierAnt):
            self.soldier_count -= 1
            self.colony_node_view.set_soldier_count(self.soldier_count)
        elif isinstance(ant, BalaAnt):
            self.bala_count -= 1
            self.colony_node_view.set_bala_count(self.bala_count)

        self.ants.remove(ant)

    @notify_hover_text
    def remove_random_bala_ant(self):
        from BalaAnt import BalaAnt

        bala_ants = [ant for ant in self.ants if isinstance(ant, BalaAnt)]
        bala_ant = None
        if len(bala_ants) > 1:
            bala_ant = random.choice(bala_ants)
        elif len(bala_ants) == 1:
            bala_ant = bala_ants[0]

        if bala_ant:
            print(f'A soldier ant attacked and killed a bala ant in node {self.node_id}')
            bala_ant.die()
        else:
            raise AntNotFoundException()

    @notify_hover_text
    def remove_random_non_bala_ant(self):
        from BalaAnt import BalaAnt

        ant_to_die = None
        non_bala_ants = [ant for ant in self.ants if not isinstance(ant, BalaAnt)]
        if len(non_bala_ants) > 0:
            ant_to_die = random.choice(non_bala_ants)
        elif len(non_bala_ants) == 1:
            ant_to_die = non_bala_ants[0]

        if ant_to_die:
            print(f'A bala ant attacked and killed an ant of type {type(ant_to_die)} in node {self.node_id}')
            ant_to_die.die()
        else:
            raise AntNotFoundException()

    @notify_hover_text
    def set_scout_count(self, scout_count):
        if scout_count < 0:
            raise Exception("scout_count can't be less than 0: " + str(scout_count))

        self.scout_count = scout_count
        self.colony_node_view.set_scout_count(self.scout_count)
        if self.scout_count == 0:
            self.colony_node_view.hide_scout()
        else:
            self.colony_node_view.show_scout()

    @notify_hover_text
    def add_scout(self):
        self.scout_count += 1
        self.set_scout_count(self.scout_count)

    @notify_hover_text
    def remove_scout(self):
        self.scout_count -= 1
        self.set_scout_count(self.scout_count)

    @notify_hover_text
    def set_soldier_count(self, soldier_count):
        if soldier_count < 0:
            raise Exception("soldier_count can't be less than 0: " + str(soldier_count))

        self.soldier_count = soldier_count
        self.colony_node_view.set_soldier_count(self.soldier_count)
        if self.soldier_count == 0:
            self.colony_node_view.hide_soldier()
        else:
            self.colony_node_view.show_soldier()

    @notify_hover_text
    def add_soldier(self):
        self.soldier_count += 1
        self.set_soldier_count(self.soldier_count)

    @notify_hover_text
    def remove_soldier(self):
        self.soldier_count -= 1
        self.set_soldier_count(self.soldier_count)

    @notify_hover_text
    def set_bala_count(self, bala_count):
        if bala_count < 0:
            raise Exception("bala_count can't be less than 0: " + str(bala_count))

        self.bala_count = bala_count
        self.colony_node_view.set_bala_count(self.bala_count)
        if self.bala_count == 0:
            self.colony_node_view.hide_bala()
        else:
            self.colony_node_view.show_bala()

    @notify_hover_text
    def add_bala(self):
        self.bala_count += 1
        self.set_bala_count(self.bala_count)

    @notify_hover_text
    def remove_bala(self):
        self.bala_count -= 1
        self.set_bala_count(self.bala_count)
