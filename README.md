AI-final
========

This is a simple maze solving game who's sole purpose is to find the optimal path from a start to finish.

To get started the quick and dirty way, simply run `$ python Engine.py` to solve one of the mazes embded in the Engine.py file.

To have some more fun with the solver, `cd` into the directory containing this projects and run python `$ python`. Then paste the following into the interpreter.

    from Maze import *
    
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
    	[wal,wal,wal," ",wal," "," ",wal," ",wal," ",wal]
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


Then instantiate the game with one of the mazes above.

    game = Board(maze1)
OR

    game = Board(maze2)

To take a single step

    game.step()

Each step should print the game board, but if you want to print the Board anyways, do:
 
    game
OR

    print game

To solve the puzzle do:

    game.solve()


If at any point you want to see the game's state, you can access the attributes such as _exploreHeap by:

    print game._exploreHeap
