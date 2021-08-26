import pytest
from kanban.domain.model import Board, WorkItem
from kanban.infrastructure.repos.orm import sql_session as real_sql_session


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


@pytest.fixture(scope='function')
def sql_session():
    return real_sql_session('sqlite://')  # inmem
