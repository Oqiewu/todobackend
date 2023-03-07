from entity import Label
import sqlite3 as sq

class LabelRepository():
    global cur
    global sqlite_connection

    def add_label(self, label: Label.Label):
        sqlite_connection = sq.connect("./db/tasks.db")
        sqlite_connection.execute("PRAGMA foreign_keys = ON")
        cur = sqlite_connection.cursor()

        cur.execute("INSERT INTO label (name) VALUES (?)", (label.name,))
        sqlite_connection.commit()
        

    def delete_label(self, id: int):
        sqlite_connection = sq.connect("./db/tasks.db")
        sqlite_connection.execute("PRAGMA foreign_keys = ON")
        cur = sqlite_connection.cursor()
        cur.execute(f"DELETE FROM label WHERE id = {id}")
        sqlite_connection.commit()
        sqlite_connection.close()    
        

    def get_labels_list(self) -> list:
        sqlite_connection = sq.connect("./db/tasks.db", check_same_thread=False)
        sqlite_connection.execute("PRAGMA foreign_keys = ON")
        cur = sqlite_connection.cursor()

        items = cur.execute("SELECT * FROM label")
        
        items_list = []
        for item in items:
            data = {
                'id': item[0],
                'name': item[1]
            }
            label = Label.Label(**data)
            items_list.append(label)
        return items_list