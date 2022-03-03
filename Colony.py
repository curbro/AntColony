import random
import threading

from Ant import Ant
from AntSimGui import AntSimGui
from ColonyNode import ColonyNode
from ColonyNodeView2 import ColonyNodeView2
from ColonyView2 import ColonyView2
from ForagerAnt import ForagerAnt
from QueenAnt import QueenAnt
from ScoutAnt import ScoutAnt
from SoldierAnt import SoldierAnt


def setInterval(interval):
    def decorator(function):
        def wrapper(*args, **kwargs):
            stopped = threading.Event()

            def loop(): # executed in another thread
                while not stopped.wait(interval): # until stopped
                    function(*args, **kwargs)

            t = threading.Thread(target=loop)
            t.daemon = True # stop if the program exits
            t.start()
            return stopped
        return wrapper
    return decorator

class Colony:
    def __init__(self, colony_view: ColonyView2, ant_sim_gui: AntSimGui, x_length, y_length):
        self.ant_sim_gui = ant_sim_gui
        self.colony_view = colony_view
        self.colony_nodes = []
        self.colony_node_view = None
        self.x_length = x_length
        self.y_length = y_length
        self.ants: list[Ant] = []
        self.initialize_colony_grid()
        self.queen = None
        self.central_node = None
        self.turn_count = 0
        self.hatched_ant = None

    def common_setup(func):
        def wrapper(self):
            self.central_node = self.colony_nodes[13][13]
            self.central_node.show_node()
            self.central_node.set_food_count(1000)
            self.queen = QueenAnt(self.central_node)
            self.ants.append(self.queen)
            self.central_node.add_ant(self.queen)

            func(self)

            self.ant_sim_gui.set_colony_view(self.colony_view)
        return wrapper

    def base_node_layout(func):
        def wrapper(self):
            func(self)
            central_node_perimeter_nodes = list(self.central_node.adjacent_colony_nodes.values())
            for node in central_node_perimeter_nodes:
                node.show_node()
        return wrapper

    @common_setup
    @base_node_layout
    def normal_setup(self):
        # central_node.set_soldier_count(10)
        for x in range(50):
            forager_ant = ForagerAnt(self.central_node)
            self.ants.append(forager_ant)
            self.central_node.add_ant(forager_ant)

        for x in range(4):
            scout_ant = ScoutAnt(self.central_node)
            self.ants.append(scout_ant)
            self.central_node.add_ant(scout_ant)

        for x in range(10):
            soldier_ant = SoldierAnt(self.central_node)
            self.ants.append(soldier_ant)
            self.central_node.add_ant(soldier_ant)

        self.central_node.set_food_count(1000)

    @common_setup
    def queen_test_setup(self):
        pass

    @common_setup
    def forager_test_setup(self):
        for x in range(1):
            forager_ant = ForagerAnt(self.central_node)
            self.ants.append(forager_ant)
            self.central_node.add_ant(forager_ant)

        central_node_perimeter_nodes = list(self.central_node.adjacent_colony_nodes.values())
        for node in central_node_perimeter_nodes:
            node.show_node()
            for outer_node in list(node.adjacent_colony_nodes.values()):
                outer_node.show_node()

        self.colony_nodes[11][11].set_food_count(500)
        self.colony_nodes[15][15].set_food_count(500)

    @common_setup
    def soldier_test_setup(self):
        self.show_all_nodes()
        for x in range(4):
            soldier_ant = SoldierAnt(self.central_node)
            self.ants.append(soldier_ant)
            self.central_node.add_ant(soldier_ant)

    def show_all_nodes(self):
        for x in range(self.x_length):
            for y in range(self.y_length):
                self.colony_nodes[x][y].show_node()

    @common_setup
    @base_node_layout
    def scout_test_setup(self):
        for x in range(4):
            scout_ant = ScoutAnt(self.central_node)
            self.ants.append(scout_ant)
            self.central_node.add_ant(scout_ant)

    def initialize_colony_grid(self):
        for x in range(self.x_length):
            row = []
            self.colony_nodes.append(row)
            for y in range(self.y_length):
                colony_node_view = ColonyNodeView2(self.colony_view.scrollAreaWidgetContents)
                self.colony_view.add_colony_node_view(colony_node_view, x, y)
                colony_node = ColonyNode(colony_node_view, x, y, self)
                row.append(colony_node)

                # Build node perimeter references
                # Set north and south nodes
                if y > 0:
                    south_node = self.colony_nodes[x][y-1]
                    assert south_node, "North node is None"
                    colony_node.adjacent_colony_nodes['south'] = south_node
                    if x > 0:
                        southwest_node = south_node.adjacent_colony_nodes['west']
                        colony_node.adjacent_colony_nodes['southwest'] = southwest_node
                        if x < self.x_length - 1 and y < self.y_length - 1:
                            southwest_node.adjacent_colony_nodes['northeast'] = colony_node
                    south_node.adjacent_colony_nodes['north'] = colony_node

                # Set east and west nodes
                if x > 0:
                    west_node = self.colony_nodes[x-1][y]
                    assert west_node, "West node is None"
                    colony_node.adjacent_colony_nodes['west'] = west_node
                    if y < self.y_length - 1:
                        northwest_node = west_node.adjacent_colony_nodes['north']
                        colony_node.adjacent_colony_nodes['northwest'] = northwest_node
                        if y > 0:
                            northwest_node.adjacent_colony_nodes['southeast'] = colony_node
                    west_node.adjacent_colony_nodes['east'] = colony_node
        print('Colony Grid Initialized')

    def add_bala_to_colony(self):
        from BalaAnt import BalaAnt

        x, y = None, None
        choice = random.randint(0, 3)
        if choice == 0:
            x = 0
        elif choice == 1:
            x = self.x_length - 1
        elif choice == 2:
            y = 0
        else:
            y = self.y_length - 1

        if x is not None:
            y = random.choice(range(self.y_length))
        elif y is not None:
            x = random.choice(range(self.x_length))
        else:
            raise Exception('Both x and y are none')

        print(f'Spawning new bala ant in node {x},{y}')
        bala_node = self.colony_nodes[x][y]
        bala_ant = BalaAnt(bala_node)
        self.ants.append(bala_ant)
        bala_node.add_ant(bala_ant)

    @setInterval(.5)
    def take_all_turns(self):
        self.take_turn()

    def take_turn(self):
        if not self.queen.is_dead():
            # All ants take their turn
            for ant in self.ants:
                if not ant.is_dead():
                    ant.take_turn()
            self.ants = [ant for ant in self.ants if not ant.is_dead()]

            # Increment turn count
            self.turn_count += 1

            # Bala chance
            bala_chance = random.randint(1, 100)
            # if bala_chance < 4:
            if bala_chance < 51:
                self.add_bala_to_colony()

            # Degrade pheramone
            self.ant_sim_gui.fire_degradation_event(self.turn_count)

            # Add hatched ant to the rotation
            if self.hatched_ant:
                self.ants.append(self.hatched_ant)
        else:
            print("The queen is dead. Simulation terminated.")
            raise Exception()

