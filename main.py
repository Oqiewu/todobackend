import uvicorn
from fastapi import FastAPI, Body
from entity import Task, Label, User
from services import TaskService, LabelService, UserService
from repository import TaskRepository, LabelRepository, UserRepository
from fastapi.middleware.cors import CORSMiddleware
from auth.Jwt_handler import signJWT
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

#user requests
@app.post('/user/signup')
def create_user(user: User.CreateUser):
    repo = UserRepository.UserRepository()
    service = UserService.UserService(repo)
    service.add_user(user)
    return signJWT(user.email)

def check_user(data: User.LoginUser):
    repo = UserRepository.UserRepository()
    service = UserService.UserService(repo)
    users = service.get_users()
    for user in users:
        if user.email == data.email and user.hashed_password == data.hashed_password:
            return True
    
@app.post("/user/login")
def user_login(user: User.LoginUser):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details!"
        }

@app.delete('/user/{id}')
def delete_user(id: int):
    repo = UserRepository.UserRepository()
    service = UserService.UserService(repo)
    service.delete_user(id)
    return "Successful!"

@app.get("/users")
def get_users():
    repo = UserRepository.UserRepository()
    service = UserService.UserService(repo)
    return service.get_users()

uvicorn.run(app)