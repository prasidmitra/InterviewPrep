from abc import ABC, abstractmethod

from checkerboard.cell import Cell
from checkerboard.color import Color
from checkerboard.position import Position


class Board(ABC):
    def __init__(self, board_size: int):
        self.size = board_size
        self.cells: list[list[Cell]]

    @abstractmethod
    def _create_checkerboard_cells(self):
        pass

    @abstractmethod
    def initialize_board(self):
        pass

    @abstractmethod
    def make_move(self, start: Position, end: Position):
        pass


class ChessBoard(Board):
    def __init__(self):
        super().__init__(8)
        self.cells = self._create_checkerboard_cells()

    def _create_checkerboard_cells(self):
        return [[Cell(Color.WHITE if (i + j) % 2 == 0 else Color.BLACK) for i in range(self.size)] for j in range(self.size)]

    def initialize_board(self):
        pass

    def _is_valid_move(self, start: Position, end: Position):
        return self.cells[start.x][start.y].piece.is_valid_move(start, end, self) and not self._is_king_in_check(start, end)

    def _is_king_in_check(self, start: Position, end: Position):
        pass

    def make_move(self, start: Position, end: Position):
        if self._is_valid_move(start, end):
            self.cells[end.x][end.y].piece = self.cells[start.x][start.y].piece
            self.cells[start.x][start.y].piece = None

