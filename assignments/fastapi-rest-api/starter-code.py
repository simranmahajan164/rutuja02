"""
FastAPI Task Manager REST API Starter Code

This is a starter template for building a Task Manager API.
Complete the tasks by implementing the required endpoints and functionality.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(title="Task Manager API", version="1.0.0")

# Define the Task model using Pydantic
class Task(BaseModel):
    """
    Represents a task in the Task Manager.
    - id: Unique identifier for the task
    - title: Name/title of the task
    - description: Detailed description of the task
    - completed: Boolean flag indicating if the task is completed
    """
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False


# In-memory storage for tasks (for this beginner assignment)
tasks_db = []
next_task_id = 1


# Task 1: Project Setup and Basic Endpoints
@app.get("/")
def read_root():
    """Root endpoint - welcome message"""
    return {"message": "Welcome to Task Manager API"}


@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    """
    Retrieve all tasks from the database.
    
    Returns:
        List of all tasks
    """
    # TODO: Implement this endpoint
    pass


@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    """
    Create a new task.
    
    Args:
        task: Task object to create
        
    Returns:
        The created task with an assigned ID
    """
    # TODO: Implement this endpoint
    pass


# Task 2: Retrieve and Update Endpoints
@app.get("/tasks/{task_id}", response_model=Task)
def get_task_by_id(task_id: int):
    """
    Retrieve a specific task by ID.
    
    Args:
        task_id: ID of the task to retrieve
        
    Returns:
        The requested task
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement this endpoint
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    """
    Update an existing task.
    
    Args:
        task_id: ID of the task to update
        updated_task: Task object with updated fields
        
    Returns:
        The updated task
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement this endpoint
    pass


# Task 3: Delete and Data Validation
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task by ID.
    
    Args:
        task_id: ID of the task to delete
        
    Returns:
        Success message
        
    Raises:
        HTTPException: If task is not found
    """
    # TODO: Implement this endpoint
    pass


# Run the server with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
