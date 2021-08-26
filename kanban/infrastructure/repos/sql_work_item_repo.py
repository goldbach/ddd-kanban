from kanban.domain.model.workitem import WorkItem, Repository


class SQLWorkItemRepo(Repository):

    def __init__(self, session):
        self.session = session

    def put(self, work_item: WorkItem):
        self.session.add(work_item)
        self.session.commit()

    def work_item_by_id(self, id):
        return self.session.query(WorkItem)\
            .filter(WorkItem._id == id).one_or_none()

    def list_items(self):
        return self.session.query(WorkItem).all()
