
# The user must be able to select the id of the task they wish to update
# The function in requests to issue a PUT request is literally put.
# response = requests.put(URL, json=your_data)import requests

URL= "http://127.0.0.1:5000/tasks"

def update_task(task_id, name, summary, description):
    task_data = {
        "name": name,
        "summary": summary,
        "description": description
    }
    response = requests.put(f"{URL}/{task_id}", json=task_data)
    if response.status_code == 204:
        print("Task successfully updated!")
    else:
        print("Task update failed.")