#!/usr/bin/python3
"""``Base`` class module"""

import json
import os
import turtle


class Base:
    """Base of all classes in this project"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Sets private attributes and id fields
            Args:
                _id (int): A integer
        """
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        elif type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        for d in list_dictionaries:
            if type(d) is not dict:
                msg = "list_dictionaries must be a list of dictionaries"
                raise TypeError(msg)

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_obj"""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        ret = []
        with open(filename, "r", encoding="utf-8") as f:
            list_dicts = cls.from_json_string(f.read())
            ret = [cls.create(**d) for d in list_dicts]
        return ret

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes to csv a list of instances"""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        attrs = ('id', 'size', 'width', 'height', 'x', 'y')
        with open(filename, "w", encoding="utf-8") as f:
            for o in list_objs:
                d = o.to_dictionary()
                t = []
                for attr in attrs:
                    if attr not in d:
                        continue
                    t.append(str(d.get(attr)))
                f.write(",".join(t))
                f.write("\n")

    @classmethod
    def load_from_file_csv(cls):
        """deserializes CSV"""
        filename = f"{cls.__name__}.json"

        if not os.path.exists(filename):
            return []

        list_objs = []
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                arguments = line[:-1].split(",")
                o = cls(1, 1)
                o.update(*[int(x) for x in arguments])
                list_objs.append(o)
        return list_objs

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        instance = cls(1, 1)
        instance.x = 0
        instance.y = 0
        instance.update(**dictionary)
        return instance
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        tim = turtle.Turtle()
        tim.screen.bgcolor("#b7312c")
        tim.pensize(3)
        tim.shape("turtle")

        tim.color("#ffffff")
        for rect in list_rectangles:
            tim.showturtle()
            tim.up()
            tim.goto(rect.x, rect.y)
            tim.down()
            for _ in range(2):
                tim.forward(rect.width)
                tim.left(90)
                tim.forward(rect.height)
                tim.left(90)
            tim.hideturtle()

        tim.color("#b5e3d8")
        for sq in list_squares:
            tim.showturtle()
            tim.up()
            tim.goto(sq.x, sq.y)
            tim.down()
            for i in range(2):
                tim.forward(sq.width)
                tim.left(90)
                tim.forward(sq.height)
                tim.left(90)
            tim.hideturtle()

        turtle.exitonclick()
