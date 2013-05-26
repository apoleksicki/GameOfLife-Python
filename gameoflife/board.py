'''
Created on 23/05/2013

@author: Antek
'''
import unittest

class Board(object):
    ALIVE = 1
    DEAD = 0
    
    def __init__(self, board):
        self.board = board
    
    def _getCell(self, point):
        x, y = point
        return self.board[x][y]
    
    def _generateNewCell(self, coord, board):
        cell = self._getCell(coord) 
        aliveNeighbors = reduce(lambda x,y: x + y, map(lambda point: self._getCell(point), self._generateNeighborCoords(coord)))
        
        if cell == Board.DEAD:
            if aliveNeighbors == 3:
                return Board.ALIVE
            else:
                return Board.DEAD
        elif aliveNeighbors == 2 or aliveNeighbors == 3:
            return Board.ALIVE
        else:
            return Board.DEAD
            
        
    
    def _generateNeighborCoords(self, point):
        x, y = point
        allIndices = [(x - 1, y - 1),
                        (x - 1, y),
                        (x - 1, y + 1),
                        (x, y + 1),
                        (x, y - 1),
                        (x + 1, y - 1),
                        (x + 1, y),
                        (x + 1, y + 1)]
        return [(x, y) for x, y in allIndices if x >= 0 and x < len(self.board) and y >= 0 and y < len(self.board[0])]
    
    def generateNewBoard(self, board):
        result = []
        for x in range(len(board)):
            result.append([])
            for y in range(len(board[0])):
                result[x].append(self._generateNewCell((x, y), board))
        return result
       
    def __str__(self):
        result = ''
        for x in range(len(self.board)):
            line = ''
            for y in range(len(self.board[0])):
                line += str(self.board[x][y])
            result += line
        return result
    

    
class TestNewBoardGeneration(unittest.TestCase):

    def test_dead_cell_with_three_neigbors_becomes_alive(self):
        board = Board([[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]])
        self.assertEqual(Board.ALIVE, board._generateNewCell((1,0), board))
        self.assertEqual(Board.ALIVE, board._generateNewCell((1,2), board))
        
    def test_dead_cell_with_two_neigbors_remains_dead(self):
        board = Board([[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]])
        self.assertEqual(Board.DEAD, board._generateNewCell((0,0), board))
        self.assertEqual(Board.DEAD, board._generateNewCell((2,0), board))
        
    def test_dead_cell_with_more_three_neighbors_remains_dead(self):
        board = Board([[0, 1, 0, 0],
                       [0, 1, 1, 1],
                       [0, 1, 0, 1]])
        self.assertEqual(Board.DEAD, board._generateNewCell((2,2), board))
        
    def test_alive_cell_with_two_neigbors_remains_alive(self):
        board = Board([[0, 1, 0],
                       [0, 1, 0],
                       [0, 1, 0]])
        self.assertEqual(Board.ALIVE, board._generateNewCell((1,1), board))

    def test_alive_cell_with_three_neigbors_remains_alive(self):
        board = Board([[0, 1, 1],
                       [0, 1, 1],
                       [0, 0, 0]])
        self.assertEqual(Board.ALIVE, board._generateNewCell((1,1), board))
        
    def test_alive_cell_with_four_neigbors_dies(self):
        board = Board([[0, 1, 1],
                       [1, 1, 1],
                       [1, 0, 0]])
        self.assertEqual(Board.DEAD, board._generateNewCell((1,1), board))
        


#if __name__ == "__main__":
#    #import sys;sys.argv = ['', 'Test.testName']
#    unittest.main()