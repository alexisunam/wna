from aduana.ObjectAduana import ObjectAduana
from subscribe.User import User


class Operator(User):

    def __init__(self):
        User.__init__(self)

    def update(self, obj: ObjectAduana):
        self.objects.append(obj)
