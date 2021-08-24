
from kanban.infrastructure.repos.json_work_item_repo import JsonWorkItemRepo
from kanban.infrastructure.repos.sql_work_item_repo import SQLWorkItemRepo, sql_session

from kanban.infrastructure.repos.json_board_repo import JsonBoardRepo

from kanban.service.workitem import NewWorkItemHandler, ListItemsQuery
from kanban.service.board import NewBoardHandler

PREFIX_DB = '/tmp/kanban_db'
SQLITE_DB = 'sqlite:////tmp/kanban.sqlite'


def create_app_config():

    board_repo = JsonBoardRepo(PREFIX_DB),
#    work_item_repo = JsonWorkItemRepo(PREFIX_DB)
    work_item_repo = SQLWorkItemRepo(sql_session(SQLITE_DB))

    app_config = {
        'handlers': {
            'new_work_item': NewWorkItemHandler(work_item_repo),
            'new_board': NewBoardHandler(board_repo),
        },
        'queries': {
            'list_items': ListItemsQuery(work_item_repo)
        }
    }
    return app_config