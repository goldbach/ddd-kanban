from dataclasses import asdict

from kanban.domain.model.board import Board, Column, Repository


class InMemBoardRepo(Repository):

    _boards = {}

    def __init__(self, initial_lst=None):
        if initial_lst is not None:
            for item in initial_lst:
                self._boards[item.id] = item

    def put(self, board: Board):
        self._boards[board.id] = asdict(board)

    def board_by_id(self, id):
        obj = self._boards[id]
        b = Board(**obj)
        b._columns = [Column(**x) for x in b._columns]
        return b
