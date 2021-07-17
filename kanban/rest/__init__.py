from fastapi import FastAPI

from kanban.service.workitem import NewWorkItemCommand
from kanban.service.board import NewBoardCommand

from pydantic import BaseModel
from dataclasses import asdict


class NewBoard(BaseModel):
    name: str


class NewWorkItem(BaseModel):
    name: str
    description: str


def rest_list_items_presenter(data):
    return [asdict(x) for x in data]


def create_rest_app(app_config):

    app = FastAPI()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.post('/board')
    def post_new_board(board: NewBoard):
        cmd = NewBoardCommand(board.name)
        app_config['handlers']['new_board'](cmd)

    @app.get('/workitem')
    def get_items():
        q = app_config['queries']['list_items']
        return q(rest_list_items_presenter)

    @app.post('/workitem')
    def post_new_work_item(workitem: NewWorkItem):
        cmd = NewWorkItemCommand(name=workitem.name, description=workitem.description)
        app_config['handlers']['new_work_item'](cmd)

    return app
