from abc import ABC


class Component(ABC):
    def __init__(self):
        self.mediator = None
