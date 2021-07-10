import os
import json

from dataclasses import asdict

from kanban.domain.model.board import Board, Column, Repository


class JsonBoardRepo(Repository):

    def __init__(self, dir: str):
        self.path = os.path.join(dir, 'board')
        os.makedirs(self.path, exist_ok=True)

    def put(self, board: Board):
        fh = open(os.path.join(
            self.path,
            f'{board.id}.json'
        ), 'w')
        json.dump(asdict(board), fh)

    def board_by_id(self, id):
        fh = open(os.path.join(
            self.path,
            f'{id}.json'
        ), 'r')
        b = Board(**json.load(fh))
        b._columns = [Column(**x) for x in b._columns]
        return b
