class Team:

	def __init__(self, name):
		self.name = name

		self.games = 0

		self.ppg = 0
		self.oppg = 0

	def add_game(self, points, opponent_points):
		ppg = ((ppg * games) + points) / (games + 1)
		oppg = ((oppg * games) + opponent_points) / (games + 1)
		games++