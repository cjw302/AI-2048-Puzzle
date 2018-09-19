#AIM: PLAYER_AI GETS THE NEXT MOVE FOR THE PLAYER 
# Edit for a demo

from BaseAI_3 import BaseAI
from Helper import *
from Minimaxab import *
from Grid_3 import *
import numpy as np

class PlayerAI(BaseAI):
	def getMove(self, grid):
		moves = grid.getAvailableMoves()
		maxUtility = -np.inf
		nextDir = -1

		#for move in moves:
		#	child = getChild(grid, move)
#	
#			utility = Decision(grid=child, max=False) 
#
#			if utility >= maxUtility:
#				maxUtility = utility
#				nextDir = move
		nextDir = random.choice(moves)
		return nextDir


