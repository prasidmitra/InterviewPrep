from low_level_design.checkerboard.piece import Piece
from low_level_design.checkerboard.color import Color


class Cell:
    def __init__(self, color: Color, piece: Piece = None):
        self.color: Color = color
        self.piece: Piece | None = piece
