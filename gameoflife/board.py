'''
Created on 23/05/2013

@author: Antek
'''
import unittest

ALIVE = 1
DEAD = 0

def boardParser(toParse):
    return toParse.split('\n')

def getCell(point, board):
    x, y = point
    return board[x][y]

def generateNewCell(point, board):
    cell = getCell(point, board) 
    aliveNeighbors = reduce(lambda x,y: x + y, map(lambda point: getCell(point, board), generateNeighborIndex(point, board)))
    
    if DEAD == cell:
        if aliveNeighbors == 3:
            return ALIVE
        else:
            return DEAD
    elif aliveNeighbors == 2 or aliveNeighbors == 3:
        return ALIVE
    else:
        return DEAD
        
    

def generateNeighborIndex(point, board):
    x, y = point
    allNeighbors = []
    allNeighbors.append((x - 1, y - 1))
    allNeighbors.append((x - 1, y))
    allNeighbors.append((x - 1, y + 1))
    allNeighbors.append((x, y + 1))
    allNeighbors.append((x, y - 1))
    allNeighbors.append((x + 1, y - 1))
    allNeighbors.append((x + 1, y))
    allNeighbors.append((x + 1, y + 1))
    return [(x, y) for x, y in allNeighbors if x >= 0 and x < len(board) and y >= 0 and y < len(board[0])]
    
class TestNewBoardGeneration(unittest.TestCase):

    def test_dead_cell_with_three_neigbors_becomes_alive(self):
        board = [[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]]
        self.assertEqual(ALIVE, generateNewCell((1,0), board))
        self.assertEqual(ALIVE, generateNewCell((1,2), board))
        
    def test_dead_cell_with_two_neigbors_remains_dead(self):
        board = [[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]]
        self.assertEqual(DEAD, generateNewCell((0,0), board))
        self.assertEqual(DEAD, generateNewCell((2,0), board))
        
    def test_dead_cell_with_more_three_neighbors_remains_dead(self):
        board = [[0, 1, 0, 0],
                 [0, 1, 1, 1],
                 [0, 1, 0, 1]]
        self.assertEqual(DEAD, generateNewCell((2,2), board))
        
    def test_alive_cell_with_two_neigbors_remains_alive(self):
        board = [[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]]
        self.assertEqual(ALIVE, generateNewCell((1,1), board))

    def test_alive_cell_with_three_neigbors_remains_alive(self):
        board = [[0, 1, 1],
                 [0, 1, 1],
                 [0, 0, 0]]
        self.assertEqual(ALIVE, generateNewCell((1,1), board))
        
    def test_alive_cell_with_four_neigbors_dies(self):
        board = [[0, 1, 1],
                 [0, 1, 1],
                 [0, 1, 0]]
        self.assertEqual(DEAD, generateNewCell((1,1), board))
        


#if __name__ == "__main__":
#    #import sys;sys.argv = ['', 'Test.testName']
#    unittest.main()