from dataclasses import asdict

from kanban.domain.model.workitem import WorkItem, Repository


class InMemWorkItemRepo(Repository):

    def __init__(self, initial_lst=None):
        self._items = {}
        if initial_lst is not None:
            for item in initial_lst:
                self._items[item.id] = item

    def put(self, work_item: WorkItem):
        self._items[work_item.id] = asdict(work_item)

    def work_item_by_id(self, id):
        obj = self._items[id]
        return WorkItem(**obj)

    def list_items(self):
        return [WorkItem(**x) for x in self._items.values()]
