import pytest
import requests

# CRUD
BASE_URL = (
    "http://127.0.0.1:5000"  # Base URL for the API, get this when you run the Flask app
)
tasks = []


def test_create_task():
    url = f"{BASE_URL}/tasks"
    payload = {
        "title": "Test Task",
        "description": "This is a test task.",
        "done": False,
    }
    response = requests.post(url, json=payload)
    assert (
        response.status_code == 201 or response.status_code == 200
    )  # test 1: Verify status code
    data = response.json()
    assert (
        "message" in data  # test 2: Verify that the response contains a 'message' field
    )
    assert "id" in data  # test 3: Verify that the response contains an 'id' field
    tasks.append(data["id"])  # Store the created task ID for later tests


def test_get_tasks():
    url = f"{BASE_URL}/tasks"
    response = requests.get(url)
    assert response.status_code == 200  # test 4: Verify status code
    data = response.json()
    assert "tasks" in data  # test 5: Verify that the response contains a 'tasks' field
    assert (
        "total_tasks" in data
    )  # test 6: Verify that the response contains a 'total_tasks' field


def test_get_unique_task():
    url = f"{BASE_URL}/tasks"
    if not tasks:
        pytest.skip("No tasks available to test.")  # Skip if no tasks created
    task_id = tasks[0]
    response = requests.get(f"{url}/{task_id}")
    assert response.status_code == 200  # test 7: Verify status code
    data = response.json()
    assert (
        data["id"] == task_id
    )  # test 8: Verify that the returned task ID matches the requested ID


def test_update_task():
    url = f"{BASE_URL}/tasks"
    if not tasks:
        pytest.skip("No tasks available to test.")  # Skip if no tasks created
    task_id = tasks[0]
    payload = {
        "title": "Updated Test Task",
        "description": "This is an updated test task.",
    }
    response = requests.patch(f"{url}/{task_id}", json=payload)
    assert response.status_code == 200  # test 7: Verify status code
    data = response.json()
    assert (
        "message" in data
    )  # test 8: Verify that the response contains a 'message' field


def test_done_task():
    url = f"{BASE_URL}/tasks"
    if not tasks:
        pytest.skip("No tasks available to test.")  # Skip if no tasks created
    task_id = tasks[0]
    payload = {
        "done": True,
    }
    response = requests.put(f"{url}/{task_id}", json=payload)
    assert response.status_code == 200  # test 9: Verify status code
    data = response.json()
    assert (
        "message" in data
    )  # test 10: Verify that the response contains a 'message' field


def test_delete_task():
    url = f"{BASE_URL}/tasks"
    if not tasks:
        pytest.skip("No tasks available to test.")  # Skip if no tasks created
    task_id = tasks[0]
    payload = {
        "id": task_id,
    }
    response = requests.delete(
        f"{url}/{task_id}", json=payload
    )  # Delete the task first
    assert response.status_code == 200  # test 11: Verify status code

    response = requests.get(f"{url}/{task_id}")
    assert (
        response.status_code == 404
    )  # test 12: Verify status code and that the task is deleted
