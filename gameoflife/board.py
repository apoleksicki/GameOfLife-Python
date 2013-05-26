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
    return board(x)(y)

def generateNewCell(point, board):
    cell = getCell(point, board) 
    aliveNeighbors = reduce(lambda x,y: x + y, map(getCell, generateNeighborIndex(point, board)))
    
    if DEAD == cell:
        if aliveNeighbors == 3:
            return ALIVE
        else:
            return DEAD
    elif aliveNeighbors == 2 or aliveNeighbors == 3:
        return ALIVE
        
    

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
    
class Board(object):
    pass


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


#if __name__ == "__main__":
#    #import sys;sys.argv = ['', 'Test.testName']
#    unittest.main()