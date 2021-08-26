import pytest

from kanban.infrastructure.repos.inmem_board_repo import InMemBoardRepo
from kanban.infrastructure.repos.json_board_repo import JsonBoardRepo
from kanban.infrastructure.repos.sql_board_repo import SQLBoardRepo


@pytest.fixture()
def inmem_board_repo():
    return InMemBoardRepo()


@pytest.fixture()
def json_board_repo(tmp_path):
    return JsonBoardRepo(tmp_path)


@pytest.fixture()
def sql_board_repo(sql_session):
    return SQLBoardRepo(session=sql_session)


@pytest.fixture(params=['json_board_repo', 'inmem_board_repo', 'sql_board_repo'])
def board_repo(request):
    return request.getfixturevalue(request.param)


def test_repo_putget_board(board_repo, board_with_columns):
    board_repo.put(board_with_columns)

    retrieved_task = board_repo.board_by_id(board_with_columns.id)
    assert retrieved_task == board_with_columns


def test_repo_list_boards(board_repo, board):
    board_repo.put(board)

    boards = board_repo.list_boards()
    assert boards == [board, ]
