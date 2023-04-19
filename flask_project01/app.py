from flask import Flask, request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask("__name__")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/wick'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class Project(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(200),nullable=False)
    lastname=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),unique=True, nullable=False)
    password=db.Column(db.String(200),nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def fun():
    return render_template("index.html")



@app.route('/login',methods=["GET","POST"])
def log():
    if request.method=="POST":

        
        email = request.form["email"]
    
        user = Project.query.filter_by(email = email).first()
        if user is not None:
            return render_template("message.html")
        else:
            fname=request.form['firs_tname']
            lname=request.form['lastname']
            email=request.form['email']
            password=request.form['password']
            sa=request.form
            st=Project(firstname=fname,lastname=lname,email=email,password=password)
        # st=Project(fname,lname,email,password)

            db.session.add(st)
            db.session.commit()



        return render_template("success.html",dat=sa)

if __name__ == "__main__":
    app.run(debug=True)

