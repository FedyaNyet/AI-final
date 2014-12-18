from Maze import *

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

if __name__ == '__main__':
	import sys
	args = sys.argv
	if len(args) < 2 or args[1] not in ["maze1", "maze2"] :
		exit("please specify which maze to run. maze1 or maze2")
	game = Board(globals()[args[1]])
	game.solve()