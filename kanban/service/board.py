from dataclasses import dataclass

from kanban.domain.model import Board


@dataclass(frozen=True)
class NewBoardCommand:
    name: str


@dataclass(frozen=True)
class NewColumnCommand:
    id: str
    col_name: str


class NewBoardHandler:

    def __init__(self, board_repo):
        self.repo = board_repo

    def __call__(self, cmd):
        board = Board.create(name=cmd.name)
        self.repo.put(board)


class NewColumnHandler:

    def __init__(self, board_repo):
        self.repo = board_repo

    def __call__(self, cmd):
        board = self.repo.board_by_id(cmd.id)
        board.add_column(cmd.col_name)
        self.repo.put(board)


class ListBoardsQuery:

    def __init__(self, board_repo):
        self.repo = board_repo

    def __call__(self, presenter):
        data = self.repo.list_boards()
        return presenter(data)
