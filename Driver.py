import sys
from PySide6.QtWidgets import QApplication
from AntSimGui import AntSimGui
from Colony import Colony
from ColonyView2 import ColonyView2
from SimulationEvent import SimulationEventType

total_turns = 0
ant_sim_gui = None
colony_view = None
colony = None


def simulation_event_occurred(event_source):
    print("It works!" + str(event_source))
    if event_source == SimulationEventType.NORMAL_SETUP_EVENT:
        colony.normal_setup()

    if event_source == SimulationEventType.STEP_EVENT:
        colony.take_turn()

    if event_source == SimulationEventType.QUEEN_TEST_EVENT:
        colony.queen_test_setup()

    if event_source == SimulationEventType.FORAGER_TEST_EVENT:
        colony.forager_test_setup()

    if event_source == SimulationEventType.SCOUT_TEST_EVENT:
        colony.scout_test_setup()

    if event_source == SimulationEventType.SOLDIER_TEST_EVENT:
        colony.soldier_test_setup()

    if event_source == SimulationEventType.RUN_EVENT:
        colony.take_all_turns()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ant_sim_gui = AntColonySimulatorGUI()
    ant_sim_gui = AntSimGui()
    ant_sim_gui += simulation_event_occurred
    ant_sim_gui.init_ui()
    colony_view = ColonyView2(ant_sim_gui)
    colony = Colony(colony_view, ant_sim_gui, 27, 27)
    ant_sim_gui.show()
    app.exec()

