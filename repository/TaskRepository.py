from entity import Task
import sqlite3 as sq
from decouple import config

class TaskRepository():
    global cur
    global sqlite_connection

    sqlite_connection = sq.connect(config("path_to_db"))
    cur = sqlite_connection.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT)
    """)

    sqlite_connection.commit()
    sqlite_connection.close()

    def add_task(self, task: Task.Task):
        sqlite_connection = sq.connect(config("path_to_db"))
        cur = sqlite_connection.cursor()
        cur.execute("INSERT INTO tasks (name, label_id) VALUES (?, ?)", (task.text, task.label_id, ))
        sqlite_connection.commit()
        sqlite_connection.close()
        
    def delete_task(self, id: int):
        sqlite_connection = sq.connect(config("path_to_db"))
        cur = sqlite_connection.cursor()
        cur.execute(f"DELETE FROM tasks WHERE id = {id}")
        sqlite_connection.commit()
        sqlite_connection.close()    
        
    def get_tasks_list(self, label_id = None) -> list:
        sqlite_connection = sq.connect(config("path_to_db"), check_same_thread=False)
        cur = sqlite_connection.cursor()

        if label_id != None:
             items = cur.execute(f"SELECT * FROM tasks WHERE label_id = ?", (label_id,))
        else:
            items = cur.execute("SELECT * FROM tasks")
        
        items_list = []
        for item in items:
            data = {
                'id': item[0],
                'text': item[1],
                'label_id': item[2]
            }
            task = Task.Task(**data)
            items_list.append(task)
        return items_list