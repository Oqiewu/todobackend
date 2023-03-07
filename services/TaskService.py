from repository import TaskRepository
from entity import Task

class TaskService():
    def __init__(self, task_repository: TaskRepository.TaskRepository):
        self.task_repository = task_repository


    def add_task(self, task: Task.Task):
        self.task_repository.add_task(task)
    
    def delete_task(self, id: int):
        return self.task_repository.delete_task(id)
    
    def get_tasks_list(self):
        return self.task_repository.get_tasks_list()
