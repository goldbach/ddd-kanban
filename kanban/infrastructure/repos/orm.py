from sqlalchemy import create_engine, Table, MetaData, Column, String
from sqlalchemy.orm import sessionmaker, mapper
from kanban.domain.model.workitem import WorkItem
from kanban.domain.model.board import Board


metadata = MetaData()
workitem_table = Table(
    'workitem',
    metadata,
    Column('_id', String(36), primary_key=True),
    Column('name', String(256)),
    Column('description', String(4096))
)

board_table = Table(
    'board',
    metadata,
    Column('_id', String(36), primary_key=True),
    Column('name', String(256)),
)


def start_mappers():
    mapper(WorkItem, workitem_table)
    mapper(Board, board_table)


def sql_session(engine_url):
    engine = create_engine(engine_url)
    metadata.create_all(engine)
    return sessionmaker(bind=engine)()


start_mappers()
