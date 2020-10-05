class tttGame:
    board = [0,1,0,1,0,1,0,1,0,1]
    nextMove = 1

    def makeMove(self):
        square = input()
        print(square)

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
    game.makeMove()
    print('fuck')


if(__name__ == "__main__"):
    main()
