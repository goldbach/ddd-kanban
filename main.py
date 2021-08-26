from kanban.infrastructure.repos.orm import start_mappers
from kanban.cli import create_cli_app
from config import create_app_config


if __name__ == '__main__':

    cli_app = create_cli_app(create_app_config())
    cli_app()
