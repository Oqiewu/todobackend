import uvicorn
from fastapi import FastAPI
from entity import Task, Label
from services import TaskService, LabelService
from repository import TaskRepository, LabelRepository
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Task requests
@app.post('/task')
def create_task(item: Task.Task):
    repo = TaskRepository.TaskRepository()
    service = TaskService.TaskService(repo)

    service.add_task(item)

    return item

@app.get('/tasks')
def get_tasks(label_id: int = None):
    repo = TaskRepository.TaskRepository()
    service = TaskService.TaskService(repo)
    return service.get_tasks_list(label_id)

@app.delete('/task/{id}')
def delete_task(id: int):
    repo = TaskRepository.TaskRepository()
    service = TaskService.TaskService(repo)
    service.delete_task(id)
    return "Successful!"

#Label requests
@app.post('/label')
def create_label(label: Label.Label):
    repo = LabelRepository.LabelRepository()
    service = LabelService.LabelService(repo)

    service.add_label(label)

    return label

@app.get('/labels')
def get_labels():
    repo = LabelRepository.LabelRepository()
    service = LabelService.LabelService(repo)
    return service.get_labels_list()

@app.delete('/label/{id}/tasks')
def delete_label(id: int):
    repo = LabelRepository.LabelRepository()
    service = LabelService.LabelService(repo)
    service.delete_label(id)
    return "Successful!"

uvicorn.run(app)