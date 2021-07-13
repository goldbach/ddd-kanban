from dataclasses import dataclass

from kanban.domain.model import Board


@dataclass(frozen=True)
class NewBoardCommand:
    name: str


class NewBoardHandler:

    def __init__(self, board_repo):
        self.repo = board_repo

    def __call__(self, cmd):
        board = Board.create(name=cmd.name)
        self.repo.put(board)
