from dataclasses import dataclass
from abc import ABC, abstractmethod

from .entity import Entity


@dataclass
class WorkItem(Entity):
    name: str
    description: str


class Repository(ABC):

    @abstractmethod
    def put(self, work_item):
        raise NotImplementedError

    @abstractmethod
    def work_item_by_id(self, id):
        raise NotImplementedError
