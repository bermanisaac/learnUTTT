class tttGame:
    board = [0,0,0,0,0,0,0,0,0,0]
    nextMove = 1

    def makeUserMove(self):
        square = int(input())
        self.board[square] = self.nextMove
        self.nextMove *= -1
        self.print()

    def checkWin(self):
        if self.board[0] == self.board[1] == self.board[2] or
           self.board[0] == self.board[4] == self.board[8] or
           self.board[0] == self.board[3] == self.board[6]
           return self.board[0]

        if self.board[6] == self.board[7] == self.board[8] or
           self.board[1] == self.board[4] == self.board[7]
           return self.board[7]

        if self.board[3] == self.board[4] == self.board[5] or
           self.board[2] == self.board[5] == self.board[8] or
           self.board[3] == self.board[5] == self.board[6]):
           return self.board[5]

    def print(self):
        for i in range(3):
            print(self.board[i], end = '')
        print('')
        for i in range(3,6):
            print(self.board[i], end = '')
        print('')
        for i in range(6,9):
            print(self.board[i], end = '')
        print('')


def main():
    game = tttGame()
    game.print()
    game.makeUserMove()
    game.makeUserMove()


if(__name__ == "__main__"):
    main()
