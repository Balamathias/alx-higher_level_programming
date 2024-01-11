class Base:

    """Base class for this project"""
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        if id != None:
            self.id = id
        else:
            self.id += type(self).__nb_objects
            