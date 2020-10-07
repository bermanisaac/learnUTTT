import random as r

class tttGame:
    board = [0,0,0,0,0,0,0,0,0]
    nextMove = 1

    def makeAIMove(self, move):
        self.board[move] = self.nextMove
        self.nextMove *= -1
        self.print()

    def makeUserMove(self):
        square = int(input())
        self.makeAIMove(square)

    def getMoves(self):
        moveList = [0,1,2,3,4,5,6,7,8]
        for i in range(9):
            if self.board[i] != 0:
                moveList.remove(i)
        return moveList

    def checkWin(self):
        if (self.board[0] == self.board[1] == self.board[2]) or\
           (self.board[0] == self.board[3] == self.board[6]):
           if(self.board[0] != 0):
               return self.board[0]

        if (self.board[2] == self.board[5] == self.board[8]) or\
           (self.board[6] == self.board[7] == self.board[8]):
           if(self.board[8] != 0):
               return self.board[8]

        if (self.board[0] == self.board[4] == self.board[8]) or\
           (self.board[2] == self.board[4] == self.board[6]) or\
           (self.board[3] == self.board[4] == self.board[5]) or\
           (self.board[1] == self.board[4] == self.board[7]):
           if(self.board[4] != 0):
               return self.board[4]
        for square in self.board:
            if(square == 0):
                return 0

        return 2

    def print(self):
        for i in range(3):
            print(self.board[i], end = '\t')
        print('')
        for i in range(3,6):
            print(self.board[i], end = '\t')
        print('')
        for i in range(6,9):
            print(self.board[i], end = '\t')
        print('')
        print()

class randPlayer:
    def __init__(self, game):
        self.game = game

    def pickMove(self):
        moves = self.game.getMoves()
        rand = r.randrange(len(moves))
        return moves[rand]


def main():
    game = tttGame()
    randy = randPlayer(game)
    game.print()
    result = 0

    while(True):
        game.makeUserMove()
        result = game.checkWin()
        if result != 0:
            break
        AImove = randy.pickMove()
        game.makeAIMove(AImove)
        if result != 0:
            break
    if   result is 1:
        print('pog')
    elif result is -1:
        print('cringechamp')
    elif result is 2:
        print('ludwig7')



if(__name__ == "__main__"):
    main()
