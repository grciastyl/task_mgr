from app.database import get_db

def output_formatter(results):  # converts tuple of tuples into a list of dictionaries
    out = []
    for result in results:
        res = {
            "id": result[0],
            "name": result[1],
            "summary": result[2],
            "description": result[3],
            "is_done": result[4]
        }
        out.append(res)
    return out

def scan():
    conn = get_db()  # we are creating a connection to the db
    cursor = conn.execute("SELECT * FROM task WHERE is_done=0", ())   # the data is loaded to the object in memory called "cursor" 
    results = cursor.fetchall()   # loads all the results from "cursor" into the "results" variable
    cursor.close()   # closes the object in memory "cursor" frees up the memory
    return output_formatter(results)   # returns output_formatter

def select_by_id(task_id):  #gets the task id parameter
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id=?", (task_id,))  #comma!!   The value of the tuple (task_id,) will be mapped to the quesition mark, also removes special characters
    results = cursor.fetchall()
    cursor.close()
    if results:
        return output_formatter(results)[0] #  returns only the 0 element in the list, in this case, the id
    return {}

def insert(task_data):
    task_tuple = (
        task_data.get("name"), task_data.get("summary"),  ## looks in the dictionary task_data for specified key, then returns the value otherwise returns none
        task_data.get("description")                      ## without .get, if it doesnt exist, it will crash the program
    )
    statement = """
        INSERT INTO task (
            name,
            summary,
            description
        ) VALUES (?,?,?)
    """  ## three quotes means its a multi-line string

    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def update_by_id(task_data, task_id):
    task_tuple = (
        task_data.get("name"), task_data.get("summary"),
        task_data.get("description"), task_data.get("is_done"),
        task_id
    )
    statement = """
        UPDATE task
            SET
                name=?,
                summary=?,
                description=?,
                is_done=?
        WHERE id=?
    """

    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def delete_by_id(task_id):
    conn = get_db()
    conn.execute("DELETE FROM task WHERE id=?", (task_id,)) #comma!!
    conn.commit()

    def deactivate_task(task_id):
        conn = get_db()
        conn.execute("UPDATE task SET is_done=1 WHERE id=?", (task_id,))
        conn.commit()