from kanban.domain.model.board import Board, Repository


class SQLBoardRepo(Repository):

    def __init__(self, session):
        self.session = session

    def put(self, board: Board):
        self.session.add(board)
        self.session.commit()

    def board_by_id(self, id):
        return self.session.query(Board)\
            .filter(Board._id == id).one_or_none()

    def list_boards(self):
        return self.session.query(Board).all()
