from sqlite3 import connect, Error


def createlogin():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""
                        Create table IF NOT EXISTS login(
                    name text not null,
                    user_name,
                    phone int not null,
                    login text not null,
                    password text not null,
                    log text not null
                    );
                    """)
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_create_login\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()
createlogin()


def createFan():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""
                        Create table IF NOT EXISTS fanlar(
                    id INTEGER PRIMARY KEY NOT NULL,
                    name text not null
                    );
                    """)
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_create_fan\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()
createFan()


def createSavol():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""Create table IF NOT EXISTS savol(
                    fan text not null,
                    savol text not null,
                    a text not null,
                    b text not null,
                    c text not null,
                    tj text not null,
                    id INTEGER PRIMARY KEY NOT NULL
                    );
                    """)
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_create_login\n\n\n",error)
createSavol()


def AddSavol(fan ,savol, a, b, c, tj):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""INSERT INTO savol(fan,savol, a,b,c, tj) values(?,?,?,?,?,?)""", (fan ,savol, a, b, c, tj))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_create_savol\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def addlogin(name, user_name, user_id, phone, login, password, log):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""INSERT INTO login(name, user_name,user_id, phone, login, password, log) values(?,?,?,?,?,?,?)""", (name, user_name, user_id, phone, login, password, log))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_add_login\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def AddFan(name):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""INSERT INTO fanlar(name) values(?)""", (name,))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_add_Fan\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()




def adduser(name, User_name,user_id ,savol_soni, javob_soni ,teach):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("INSERT INTO users(name, User_name,user_id,testlar_soni, javoblar_soni, teach) values(?, ?, ?, ?, ?,?)" ,(name, User_name,user_id, savol_soni, javob_soni, teach))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_add_User\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def updateLogin(login, user_id):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"UPDATE login SET login = ? WHERE user_id = ?;", (login, user_id))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_Update_login\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def updateParol(login, user_id):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"UPDATE login SET password = ? WHERE user_id = ?;", (login, user_id))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_Update_parol\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def updateLog(log, user_id):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"UPDATE login SET log = ? WHERE user_id = ?;", (log,user_id))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_Update_log\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()

def updateUser(a, b, teach, id2):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"UPDATE users SET testlar_soni = ?, javoblar_soni = ?, teach = ? WHERE user_id = ?", (a, b,teach, id2))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_update_User\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()




def readlogin():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""select * from login""")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print(f"Xato_read_login\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def readFanler():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""Select * from fanlar""")
        c = cursor.fetchall()
        return c
    except (Exception, Error) as error:
        print(f"Xato_read_Fan\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def readSavollar():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"SELECT * FROM savol")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print(f"Xato_read_savol\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def readSavollar1(id):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"SELECT * FROM savol where id={id}")
        a = cursor.fetchall()
        return a
    except (Exception, Error) as error:
        print(f"Xato_read_savol\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def readusers():
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute("""SELECT * FROM users""")
        ca = cursor.fetchall()
        return ca
    except (Exception, Error) as error:
        print(f"Xato_create_User\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()




def DeleteSavol(name):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"""DELETE FROM savol WHERE savol = ?;""", (name,))
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_del_savol\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()


def DeleteFan(name):
    try:
        create = connect("databaza.bp")
        cursor = create.cursor()
        cursor.execute(f"DELETE FROM fanlar WHERE name = '{name}';")
        create.commit()
    except (Exception, Error) as error:
        print(f"Xato_del_Fan\n\n\n",error)
    finally:
        if create:
            cursor.close()
            create.close()