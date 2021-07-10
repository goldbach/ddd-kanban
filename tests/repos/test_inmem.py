from kanban.domain.model import WorkItem
from kanban.infrastructure.repos.inmem_work_item_repo import InMemWorkItemRepo


def test_inmem_putget_workitem():
    data = {
        'name': 'title',
        'description': 'some text',
    }
    task = WorkItem.create(**data)
    repo = InMemWorkItemRepo()
    repo.put(task)

    retrieved_task = repo.work_item_by_id(task.id)
    assert retrieved_task == task
    assert retrieved_task is not task
