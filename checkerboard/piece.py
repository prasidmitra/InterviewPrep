from abc import ABC, abstractmethod

from checkerboard.board import Board
from checkerboard.color import Color
from checkerboard.position import Position


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def is_valid_move(self, start: Position, end: Position, board: Board):
        pass


class King(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return True if end.is_valid_position(board) and start.direct_distance(end) == 1 else False


class Queen(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return False


class Rook(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return False


class Knight(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return False


class Bishop(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return False


class Pawn(ABC):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board):
        return False
