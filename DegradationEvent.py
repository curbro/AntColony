class DegradationEvent:
    def __init__(self, current_turn_number: int) -> None:
        self.current_turn_number = current_turn_number
        self.listeners = []

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.listeners.append(listener)
        return self

    def notify(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)
