
import click

from kanban.domain.model.workitem import Repository as WorkItemRepo
from kanban.domain.model.board import Repository as BoardRepo
from kanban.service.workitem import NewWorkItemCommand, NewWorkItemHandler
from kanban.service.board import NewBoardCommand, NewBoardHandler


def create_cli_app(board_repo: BoardRepo, work_item_repo: WorkItemRepo):
    @click.group()
    def cli():
        pass

    @cli.group()
    def board():
        pass

    @cli.group()
    def workitem():
        pass

    @board.command(name='list')
    def board_list():
        print('board listing')

    @board.command(name='new')
    @click.argument('name')
    def board_new(name):
        print(f'creating board {name}')
        cmd = NewBoardCommand(name)
        handler = NewBoardHandler(board_repo)
        handler(cmd)


    @workitem.command(name='list')
    def workitem_list():
        print('workitem listing')

    @workitem.command(name='new')
    @click.argument('name')
    @click.argument('description')
    def workitem_new(name, description):
        print(f'creating workitem with {name} and desc {description}')
        cmd = NewWorkItemCommand(name, description)
        handler = NewWorkItemHandler(work_item_repo)
        handler(cmd)

    return cli
