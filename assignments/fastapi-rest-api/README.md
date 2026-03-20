# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build a RESTful API using the FastAPI framework by creating a Task Manager API that allows users to create, read, update, and delete tasks.

## 📝 Tasks

### 🛠️ Project Setup and Basic Endpoints

#### Description
Set up your FastAPI project and create the foundational endpoints for your Task Manager API.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn
- Create a FastAPI application instance
- Define a Task model using Pydantic with fields: `id`, `title`, `description`, and `completed` (boolean)
- Implement a GET endpoint `/tasks` that returns all tasks
- Implement a POST endpoint `/tasks` that creates a new task
- Run the server successfully without errors

### 🛠️ Retrieve and Update Endpoints

#### Description
Implement endpoints to retrieve individual tasks and update existing tasks.

#### Requirements
Completed program should:

- Implement a GET endpoint `/tasks/{task_id}` that returns a specific task by ID
- Implement a PUT endpoint `/tasks/{task_id}` that updates an existing task
- Return appropriate error responses (e.g., 404) when a task is not found
- Validate that task IDs exist before attempting updates

### 🛠️ Delete and Data Validation

#### Description
Add the ability to delete tasks and implement comprehensive data validation.

#### Requirements
Completed program should:

- Implement a DELETE endpoint `/tasks/{task_id}` that removes a task
- Add validation to ensure task titles are not empty strings
- Return meaningful success messages (e.g., "Task deleted successfully")
- Handle edge cases such as deleting non-existent tasks gracefully
- Document all endpoints with proper descriptions and examples
