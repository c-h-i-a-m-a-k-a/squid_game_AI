import numpy as np
import Grid

def manhattan_distance(position, target):
        return np.abs(target[0] - position[0]) + np.abs(target[1] - position[1])

def improved_score(player_num,grid: Grid):
        opp_num = 3 - player_num
        player_free = len(grid.get_neighbors(grid.find(player_num),True))
        opp_free = len(grid.get_neighbors(grid.find(opp_num),True))
        return player_free - opp_num

def agressive_improved_score(player_num,grid: Grid):
        opp_num = 3 - player_num
        player_free = len(grid.get_neighbors(grid.find(player_num),True))
        opp_free = len(grid.get_neighbors(grid.find(opp_num),True))
        return player_free - (2*opp_num)

def player_look_ahead_score(player_num, grid: Grid):
        player_free_spots = set(grid.get_neighbors(grid.find(player_num),True))
        look_ahead_spots = set([])

        for node in player_free_spots:
                look_ahead_spots.add(node)
                neighbors = grid.get_neighbors(grid.find(player_num),True)

                for neighbor in neighbors:
                        look_ahead_spots.add(neighbor)
        return len(look_ahead_spots)

def trap_probability(position,player_num,grid: Grid):
        opp_num = 3 - player_num
        opp_pos = grid.find(opp_num)
        distance = manhattan_distance(position,opp_pos)
        p = (1-(0.05 * (distance-1)))
        return p