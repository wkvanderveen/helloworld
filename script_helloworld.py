"""
This file is a simple Hello World script. It serves no purpose other
than checking whether everything works well.
"""
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go

from random import randint

class Helloworld(object):
	"""docstring for Helloworld"""
	def __init__(self):
		super(Helloworld, self).__init__()

	def print_helloworld(self):
		print("Hello World! (And Git)")

	def random_number(self, lower=0, upper=99):
		rand = randint(lower,upper)
		return rand

	def make_random_list(self, length=20, lower=0, upper=99):
		random_array = np.zeros(length)
		for i in range(len(random_array)):
			random_array[i] = self.random_number(lower, upper)
		return random_array

	def plot_array(self, array):
		trace = go.Scatter(
			x = np.linspace(0,len(array)),
			y = array,
			mode = 'markers'
			)
		data = [trace]

		plot_url = py.plot(data, filename="basic-line")


if __name__ == '__main__':
	my_hello_world = Helloworld()
	my_hello_world.print_helloworld()
	a = my_hello_world.make_random_list()
	my_hello_world.plot_array(a)