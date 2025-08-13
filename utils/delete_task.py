
# The user must specify the ID of the task they wish to delete.
# The function in requests to issue a DELETE request is literally delete.
# response = requests.delete(URL)

import requests

URL= "http://127.0.0.1:5000/tasks"

def delete_task(name, summary, description):
    task_data = {
        "name": name,
        "summary": summary,
        "description": description
    }
    response = requests.delete(URL)
    if response.status_code == 204:
        print("Task successfully created!")
    else:
        print("Task creation failed.")
