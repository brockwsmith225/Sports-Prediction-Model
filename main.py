from neural_network import NeuralNetwork
from teams import Team

import numpy as np
import pandas
import datetime

teams = {}
training_games = []
testing_games = []

def main():
	get_data()
	print("Training Games: ", len(training_games))
	print("Testing Games: ", len(testing_games))
	

def get_data():
	postseason_start_date = datetime.datetime(2019, 3, 18)
	data = pandas.read_csv('data/cbb-2019.csv')
	for game in data.itertuples():
		date = game[1].split("/")
		date = datetime.datetime(int(date[2]), int(date[0]), int(date[1]))
		team = game[2]
		opponent = game[5]
		points = game[7]
		opponent_points = game[8]

		if team not in teams.keys():
			teams[team] = Team(team)
		teams[team].add_game(points, opponent_points)

def train():
	pass

def test():
	pass


if __name__ == "__main__":
	main()