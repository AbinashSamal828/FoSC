
from flask import Flask,render_template,request,redirect
import os
import sqlite3

currentlocation=os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")
@app.route("/",methods=["POST"])
def checklogin():
    UN=request.form['Username']
    PW=request.form['Password']

    sqlconnection=sqlite3.Connection(currentlocation+"/Login.db")

    cursor=sqlconnection.cursor()
    query1="SELECT Username, Password From Users WHERE Username='{un}' AND Password='{pw}'".format(un=UN,pw=PW)

    rows=cursor.execute(query1)
    rows=rows.fetchall()
    if len(rows)==1:
        return render_template("index.html")
    else:
        return redirect("/register")

@app.route("/register",methods=["GET","POST"])
def registerpage():
    if request.method=="POST":
        nUN=request.form['NUsername']
        nPW=request.form['NPassword']
        Uemail=request.form['Email']

        sqlconnection=sqlite3.Connection(currentlocation+"/Login.db")
        cursor=sqlconnection.cursor()
        query1="INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u=nUN,p=nPW,e=Uemail)
        cursor.execute(query1)
        sqlconnection.commit()
        return redirect("/")
    return render_template("register.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/aboutus")
def about():
    return render_template("aboutus.html")

@app.route("/contactus")
def contact():
    return render_template("contact.html")

@app.route("/howitworks")
def howitworks():
    return render_template("howitworks.html")

if (__name__=="__main__"):
    app.run(debug=True )