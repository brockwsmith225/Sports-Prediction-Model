from neural_network import NeuralNetwork
import numpy as np

def main():
	network = NeuralNetwork(4, 2)

	team_1 = np.array([71.4, 56.1])
	team_2 = np.array([72.8, 59.5])
	input_vector = np.concatenate((team_1, team_2))
	expected_odds = 0.66
	
	

if __name__ == "__main__":
	main()