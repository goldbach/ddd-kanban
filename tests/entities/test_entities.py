import pytest

from kanban.domain.model import Board, WorkItem

@pytest.fixture()
def board_with_columns(board):
    board.add_column('col1')
    board.add_column('col2')
    board.add_column('col3')
    return board


@pytest.fixture()
def workitem():
    return WorkItem.create(name='some title', description='some text')


def test_board_can_be_created():
    data = {
        'name': 'Board1',
    }
    board = Board.create(**data)
    assert board.name == data['name']


def test_column_creation(board):
    board.add_column('col1')
    board.add_column('col2')
    assert len(board.get_columns()) == 2
    assert board.get_columns()[0].name == 'col1'
    assert board.get_columns()[1].name == 'col2'


def test_workitem_creation():
    data = {
        'name': 'title',
        'description': 'some text',
    }
    task = WorkItem.create(**data)
    assert task.name == data['name']
    assert task.description == data['description']


def test_schedule_task(board_with_columns, workitem):
    board_with_columns.schedule_work_item(workitem)
    assert workitem.id in board_with_columns._columns[0].workitem_ids


def test_assert_on_double_schedule_task(board_with_columns, workitem):
    board_with_columns.schedule_work_item(workitem)
    with pytest.raises(Exception):
        board_with_columns.schedule_work_item(workitem)


def test_advance_workitem(board_with_columns, workitem):
    board_with_columns.schedule_work_item(workitem)  # now in col1

    board_with_columns.advance_work_item(workitem)  # now in col2
    assert workitem.id not in board_with_columns._columns[0].workitem_ids
    assert workitem.id in board_with_columns._columns[1].workitem_ids

    board_with_columns.advance_work_item(workitem)  # now in col3

    with pytest.raises(Exception):  # reached end of board
        board_with_columns.advance_work_item(workitem)
