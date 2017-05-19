"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import timeit
import isolation
import game_agent

from importlib import reload

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)


if __name__ == '__main__':
    #unittest.main()

    player1 = game_agent.AlphaBetaPlayer()
    player2 = game_agent.AlphaBetaPlayer()
    game = isolation.Board(player1, player2)

    #print(int(game.width / 2.), int(game.height / 2.))
    #game._board_state = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 9, 2]

    print(game.to_string())

    #if (

    
    #game.apply_move((4, 4))
    #game.apply_move((2, 6))
    print(game.to_string())

    # players take turns moving on the board, so player1 should be next to move
    assert(player1 == game.active_player)
    
    # get a list of the legal moves available to the active player
    # print(game.get_legal_moves())
    winner, history, outcome = game.play()

    print(winner)
    print(history)
    print(outcome)
    
    print(game.to_string())

    print(game._board_state)
 

