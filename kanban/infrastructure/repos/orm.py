from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship, sessionmaker, mapper
from kanban.domain.model.workitem import WorkItem
from kanban.domain.model.board import Board, Column as BoardColumn


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

column_table = Table(
    'column',
    metadata,
    Column('_id', String(36), primary_key=True),
    Column('board_id', String(36), ForeignKey('board._id')),
    Column('name', String(256)),
)

""" workitem_ids_table = Table(
    'item_ids',
    metadata,
    Column('id', String(36), primay_key=True),
    Column('column_id', String(36), ForeignKey('column._id')),

)
 """


def start_mappers():
    mapper(WorkItem, workitem_table)
    mapper(Board, board_table, properties={
        '_columns': relationship(BoardColumn, backref='board'),
    })
    mapper(BoardColumn, column_table)


def sql_session(engine_url):
    engine = create_engine(engine_url)
    metadata.create_all(engine)
    return sessionmaker(bind=engine)()
