from abc import ABC, abstractmethod
from typing import List
from subscribe.Subscriber import Subscriber


class ObjectAduana(ABC):

    def __init__(self):
        self.num_identification: str = ""
        self.state: str = ""
        self.users: List[Subscriber] = []

    @abstractmethod
    def subscribe(self, sub: Subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, sub: Subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass
