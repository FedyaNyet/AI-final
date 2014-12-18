from Maze import *

class Engine:
	"""
	Engine and accessor class for the the Maze Board solver.
	Instantiating this class creates a new board with a predefined
	maze, and solves it.
	"""
	B  = ENTRANCE
	X  = EXIT
	O  = PATH
	WAL  = WALL

	maze1 = [
		[WAL, B ,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL],
		[WAL, O ,WAL, O , O , O ,WAL, O , O , O , O ,WAL],
		[WAL, O ,WAL, O ,WAL,WAL,WAL, O ,WAL,WAL, O ,WAL],
		[WAL, O , O , O , O , O ,WAL, O , O , O , O ,WAL],
		[WAL,WAL,WAL,WAL,WAL, O ,WAL, O ,WAL, O ,WAL,WAL],
		[WAL, O , O , O , O , O ,WAL, O ,WAL, O ,WAL,WAL],
		[WAL, O ,WAL, O ,WAL, O ,WAL, O ,WAL, O , O ,WAL],
		[WAL, O ,WAL, O ,WAL,WAL,WAL, O ,WAL,WAL, O ,WAL],
		[WAL, O ,WAL, O ,WAL, O , O , O , O ,WAL, O ,WAL],
		[WAL, O ,WAL, O , O , O ,WAL,WAL, O ,WAL, O ,WAL],
		[WAL,WAL,WAL, O ,WAL, O , O ,WAL, O ,WAL, O ,WAL],
		[WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL, X ,WAL]
	]

	maze2 = [
		[WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL, X ,WAL],
		[WAL, O , O , O , O , O ,WAL, O ,WAL,WAL, O ,WAL],
		[WAL, O ,WAL, O ,WAL,WAL,WAL, O ,WAL, O , O ,WAL],
		[WAL, O ,WAL, O , O , O , O , O ,WAL, O ,WAL,WAL],
		[WAL, O ,WAL, O ,WAL,WAL,WAL, O ,WAL, O , O ,WAL],
		[ B , O ,WAL, O ,WAL, O , O , O ,WAL,WAL, O ,WAL],
		[WAL,WAL,WAL, O , O , O ,WAL, O , O , O , O ,WAL],
		[WAL, O , O , O ,WAL, O ,WAL,WAL,WAL,WAL, O ,WAL],
		[WAL, O ,WAL,WAL,WAL, O ,WAL, O , O , O , O ,WAL],
		[WAL, O ,WAL, O ,WAL, O ,WAL, O ,WAL,WAL,WAL,WAL],
		[WAL, O , O , O ,WAL, O ,WAL, O , O , O , O ,WAL],
		[WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL,WAL]
	]

	def __init__(self,*args, **kwargs):
		game = Board(self.maze2)
		game.solve()


Engine()