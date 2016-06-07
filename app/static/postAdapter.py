from flask import jsonify,request
import sqlite3

def create_database():
    db = sqlite3.connect('database.db')
    db.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    db.close()
    return "database created"


def add_student(n, a, c, p):
    msg = ""
    if request.method == 'POST':
      try:
         with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin)VALUES (?,?,?,?)",(n,a,c,p) )
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return msg
         con.close()
    else:
        return "not post"


def update(n,a,c,p):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    if(n is not None):
        cur.execute("update students set name = '%s' where name = '%s'" % (n,n))
    if(a is not None):
        cur.execute("update students set addr = '%s' where name = '%s'" % (a,n))
    if(c is not None):
        cur.execute("update students set city = '%s' where name = '%s'" % (c,n))
    if(p is not None):
        cur.execute("update students set pin = '%s' where name = '%s'" % (p,n))

    con.commit()
    cur.close()

def update_this(name,n,a,c,p):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    if(n is not None):
        cur.execute("update students set name = '%s' where name = '%s';" % (n,name))
    if(a is not None):
        cur.execute("update students set addr = '%s' where name = '%s';" % (a,name))
    if(c is not None):
        cur.execute("update students set city = '%s' where name = '%s';" % (c,name))
    if(p is not None):
        cur.execute("update students set pin = '%s' where name = '%s';" % (p,name))

    con.commit()
    cur.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def show_database():
   con = sqlite3.connect("database.db")
   con.row_factory = dict_factory

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall();
   return jsonify(rows)
   con.close()


def show_this_row(name):
    con = sqlite3.connect("database.db")
    con.row_factory = dict_factory

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    for i in range(len(rows)):
        if(rows[i]["name"] == name):
            return jsonify(rows[i])
    con.close()


def delete_row(name):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("delete from students where name='%s';" % (name))
    con.commit()
    cur.close()

def delete_row_this(name):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("delete from students where name='%s';" % (name))
    con.commit()
    cur.close()
