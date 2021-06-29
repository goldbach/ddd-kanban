import os
import json

from dataclasses import asdict

from kanban.domain.model.workitem import WorkItem, Repository


class JsonWorkItemRepo(Repository):

    path = 'json_repos/workitem/'

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
