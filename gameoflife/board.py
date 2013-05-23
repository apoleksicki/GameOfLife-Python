'''
Created on 23/05/2013

@author: Antek
'''
import unittest

def boardParser(toParse):
    return toParse.split('\n')

def generateNewCell(board, x, y):
    pass

def generateNeighborIndex(point, board):
    allNeighbors = []
    allNeighbors.append(Point(point.x - 1, point.y - 1))
    allNeighbors.append(Point(point.x - 1, point.y))
    allNeighbors.append(Point(point.x - 1, point.y + 1))
    allNeighbors.append(Point(point.x, point.y + 1))
    allNeighbors.append(Point(point.x, point.y - 1))
    allNeighbors.append(Point(point.x + 1, point.y - 1))
    allNeighbors.append(Point(point.x + 1, point.y))
    allNeighbors.append(Point(point.x + 1, point.y + 1))
    return [neighbor for neighbor in allNeighbors if neighbor.x >= 0 and neighbor.x < len(board) and neighbor.y >= 0 and neighbor.y < len(board[0])  ]
    
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        '''
        Overrides str
        '''
        return 'X: %s Y: %s' % (self.x, self.y)
        

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