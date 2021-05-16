import sqlite3
import hashlib

# Cursor can be instantiated only once
userid = []
password = []
created_at = []
user_db_file_location = "D:/Essentials/Blue Bird ==========/Tracing/DB Browser for SQLite/Test_DBs/test.db"

con = sqlite3.connect(user_db_file_location)
cur = con.cursor()
cur.execute("SELECT * FROM users")

op = [x for x in cur.fetchall()]

for i in op:
    userid.append(i[0])
    password.append(i[1])
    created_at.append(i[2])

result= [userid,password, created_at]

print (result)


def insert(id,psd):
    if id not in list_users:
        cur.execute("INSERT INTO users (user_name, pass) VALUES (?, ?)", (id, psd))
        con.commit()
    else:
        print(f"{id} Exists")

def update(id,psd):
    cur.execute("update users SET pass = ? , modified_at = CURRENT_TIMESTAMP WHERE user_name = ?", (psd, id))
    con.commit()
    #con.close()




#insert('test1', 'test_pass')
#update('test1', 'test_pass')



#for i in cur.fetchall():
    #print(i)


