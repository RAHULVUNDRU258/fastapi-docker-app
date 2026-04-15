from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "It works!"}

@app.post ("/add-task")
def add_task(task: str):
    tasks.append(task)
    return {"tasks": tasks}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}