AI-final
========

This is a simple maze solving game who's sole purpose is to find the optimal path from a start to finish.

To get started the quick and dirty way, simply run `$ python Engine.py` to solve one of the mazes embded in the Engine.py file.

To have some more fun with the solver, `cd` into the directory containing this projects and run python `$ python`. Then paste the following into the interpreter.

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


If at any point you want to see the game's state, you can access the game's attributes such as `_exploreHeap` by printing them out to the screen. _Note that tile's are simply represented by their coordinates_

    print game._exploreHeap

To explore a Tile's runtime attributes such as it's `_northTile`, you can access the tile at `(2,10)` via the game's `_tiles` attribute in the following manner:

    game._tiles[(2,10)]._northTile
