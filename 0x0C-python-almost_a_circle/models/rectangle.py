#!/usr/bin/python3


clsss Rectangle(Base):
    """New Rectangle class"""


def __init__(self, width, height, x=0, y=0, id=None):
    """Initialization of new Rectangle"""

    self.width = width
    self.height = height
    self.x = x
    self.y = y
    super().__init__(id)
