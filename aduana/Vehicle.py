from typing import List
from aduana.ObjectAduana import ObjectAduana
from subscribe.Subscriber import Subscriber


class Vehicle(ObjectAduana):

    def __init__(self):
        ObjectAduana.__init__(self)

    def subscribe(self, sub: Subscriber):
        self.users.append(sub)

    def unsubscribe(self, sub: Subscriber):
        self.users.remove(sub)

    def notify(self):
        pass
