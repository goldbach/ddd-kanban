import os
import json

from dataclasses import asdict

from kanban.domain.model.workitem import WorkItem, Repository


class JsonWorkItemRepo(Repository):

    def __init__(self, dir: str):
        self.path = os.path.join(dir, 'workitem')
        os.makedirs(self.path, exist_ok=True)

    def put(self, work_item: WorkItem):
        fh = open(os.path.join(
            self.path,
            f'{work_item.id}.json'
        ), 'w')
        json.dump(asdict(work_item), fh)

    def work_item_by_id(self, id):
        fh = open(os.path.join(
            self.path,
            f'{id}.json'
        ), 'r')
        return WorkItem(**json.load(fh))

    def list_items(self):
        ids = [x.split('.')[0] for x in os.listdir(self.path)]
        return [self.work_item_by_id(_id) for _id in ids]
