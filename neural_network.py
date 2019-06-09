import math
import numpy as np
from scipy.stats import truncnorm
from scipy.special import expit

def truncated_normal(mean=0, std_dev=1, lower=0, upper=10):
		return truncnorm((lower - mean) / std_dev, (upper - mean) / std_dev, loc=mean, scale=std_dev)


class NeuralNetwork:

	def __init__(self, input_nodes, hidden_nodes):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = 1

		self.weights_ih = self.create_weight_matrix(input_nodes, hidden_nodes)
		self.weights_ho = self.create_weight_matrix(hidden_nodes, 1)



	def create_weight_matrix(self, input_nodes, output_nodes):
		bound = 1 / np.sqrt(input_nodes)
		x = truncated_normal(mean=2, std_dev=1, lower=-bound, upper=bound)
		return x.rvs((output_nodes, input_nodes))



	def train(self, input_vector, expected_odds):
		pass



	def run(self, input_vector):
		input_vector = np.array(input_vector, ndmin=2).T

		output_vector = np.dot(self.weights_ih, input_vector)
		output_vector = expit(output_vector)

		output_vector = np.dot(self.weights_ho, output_vector)
		output_vector = expit(output_vector)

		return output_vector