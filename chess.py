class Chess:

    @classmethod
    def f2b(cls, fen_board: str) -> list:
        board = []
        for char in fen_board:
            if char.isdigit():
                fen_board = fen_board.replace(char, int(char) * 'x')
        for row in fen_board.split('/'):
            board.append(list(row))
        return board

    @classmethod
    def b2f(cls, board: list) -> str:
        pass

    @classmethod
    def c2i(cls, coords: str) -> tuple:
        d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        return 8 - int(coords[1]), int(d[coords[0]])

    @classmethod
    def i2c(cls, *indexes) -> str:
        d = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
        return str(indexes[1]) + str(d[indexes[0]])

    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.complete: bool = False
        self.board = self.__class__.f2b(fen.split()[0])


if __name__ == '__main__':
    game = Chess()
    input()
