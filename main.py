
import click

from kanban.infrastructure.repos.json_work_item_repo import JsonWorkItemRepo
from kanban.infrastructure.repos.json_board_repo import JsonBoardRepo
from cli import create_cli_app

PREFIX_DB = '/tmp/kanban_db'

    # board.add_column(name='ToDo')
    # board.add_column(name='WIP')
    # board.add_column(name='Done')
    # board_repo.put(board)
    # # board = board_repo.board_by_id('75d40434-9166-4895-bb22-b4032ff30519')
    # work_item_repo.put(task1)
    # work_item_repo.put(task2)
    # # task1 = work_item_repo.work_item_by_id('126d0771-ba0b-4d09-9b24-e52634a76cd9')
    # # task2 = work_item_repo.work_item_by_id('87d50db0-d9a5-4019-8a0d-7d22a83da58e')
    # board.schedule_work_item(task1)
    # board.schedule_work_item(task2)
    # board.advance_work_item(task1)


if __name__ == '__main__':

    cli_app = create_cli_app(
        JsonBoardRepo(PREFIX_DB),
        JsonWorkItemRepo(PREFIX_DB)
    )
    cli_app()
