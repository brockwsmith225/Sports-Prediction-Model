from neural_network import NeuralNetwork
from teams import Team

import numpy as np
import pandas

def main():
	get_data()
	

def get_data():
	teams = {}
	games = []
	data = pandas.read_csv('data/cbb-2019.csv')
	for game in data.itertuples():
		print(game)


def train():
	pass

def test():
	pass


if __name__ == "__main__":
	main()