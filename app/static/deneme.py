from flask import Flask, jsonify,request
import json,sqlite3


app = Flask(__name__)


def create_database():
    db = sqlite3.connect('database.db')
    db.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    db.close()
    return "database created"

def addStudent(n,a,c,p):
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

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def showDatabase():
   con = sqlite3.connect("database.db")
   con.row_factory = dict_factory

   cur = con.cursor()
   cur.execute("select * from students")

   rows = cur.fetchall();
   return jsonify(rows)
   con.close()

def deleteRow(name):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("delete from students where name='%s';" % (name))
    con.commit()
    cur.close()


@app.route('/create')
def create():
    return create_database();

@app.route('/add' , methods=['GET','POST'])
def add():
    n = request.args.get('n')
    a = request.args.get('a')
    c = request.args.get('c')
    p = request.args.get('p')
    return addStudent(n,a,c,p);

@app.route('/show' , methods=['GET'])
def show():
    return showDatabase()

@app.route('/del' , methods=['GET','POST'])
def dele():
    n = request.args.get('n')
    deleteRow(n)
    return "a"

if __name__ == "__main__":
    app.run();