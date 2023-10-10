from abc import ABC, abstractmethod

from low_level_design.checkerboard.board import Board
from low_level_design.checkerboard.color import Color
from low_level_design.checkerboard.position import Position


class Piece(ABC):
    def __init__(self, color: Color):
        self.color = color

    @staticmethod
    @abstractmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        pass


class King(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return True if end.is_valid_position(board) and start.direct_distance(end) == 1 else False


class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return False


class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return False


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return False


class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return False


class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(color)

    @staticmethod
    def is_valid_move(start: Position, end: Position, board: Board) -> bool:
        return False
