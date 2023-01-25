from abc import ABC, abstractmethod
from typing import List

from aduana.ObjectAduana import ObjectAduana
from subscribe.Subscriber import Subscriber


class User(Subscriber, ABC):

    def __init__(self):
        self.objects: List[ObjectAduana] = []
        self.type: str = ""
        self.name: str = ""
        self.phone_number: str = ""

    @abstractmethod
    def update(self, obj: ObjectAduana):
        pass
