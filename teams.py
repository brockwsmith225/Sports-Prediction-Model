class Team:

	def __init__(self, name):
		self.name = name

		self.games = 0

		self.ppg = 0
		self.oppg = 0

	def add_game(self, points, opponent_points):
		self.ppg = ((self.ppg * self.games) + points) / (self.games + 1)
		self.oppg = ((self.oppg * self.games) + opponent_points) / (self.games + 1)
		self.games += 1