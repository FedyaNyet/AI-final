from heapq import *

WALL = "#"
ENTRANCE = "S"
EXIT = "F"
PATH = " "
EXPLORED = "."
QUEUED = "*"
NEXT = "0"
SOLUTION = "o"

class Tile(object):
	"""docstring for Tile"""

	#tile's coordintes
	_coordinates = (None, None)

	#breadcrumbs to this tile.
	_path = []

	#Tile links
	_northTile = None
	_eastTile = None
	_southTile = None
	_westTile = None
	_links = [_northTile, _eastTile, _southTile, _westTile]

	@property
	def row(self):
		return self._coordinates[0]
	
	@property
	def col(self):
		return self._coordinates[1]

	def __init__(self, coordinates):
		self._coordinates = coordinates
		super(Tile, self).__init__()

	def __repr__(self):
		return "(%d, %d)" % (self.row, self.col)
	


class Board(object):
	"""
	docstring for Board
	A class used to solve mazes.
	"""
	_isSolved = False
	_entrance = None
	_exit = None

	# a sorted queue that will contain the next to-be-explored tile at the head of the queue
	_exploreHeap = [] # stores objects in the form of (priority, tile)

	# this is a map for storring all the tiles, with the tiles as the values and keys as their coorsindates on the board.
	_tiles = {} # is built in the form of {(5,2):someTile}

	def __init__(self, maze, *args, **kwargs):
		"""
		Board instantiation takes a two dimentional array of strings in [" ",WALL,ENTRANCE,EXIT] and 
		builds a graph to connect all the tiles. It then adds the _entrance tile to _exploreHeap for solving.
		"""
		super(Board, self).__init__(*args, **kwargs)
		for row,rowArray in enumerate(maze):
			for col,cTile in enumerate(rowArray):
				if WALL in cTile: continue
				tile = Tile((row, col))
				if ENTRANCE in cTile: 
					self._entrance = tile
				elif EXIT in cTile:
					self._exit = tile
				self._tiles[(row,col)] = tile

		if not self._entrance or not self._exit:
			exit("Unable to locate maze ENTRANCE or EXIT")

		# Build the tile graph by itterate over all the tiles and settings each of their north,east,south,west tiles.
		for row,col in self._tiles:
			tile = self._tiles[(row,col)]
			try:
				tile._northTile = self._tiles[(tile.row-1, tile.col  )]
			except:
				pass
			try:
				tile._eastTile = self._tiles[(tile.row,   tile.col+1)]
			except:
				pass
			try:
				tile._southTile = self._tiles[(tile.row+1, tile.col  )]
			except:
				pass
			try:
				tile._westTile = self._tiles[(tile.row,   tile.col-1)]
			except:
				pass

		#start the exploration queue with the _entrance tile
		heappush(self._exploreHeap, (self.getDistanceToExit(self._entrance), self._entrance))

		
	def getDistanceToExit(self, tile):
		"""Returns the Manhattan distance for a given tile, to the board's _exit tile."""
		return abs(tile.row - self._exit.row) + abs(tile.col - self._exit.col)


	def step(self):
		"""
		First, sets the current tile by popping off the head of _exploreHeap. It then checks if the current tile is the exit tile. 
		If it is, it sets _isSolved to true and returns without a further step. If current tile is not the exit tile, it scans 
		the tiles directly to the north, east, south, and west of the current tile and inserts any unexplored
		tiles into the _exploreHeap with the prioty of their Manhattan distance to the exit.
		"""
		tile = heappop(self._exploreHeap)[1]
		if tile is self._exit:
			self._isSolved = True
			return
		for nextTile in [tile._northTile, tile._eastTile, tile._southTile, tile._westTile]:
			if not nextTile: continue # there's no tile in that direction!
			if nextTile._path or nextTile is self._entrance: continue # it's been explored!
			nextTile._path = tile._path + [tile]
			heappush(self._exploreHeap, (self.getDistanceToExit(nextTile), nextTile))
		print self

	def solve(self):
		"""Keeps executing step() until the maze is solved. It prints the solve path at the end."""
		while not self._isSolved:
			self.step()
		print self

	def isEnqueued(self, tile):
		"""Returns true if the provided tile is in the exploreHeap, otherwise false."""
		for i in range(len(self._exploreHeap)):
			if self._exploreHeap[i][1] != tile: continue
			return True
		return False

	def __repr__(self):
		retString = "Legend: wall:`%s` start:`%s` end:`%s` path:`%s` explored:`%s` queued:`%s` next:`%s` solution:`%s` \n" %(WALL, ENTRANCE, EXIT, PATH, EXPLORED, QUEUED, NEXT, SOLUTION)
		for row in range(0,12):
			line = ""
			for col in range(0,12):
				try:
					tile = self._tiles[(row,col)]
					if tile is self._entrance:
						charToPrint = ENTRANCE
					elif tile is self._exit:
						charToPrint = EXIT
					elif self._isSolved and tile in self._exit._path:
						charToPrint = SOLUTION
					elif self._exploreHeap[0][1] == tile:
						charToPrint = NEXT
					elif self.isEnqueued(tile):
						charToPrint = QUEUED
					elif len(tile._path)>0:
						charToPrint = EXPLORED
					else:
						charToPrint = PATH
				except:
					charToPrint = WALL
				line += charToPrint
			retString += line+"\n"
		return retString

