from fastapi import FastAPI

from kanban.domain.model.workitem import Repository as WorkItemRepo
from kanban.domain.model.board import Repository as BoardRepo
# from kanban.service.workitem import NewWorkItemCommand, NewWorkItemHandler
from kanban.service.board import NewBoardCommand, NewBoardHandler

from pydantic import BaseModel


class NewBoard(BaseModel):
    name: str


def create_rest_app(board_repo: BoardRepo, work_item_repo: WorkItemRepo):

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.post('/board')
    def post_new_board(board: NewBoard):
        cmd = NewBoardCommand(board.name)
        handler = NewBoardHandler(board_repo)
        handler(cmd)
        print(cmd)

    return app
