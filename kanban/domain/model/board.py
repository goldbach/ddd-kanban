from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from typing import List
from .entity import Entity
from .workitem import WorkItem


@dataclass
class Column(Entity):
    name: str
    workitem_ids: List[str] = field(default_factory=list)

    def __repr__(self):
        return f"""
            {self.name}:
                {list(task for task in self.workitem_ids)}
        """


@dataclass
class Board(Entity):
    name: str
    _columns: List[Column] = field(default_factory=list)

    def add_column(self, name):
        self._columns.append(Column.create(name=name))

    def get_columns(self):
        return self._columns

    def schedule_work_item(self, task: WorkItem):
        if any([task.id in col.workitem_ids for col in self._columns]):
            print(f'{task.id} already present')
            return
        self._columns[0].workitem_ids.append(task.id)

    def advance_work_item(self, task: WorkItem):
        for idx, col in enumerate(self._columns):
            if task.id in col.workitem_ids:
                col.workitem_ids.remove(task.id)
                try:
                    self._columns[idx+1].workitem_ids.append(task.id)
                except IndexError:
                    pass
                return

    def reverse_work_item(self, task: WorkItem):
        for idx, col in enumerate(self._columns):
            if task.id in col.workitem_ids:
                col.workitem_ids.remove(task.id)
                try:
                    self._columns[idx-1].workitem_ids.append(task.id)
                except IndexError:
                    pass
                return

    def __repr__(self):
        # for col in self._columns:
        #     print(col)
        return f"""
        {self.name}:
            {list(col for col in self._columns)}
        """


class Repository(ABC):

    @abstractmethod
    def put(self, board):
        raise NotImplementedError

    @abstractmethod
    def board_by_id(self, id):
        raise NotImplementedError
