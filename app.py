from kanban.rest import create_rest_app
from config import create_app_config

app = create_rest_app(create_app_config())
