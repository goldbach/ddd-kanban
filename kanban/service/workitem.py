from dataclasses import dataclass

from kanban.domain.model import WorkItem


@dataclass(frozen=True)
class NewWorkItemCommand:
    name: str
    description: str


class NewWorkItemHandler:

    def __init__(self, workitem_repo):
        self.repo = workitem_repo

    def __call__(self, cmd):
        task = WorkItem.create(name=cmd.name, description=cmd.description)
        self.repo.put(task)
