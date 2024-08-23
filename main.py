from fastapi import FastAPI, HTTPException
from service.task_service import find_all_tasks, find_task_by_id

app = FastAPI()


@app.get("/")
async def root():
    return ""

@app.get("/findAll")
async def findAll():
    
    return {"tasks": find_all_tasks()}


@app.get("/findById/{task_id}")
async def findById(task_id: int = 0):
    
    if task_id == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    if type(task_id) != int:
        raise HTTPException(status_code="400", detail="Task id error")
    return find_task_by_id(task_id)
            
    
    