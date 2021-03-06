import random

class GameLogic:

	@staticmethod
	def get_scorers(test_input):
		truthy_scorers = []
		numberCounts = {
			6: 0,
			5: 0,
			4: 0,
			3: 0,
			2: 0,
			1: 0,
		}
		
		for value in test_input:
				numberCounts[value] += 1

		pairs = 0
		for value in numberCounts:
			if numberCounts[value] == 2:
				pairs+=1
		if pairs == 3:
			for value in numberCounts:
				if numberCounts[value] == 2:
					truthy_scorers.extend([value, value])

		straight = True
		for value in numberCounts:
			if numberCounts[value] != 1:
				straight = False
		if straight:
			truthy_scorers.extend([1, 2, 3, 4, 5, 6])

		if not len(truthy_scorers):
			for value in numberCounts:
				value_type = [value for i in range(numberCounts[value])]
				if GameLogic.calculate_score(value_type):
					truthy_scorers.extend(value_type)

		truthy_scorers.sort()
		return tuple(truthy_scorers)

	@staticmethod
	def validate_keepers(diceroll, keepers):
		no_cheat = True
		roll_list = [value for value in diceroll]
		for value in keepers:
			if value not in roll_list:
				no_cheat = False
			else:
				roll_list.remove(value)
		return no_cheat

	@staticmethod
	def calculate_score(diceroll):
		points = 0
		## START COUNTING DIE
		numberCounts = {
			6: 0,
			5: 0,
			4: 0,
			3: 0,
			2: 0,
			1: 0,
		}
		for value in diceroll:
			numberCounts[value] += 1
		## END COUNTING DIE

		## START CHECKING FOR PAIRS
		pairs = 0
		for value in numberCounts:
			if numberCounts[value] == 2:
				pairs+=1
		if pairs == 3:
			return 750
		## END CHECKING FOR PAIRS

		## START CHECKING FOR A STRAIGHT
		else:
			#rework for less than 6 die
			straight = True
			for value in numberCounts:
				if numberCounts[value] != 1:
					straight = False
			if straight:
				return 1500
		## END CHECKING FOR A STRAIGHT

		## START BASE CASES
			for value in numberCounts:
				if value != 1 and numberCounts[value] > 2:
					points += value*100*(numberCounts[value]-2)
				elif value == 1:
					if numberCounts[value] < 3:
						points += 100*numberCounts[value]
					else:
						points += 1000*(numberCounts[value]-2)
				elif value == 5:
					points += 50*numberCounts[value]
			return points

	

	@staticmethod
	def roll_dice(count):
		## PREVENT BAD USER INPUTS
		if type(count) is not int:
			count = 6
		count = max(min(count, 6), 1)

		# GENERATE THE TUPLE
		return(tuple(random.randint(1, 6) for i in range(count)))

class Banker:

	def __init__(self):
		self.total = 0
		self.shelved = 0

	def shelf(self, points=0):
		self.shelved += points

	def bank(self):
		roundPoints = self.shelved
		self.total += roundPoints
		self.shelved = 0
		return roundPoints

	def clear_shelf(self):
		self.shelved = 0