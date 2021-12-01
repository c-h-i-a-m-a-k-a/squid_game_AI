import numpy as np
import random
import time
import sys
import os 
from BaseAI import BaseAI
from Grid import Grid
import Utils
import math

# TO BE IMPLEMENTED
# 
class PlayerAI(BaseAI):

    def __init__(self) -> None:
        # You may choose to add attributes to your player - up to you!
        super().__init__()
        self.pos = None
        self.player_num = None
    
    def getPosition(self):
        return self.pos

    def setPosition(self, new_position):
        self.pos = new_position 

    def getPlayerNum(self):
        return self.player_num

    def setPlayerNum(self, num):
        self.player_num = num

    def getMove(self, grid: Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player moves.

        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Trap* actions, 
        taking into account the probabilities of them landing in the positions you believe they'd throw to.

        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """

        max_depth = 5

        neighbors = grid.get_neighbors(self.getPosition(),True)
        opp_pos = grid.find(3-self.player_num)
        moves = []

        # Compute Heuristic for each node
        # All scores are negative, but more negative is less desirable for trapper
        for child in neighbors:
            man_dist = Utils.manhattan_distance(opp_pos, child)
            look_ahead_score = Utils.player_look_ahead_score(self.player_num,grid)
            h = -1 * (look_ahead_score + man_dist)
            moves.append(tuple([child[0],child[1],h]))

        # Implementing minimax
        def minimax(d,index,mode,moves,max_d,last_ind):
            if d == max_d:
                try:
                    return moves[index]
                except:
                    return moves[last_ind]

            # Mode: 0 --> Mininimize, 1 --> Maximize
            # Will expand later to add Max, Min, and Chance
            if mode:
                leaf_1 = minimax(d+1,index*2,False,moves,max_d,index)
                leaf_2 = minimax(d+1,index*2 + 1,False,moves,max_d,index)
                return max([leaf_1,leaf_2], key= lambda x: x[2])
            else:
                leaf_1 = minimax(d + 1, index * 2, True, moves, max_d,index)
                leaf_2 = minimax(d + 1, index * 2 + 1, True, moves, max_d,index)
                return min([leaf_1,leaf_2], key= lambda x: x[2])

        result = minimax(0,0,True,moves,round(math.log(len(moves),2)),0)

        return tuple([result[0],result[1]])

    def getTrap(self, grid : Grid) -> tuple:
        """ 
        YOUR CODE GOES HERE

        The function should return a tuple of (x,y) coordinates to which the player *WANTS* to throw the trap.
        
        It should be the result of the ExpectiMinimax algorithm, maximizing over the Opponent's *Move* actions, 
        taking into account the probabilities of it landing in the positions you want. 
        
        Note that you are not required to account for the probabilities of it landing in a different cell.

        You may adjust the input variables as you wish (though it is not necessary). Output has to be (x,y) coordinates.
        
        """


        # REMOVE LATER
        # Just using standard Opp mode as place holder

        # find all available cells in the grid
        available_cells = grid.getAvailableCells()

        # find all available cells
        trap = random.choice(available_cells) if available_cells else None

        return trap
        

    