from entity.task import Task
from datetime import date

# cada col se tomara como id
tasks = [
    Task("ejem1", "ejemdes", True, date.today()),
    Task("ejem2", "ejemde2", True, date.today()),
    Task("ejem3", "ejemde3", True, date.today()),
    Task("ejem4", "ejemde4", True, date.today()),
    Task("ejem5", "ejemde5", True, date.today()),
]

def find_all_tasks():
    if tasks != None:
        return tasks
    
def find_task_by_id(id: int)-> Task:
    
    length: int = len(tasks)
    
    if length < id: return None
    
    try:
        return tasks[id]
    except Exception:
        return  None