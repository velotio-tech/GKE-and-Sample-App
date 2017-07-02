"""
Simple Python App to demonstrate delpoyment using GKE
This app will run in one container and will connect
with MySQL database running as another container using service name
"""

from flask import Flask, request
app = Flask(__name__)
import MySQLdb
conn = ""


def get_db_conn(host, user, passwd, db):
    """
    Get connection to MySQL database
    """

    global conn
    if not conn.open:
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    return conn


def db_init(host, user, passwd, db):
    """
    Initialize the database by creating employee table
    """

    global conn
    try:
        conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        cur=conn.cursor()
        cur.execute("show tables like 'employee'")
        if not cur.rowcount:
            cur.execute("create table employee(id int, name varchar(20))")
            conn.commit()
        else:
            print "Database table already present"
    except Exception as msg:
        print "Exception while initializing database : %s"%msg


@app.route('/')
def greet():
    """
    Greet to visitors of url http://IP:5000/
    """

    return 'Valar Morghulis!!'


@app.route("/storedata", methods=["POST"])
def store_data():
    """
    Store the employee data in database and return msg
    """

    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
        cur.execute("insert into employee values (%s, '%s')"%(request.form['id'], request.form['name']))
        conn.commit()
        msg = "Inserted Data for Employee : %s"%(request.form['name'])
    except Exception as msg:
        print "Exception : %s"%(msg)
        msg = "Exception while inserting data %s"%(msg)
    return msg


@app.route("/getdata/<int:id>", methods=["GET"])
def get_data(id):
    """
    Get Employee data using Employee ID
    """

    try:
        conn = get_db_conn(host="mysql-service.default", user="root", passwd="admin", db="admin")
        cur = conn.cursor()
        cur.execute("select * from employee where id=%d"%id)
        if cur.rowcount:
            res = cur.fetchone()
            msg = "Employee Details ID : %d  Name : %s"%(res[0], res[1])
        else:
            msg = "Data for Employee ID : %d not present"%(id)
    except Exception as msg:
        print "Exception : %s"%(msg)
        msg = "Exception while fetching data %s"%(msg)
    return msg


if __name__ == '__main__':
    db_init(host="mysql-service.default", user="root", passwd="admin", db="admin")
    app.run(host="0.0.0.0", port=5000)
