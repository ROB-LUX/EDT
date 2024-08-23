# id, title, description, completed, y due_date.

class Task:
    
    def __init__(self, title: str, description: str, completed: bool, 
                 due_date):
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date
        