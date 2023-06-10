#!/usr/bin/python3

"""Defines Base model class"""

class Base():
	"""The Base model class"""

	__nb_objects = 0

	def __init__(self, id=None):
		"""Args: id(int), new initialized Base"""

		if id is not None:
			self.id = id
		else:
			Base.__nb_objects += 1
			self.id = Base__nb_objects

		