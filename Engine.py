from Maze import *

class Engine:

	ent = ENTRANCE
	ext = EXIT
	wal = WALL

	maze1 = [
		[wal,ent,wal,wal,wal,wal,wal,wal,wal,wal,wal,wal],
		[wal," ",wal," "," "," ",wal," "," "," "," ",wal],
		[wal," ",wal," ",wal,wal,wal," ",wal,wal," ",wal],
		[wal," "," "," "," "," ",wal," "," "," "," ",wal],
		[wal,wal,wal,wal,wal," ",wal," ",wal," ",wal,wal],
		[wal," "," "," "," "," ",wal," ",wal," ",wal,wal],
		[wal," ",wal," ",wal," ",wal," ",wal," "," ",wal],
		[wal," ",wal," ",wal,wal,wal," ",wal,wal," ",wal],
		[wal," ",wal," ",wal," "," "," "," ",wal," ",wal],
		[wal," ",wal," "," "," ",wal,wal," ",wal," ",wal],
		[wal,wal,wal," ",wal," "," ",wal," ",wal," ",wal],
		[wal,wal,wal,wal,wal,wal,wal,wal,wal,wal,ext,wal]
	]

	maze2 = [
		[wal,wal,wal,wal,wal,wal,wal,wal,wal,wal,ext,wal],
		[wal," "," "," "," "," ",wal," ",wal,wal," ",wal],
		[wal," ",wal," ",wal,wal,wal," ",wal," "," ",wal],
		[wal," ",wal," "," "," "," "," ",wal," ",wal,wal],
		[wal," ",wal," ",wal,wal,wal," ",wal," "," ",wal],
		[ent," ",wal," ",wal," "," "," ",wal,wal," ",wal],
		[wal,wal,wal," "," "," ",wal," "," "," "," ",wal],
		[wal," "," "," ",wal," ",wal,wal,wal,wal," ",wal],
		[wal," ",wal,wal,wal," ",wal," "," "," "," ",wal],
		[wal," ",wal," ",wal," ",wal," ",wal,wal,wal,wal],
		[wal," "," "," ",wal," ",wal," "," "," "," ",wal],
		[wal,wal,wal,wal,wal,wal,wal,wal,wal,wal,wal,wal]
	]

	def __init__(self,*args, **kwargs):
		game = Board(self.maze2)
		game.solve()


Engine()