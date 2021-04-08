from ai_term2048.ai import AI
from ai_term2048.board import Board


class Bot:
    def __init__(self):
        self.ai = AI()

    def search(self, cells):
        cells = list(map(list, zip(*cells)))
        board = Board()
        board.setCells(cells)
        move = self.ai.nextMove(board)
        return self.translate(move)

    def translate(self, moveNum):
        return {1: 'up', 2: 'down', 3: 'left', 4: 'right'}[moveNum]
