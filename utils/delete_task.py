
# The user must specify the ID of the task they wish to delete.
# The function in requests to issue a DELETE request is literally delete.
# response = requests.delete(URL)

import requests

URL= "http://127.0.0.1:5000/tasks"

def delete_task(task_id):
    task_data = {
        "id": task_id
    }
    response = requests.delete(URL, json=task_data)
    if response.status_code == 204:
        print("Task successfully deleted!")
    else:
        print("Task deletion failed.")
