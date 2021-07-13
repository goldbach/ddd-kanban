from dataclasses import dataclass
import uuid


def get_id():
    return str(uuid.uuid4())


@dataclass
class Entity:
    _id: str

    @classmethod
    def create(cls, **kwargs):
        new_id = get_id()
        print(f'Creating {cls} with id {new_id}')
        return cls(_id=new_id, **kwargs)

    @property
    def id(self):
        return self._id
