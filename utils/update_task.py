
# The user must be able to select the id of the task they wish to update
# The function in requests to issue a PUT request is literally put.
# response = requests.put(URL, json=your_data)import requests

URL= "http://127.0.0.1:5000/tasks"

def update_task(name, summary, description):
    task_data = {
        "name": name,
        "summary": summary,
        "description": description
    }
    response = requests.put(URL, json=task_data)
    if response.status_code == 204:
        print("Task successfully updated!")
    else:
        print("Task creation failed.")


if __name__ == "__main__":
    print("Update a task:")
    name = input("Name: ")
    summary = input("Summary: ")
    description = input("Description: ")
    update_task(name, summary, description)