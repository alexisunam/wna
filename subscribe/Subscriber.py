from abc import ABC, abstractmethod

from aduana.ObjectAduana import ObjectAduana


class Subscriber(ABC):

    @abstractmethod
    def update(self, obj: ObjectAduana):
        pass
