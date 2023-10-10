from dataclasses import dataclass

from checkerboard.board import Board


@dataclass
class Position:
    x: int
    y: int

    def is_valid_position(self, board: Board):
        return True if 0 <= self.x < board.size and 0 <= self.y < board.size else False

    def direct_distance(self, position):
        return max(abs(self.x - position.x), abs(self.y - position.y))

