from enum import Enum


class SimulationEventType(Enum):
    NORMAL_SETUP_EVENT = 0
    QUEEN_TEST_EVENT = 1
    SCOUT_TEST_EVENT = 2
    FORAGER_TEST_EVENT = 3
    SOLDIER_TEST_EVENT = 4
    RUN_EVENT = 5
    STEP_EVENT = 6


class SimulationEvent:
    def __init__(self, event_type: SimulationEventType) -> None:
        self.event_type = event_type
        self.listeners = []

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.listeners.append(listener)
        return self

    def notify(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)
