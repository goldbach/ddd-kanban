from dataclasses import dataclass
import uuid


def get_id():
    return str(uuid.uuid4())


@dataclass
class Entity:
    _id: str

    @classmethod
    def create(cls, **kwargs):
        return cls(_id=get_id(), **kwargs)

    @property
    def id(self):
        return self._id
