
import click

from kanban.service.workitem import NewWorkItemCommand
from kanban.service.board import NewBoardCommand


def cli_list_item_presenter(data):
    for item in data:
        print(f'{item.id[:6]}\t{item.name}')


def create_cli_app(app_config):
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
        cmd = NewBoardCommand(name)
        app_config['handlers']['new_board'](cmd)

    @workitem.command(name='list')
    def workitem_list():
        q = app_config['queries']['list_items']
        q(cli_list_item_presenter)

    @workitem.command(name='new')
    @click.argument('name')
    @click.argument('description')
    def workitem_new(name, description):
        print(f'creating workitem with {name} and desc {description}')
        cmd = NewWorkItemCommand(name, description)
        app_config['handlers']['new_work_item'](cmd)

    return cli
