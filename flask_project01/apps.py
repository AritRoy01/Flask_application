from flask import Flask, request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    database="John",
    user = "postgres",
    password = "admin",
    host = "localhost",
    port = 5432
    )


cur = conn.cursor()
# cur.execute("INSERT INTO student (first_name, last_name, phone,email,password) VALUES (%s, %s, %s,%s,%s)", ("vati cumming ", "value 2", 3,"aritroy@gmail.com","12345456"))
# cur.fetchall()
# print(a)
# conn.commit()
# cur.close()
# conn.close()
@app.route('/')
def fun():
    return render_template("index.html")



@app.route('/login',methods=["GET","POST"])
def login():
    if request.method=="POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        # cur.execute(f'''INSERT INTO student (first_name, last_name, phone,email,password) VALUES (%s, %s, %s,%s,%s)''', (f"{firstname} ", f"{lastname}", phone,f"{email}",f"{password}"))
        cur.execute(f'''INSERT INTO student (first_name, last_name, phone,email,password) VALUES (%s, %s, %s,%s,%s)''', (firstname, lastname, phone,email,password))

        conn.commit()
   
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)