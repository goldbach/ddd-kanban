import pytest

from kanban.infrastructure.repos.inmem_board_repo import InMemBoardRepo
from kanban.infrastructure.repos.json_board_repo import JsonBoardRepo


@pytest.fixture()
def inmem_board_repo():
    return InMemBoardRepo()


@pytest.fixture()
def json_board_repo(tmp_path):
    return JsonBoardRepo(tmp_path)


@pytest.fixture(params=['json_board_repo', 'inmem_board_repo'])
def board_repo(request):
    return request.getfixturevalue(request.param)


def test_repo_putget_board(board_repo, board_with_columns):
    board_repo.put(board_with_columns)

    retrieved_task = board_repo.board_by_id(board_with_columns.id)
    assert retrieved_task == board_with_columns
    assert retrieved_task is not board_with_columns
