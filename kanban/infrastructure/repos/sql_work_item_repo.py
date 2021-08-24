from dataclasses import asdict

from kanban.domain.model.workitem import WorkItem, Repository

from sqlalchemy import create_engine, Table, MetaData, Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper, relationship


metadata = MetaData()
workitem_table = Table(
    'workitem',
    metadata,
    Column('_id', String(36), primary_key=True),
    Column('name', String(256)),
    Column('description', String(4096))
)


def start_mappers():
    mapper(WorkItem, workitem_table)


start_mappers()


def sql_session(engine_url='sqlite:///workitem.db'):
    engine = create_engine(engine_url)
    metadata.create_all(engine)
    return sessionmaker(bind=engine)()


class SQLWorkItemRepo(Repository):

    def __init__(self, session):
        self.session = session

    def put(self, work_item: WorkItem):
        self.session.add(work_item)
        self.session.commit()

    def work_item_by_id(self, id):
        return self.session.query(WorkItem)\
            .filter(WorkItem._id == id).one_or_none()

    def list_items(self):
        return self.session.query(WorkItem).all()
