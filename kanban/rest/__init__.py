from fastapi import FastAPI

from kanban.domain.model.workitem import Repository as WorkItemRepo
from kanban.domain.model.board import Repository as BoardRepo
from kanban.service.workitem import NewWorkItemCommand, NewWorkItemHandler, ListItemsQuery
from kanban.service.board import NewBoardCommand, NewBoardHandler

from pydantic import BaseModel
from dataclasses import asdict


class NewBoard(BaseModel):
    name: str


class NewWorkItem(BaseModel):
    name: str
    description: str


def rest_list_items_presenter(data):
    return [asdict(x) for x in data]


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

    @app.get('/workitem')
    def get_items():
        q = ListItemsQuery(work_item_repo)
        return q(rest_list_items_presenter)

    @app.post('/workitem')
    def post_new_work_item(workitem: NewWorkItem):
        cmd = NewWorkItemCommand(name=workitem.name, description=workitem.description)
        handler = NewWorkItemHandler(work_item_repo)
        handler(cmd)

    return app
