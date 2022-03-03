import string
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QSize
from PySide6.QtGui import QScreen

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, \
    QLabel, QSizePolicy
from ColonyNodeView import ColonyNodeView
from ColonyView import ColonyView
from SimulationEvent import SimulationEventType, SimulationEvent


class AntColonySimulatorGUI(QMainWindow):

    def __init__(self):
        super(AntColonySimulatorGUI, self).__init__()
        self.setWindowTitle("Ant Colony Simulator")
        self.main_layout = QVBoxLayout()
        self.control_panel_layout = QHBoxLayout()
        self.colony_node_layout = QGridLayout()
        self.control_panel_widget = QWidget()
        self.top_size_policy = QSizePolicy()
        # self.top_size_policy.setVerticalStretch(1)
        self.control_panel_widget.setSizePolicy(self.top_size_policy)
        self.colony_node_widget = QWidget()
        self.bottom_size_policy = QSizePolicy()
        # self.bottom_size_policy.setVerticalStretch(20)
        self.colony_node_widget.setSizePolicy(self.bottom_size_policy)
        self.control_panel_widget.setLayout(self.control_panel_layout)
        self.main_layout.addWidget(self.control_panel_widget)
        self.main_layout.addStretch()
        self.colony_node_widget.setLayout(self.colony_node_layout)
        self.main_layout.addWidget(self.colony_node_widget)

        self.normal_setup_botton = QPushButton("Normal Setup")
        self.control_panel_layout.addWidget(self.normal_setup_botton)
        self.normal_setup_botton.setToolTip("Set up a simulation for normal execution")
        self.normal_setup_botton.clicked.connect(self.button_pushed_event)

        self.queen_test_button = QPushButton("Queen Test")
        self.control_panel_layout.addWidget(self.queen_test_button)
        self.queen_test_button.setToolTip("Set up a simulation for testing the queen ant")
        self.queen_test_button.clicked.connect(self.button_pushed_event)

        self.scout_test_button = QPushButton("Scout Test")
        self.control_panel_layout.addWidget(self.scout_test_button)
        self.scout_test_button.setToolTip("Set up a simulation for testing the scout ant")
        self.scout_test_button.clicked.connect(self.button_pushed_event)

        self.forager_test_button = QPushButton("Forager Test")
        self.control_panel_layout.addWidget(self.forager_test_button)
        self.forager_test_button.setToolTip("Set up a simulation for testing the forager ant")
        self.forager_test_button.clicked.connect(self.button_pushed_event)

        self.soldier_test_button = QPushButton("Soldier Test")
        self.control_panel_layout.addWidget(self.soldier_test_button)
        self.soldier_test_button.setToolTip("Set up a simulation for testing the soldier ant")
        self.soldier_test_button.clicked.connect(self.button_pushed_event)

        self.run_button = QPushButton("Run")
        self.control_panel_layout.addWidget(self.run_button)
        self.run_button.setToolTip("Run the simulation continuously")
        self.run_button.clicked.connect(self.button_pushed_event)

        self.step_button = QPushButton("Step")
        self.control_panel_layout.addWidget(self.step_button)
        self.step_button.setToolTip("Step through the simulation one turn at a time")
        self.step_button.clicked.connect(self.button_pushed_event)

        self.time_label = QLabel()
        self.time_label.setText("Day 0, Turn 0")
        self.control_panel_layout.addWidget(self.time_label)

        # self.colony_node_layout.addWidget(ColonyNodeView(), 0, 0)
        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

        screen_size = QScreen.availableSize(QApplication.primaryScreen())
        if screen_size.width() >= 1200:
            widget.setMinimumSize(1024, 768)
        elif screen_size.width() >= 1024:
            widget.setMinimumSize(800, 600)
        else:
            widget.setMinimumSize(640, 400)

        self.simulation_event_listeners = []

        # self.init_gui()

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.simulation_event_listeners.append(listener)
        return self

    def set_colony_view(self, colony_view: ColonyView):
        # self.colony_node_layout.addWidget(colony_view)
        self.main_layout.addWidget(colony_view)

    def fire_simulation_event(self, simulation_event_type: SimulationEventType) -> None:
        simulation_event = SimulationEvent(simulation_event_type)
        simulation_event.listeners = self.simulation_event_listeners
        simulation_event.notify(simulation_event_type)

    def set_time(self, time: string) -> None:
        self.time_label.setText(time)

    def button_pushed_event(self):
        if self.sender() == self.normal_setup_botton:
            self.fire_simulation_event(SimulationEventType.NORMAL_SETUP_EVENT)
        elif self.sender() == self.queen_test_button:
            self.fire_simulation_event(SimulationEventType.QUEEN_TEST_EVENT)
        elif self.sender() == self.scout_test_button:
            self.fire_simulation_event(SimulationEventType.SCOUT_TEST_EVENT)
        elif self.sender() == self.forager_test_button:
            self.fire_simulation_event(SimulationEventType.FORAGER_TEST_EVENT)
        elif self.sender() == self.soldier_test_button:
            self.fire_simulation_event(SimulationEventType.SOLDIER_TEST_EVENT)
        elif self.sender() == self.run_button:
            self.fire_simulation_event(SimulationEventType.RUN_EVENT)
        elif self.sender() == self.step_button:
            self.fire_simulation_event(SimulationEventType.STEP_EVENT)

    # def init_gui(self):
    #     window = AntColonySimulatorGUI()
    #     window.show()
# app = QApplication(sys.argv)


# app.exec()
