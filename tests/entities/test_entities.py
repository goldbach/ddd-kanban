from kanban.domain.model import Board, WorkItem


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
