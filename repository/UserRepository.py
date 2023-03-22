from entity import User
import sqlite3 as sq
from decouple import config

class UserRepository():
    global cur
    global sqlite_connection

    def add_user(self, user: User.CreateUser):
        sqlite_connection = sq.connect(config("path_to_db"))
        cur = sqlite_connection.cursor()
        cur.execute("INSERT INTO user (email, hashed_password) VALUES (?, ?)", (user.email, user.hashed_password,))
        sqlite_connection.commit()
        sqlite_connection.close() 

    def delete_user(self, id: int):
        sqlite_connection = sq.connect(config("path_to_db"))
        cur = sqlite_connection.cursor()
        cur.execute("UPDATE user SET is_active=false WHERE id = ?", (id,))
        sqlite_connection.commit()
        sqlite_connection.close() 

    def get_user(self):
        sqlite_connection = sq.connect(config("path_to_db"), check_same_thread=False)
        cur = sqlite_connection.cursor()
        users = cur.execute("SELECT * FROM user")
        items_list = []
        for item in users:
            data = {
                "id": item[0],
                "email": item[1],
                "hashed_password": item[2],
                "is_active": item[3],
                "is_superuser": item[4],
                "is_verified": item[5]
            }
            user = User.CreateUser(**data)
            items_list.append(user)

        sqlite_connection.close() 

        return items_list