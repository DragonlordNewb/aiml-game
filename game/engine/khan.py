HUMAN = "HUMAN"
KHAN = "KHAN"

class GameState:
	def __init__(self, turn: HUMAN or KHAN, **data) -> None:
		self.turn = turn
		for key in data.keys():
			setattr(self, key, data[key])
			
	def hasWon(self, player: HUMAN or KHAN) -> bool:
		return False
	
	def isOver(self) -> bool:
		return self.hasWon(HUMAN) or self.hasWon(KHAN)
			
	def getSearchTreeScore
