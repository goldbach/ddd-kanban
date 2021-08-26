
import click

from kanban.service.workitem import NewWorkItemCommand
from kanban.service.board import NewBoardCommand
from kanban.service.board import NewColumnCommand


def cli_list_item_presenter(data):
    for item in data:
        print(f'{item.id[:6]}\t{item.name}')


def cli_list_boards_presenter(data):
    for item in data:
        print(f'{item.id}\t{item.name}: {[col.name for col in item.get_columns()]}')


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
        q = app_config['queries']['list_boards']
        q(cli_list_boards_presenter)

    @board.command(name='new')
    @click.argument('name')
    def board_new(name):
        cmd = NewBoardCommand(name)
        app_config['handlers']['new_board'](cmd)

    @board.command(name='col')
    @click.argument('id')
    @click.argument('col_name')
    def board_new_col(id, col_name):
        cmd = NewColumnCommand(id, col_name)
        app_config['handlers']['new_column'](cmd)

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
