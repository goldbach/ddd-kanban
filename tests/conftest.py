import pytest
from kanban.domain.model import Board, WorkItem


@pytest.fixture
def board():
    return Board.create(name='board1')


@pytest.fixture()
def board_with_columns(board):
    board.add_column('col1')
    board.add_column('col2')
    board.add_column('col3')
    return board


@pytest.fixture()
def workitem():
    return WorkItem.create(name='some title', description='some text')
