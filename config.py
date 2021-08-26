
from kanban.infrastructure.repos.sql_work_item_repo import SQLWorkItemRepo
from kanban.infrastructure.repos.orm import sql_session, start_mappers

from kanban.infrastructure.repos.sql_board_repo import SQLBoardRepo

from kanban.service.workitem import NewWorkItemHandler, ListItemsQuery
from kanban.service.board import NewBoardHandler, NewColumnHandler, ListBoardsQuery

PREFIX_DB = '/tmp/kanban_db'
SQLITE_DB = 'sqlite:////tmp/kanban.sqlite'


def create_app_config():

    start_mappers()

    board_repo = SQLBoardRepo(sql_session(SQLITE_DB))
    work_item_repo = SQLWorkItemRepo(sql_session(SQLITE_DB))

    app_config = {
        'handlers': {
            'new_work_item': NewWorkItemHandler(work_item_repo),
            'new_board': NewBoardHandler(board_repo),
            'new_column': NewColumnHandler(board_repo),
        },
        'queries': {
            'list_items': ListItemsQuery(work_item_repo),
            'list_boards': ListBoardsQuery(board_repo),
        }
    }
    return app_config
