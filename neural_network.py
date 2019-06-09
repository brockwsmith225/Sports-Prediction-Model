import math
import numpy as np
from scipy.stats import truncnorm
from scipy.special import expit

def truncated_normal(mean=0, std_dev=1, lower=0, upper=10):
		return truncnorm((lower - mean) / std_dev, (upper - mean) / std_dev, loc=mean, scale=std_dev)


class NeuralNetwork:

	def __init__(self, input_nodes, hidden_nodes, learning_rate):
		self.input_nodes = input_nodes
		self.hidden_nodes = hidden_nodes
		self.output_nodes = 1

		self.learning_rate = learning_rate

		self.weights_ih = self.create_weight_matrix(input_nodes, hidden_nodes)
		self.weights_ho = self.create_weight_matrix(hidden_nodes, 1)



	def create_weight_matrix(self, input_nodes, output_nodes):
		bound = 1 / np.sqrt(input_nodes)
		x = truncated_normal(mean=2, std_dev=1, lower=-bound, upper=bound)
		return x.rvs((output_nodes, input_nodes))



	def train(self, input_vector, expected_output):
		input_vector = np.array(input_vector, ndmin=2).T
		expected_output = np.array(expected_output, ndmin=2).T

		hidden_vector = expit(np.dot(self.weights_ih, input_vector))
		output_vector = expit(np.dot(self.weights_ho, hidden_vector))

		output_errors = expected_output - output_vector
		desired_change = output_errors * output_vector * (1 - output_vector)
		self.weights_ho += self.learning_rate * np.dot(desired_change, hidden_vector.T)

		hidden_errors = np.dot(self.weights_ho.T, output_errors)
		desired_change = hidden_errors * hidden_vector * (1 - hidden_vector)
		self.weights_ih += self.learning_rate * np.dot(desired_change, input_vector.T)

		return output_errors



	def run(self, input_vector):
		input_vector = np.array(input_vector, ndmin=2).T

		output_vector = expit(np.dot(self.weights_ih, input_vector))
		output_vector = expit(np.dot(self.weights_ho, output_vector))

		return output_vector