import pytest

from kanban.infrastructure.repos.inmem_work_item_repo import InMemWorkItemRepo
from kanban.infrastructure.repos.json_work_item_repo import JsonWorkItemRepo


@pytest.fixture(scope='function')
def inmem_workitem_repo():
    return InMemWorkItemRepo()


@pytest.fixture(scope='function')
def json_workitem_repo(tmp_path):
    return JsonWorkItemRepo(tmp_path)


@pytest.fixture(params=['json_workitem_repo', 'inmem_workitem_repo'], scope='function')
def workitem_repo(request):
    return request.getfixturevalue(request.param)


def test_repo_putget_workitem(workitem_repo, workitem):
    workitem_repo.put(workitem)

    retrieved_task = workitem_repo.work_item_by_id(workitem.id)
    assert retrieved_task == workitem
    assert retrieved_task is not workitem


def test_repo_list_workitem(workitem_repo, workitem):
    workitem_repo.put(workitem)

    tasks = workitem_repo.list_items()
    assert tasks == [workitem, ]
