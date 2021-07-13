from kanban.rest import create_rest_app
from kanban.infrastructure.repos.json_work_item_repo import JsonWorkItemRepo
from kanban.infrastructure.repos.json_board_repo import JsonBoardRepo

PREFIX_DB = '/tmp/kanban_db'

app = create_rest_app(
    JsonBoardRepo(PREFIX_DB),
    JsonWorkItemRepo(PREFIX_DB)
)