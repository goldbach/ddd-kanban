import pytest
from kanban.domain.model import Board


@pytest.fixture
def board():
    return Board.create(name='board1')
