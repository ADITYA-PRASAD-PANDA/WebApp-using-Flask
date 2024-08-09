from flask import Flask,render_template,request  #render template is used to load the html files and request is used to receive the data from the server

from db import Database

app=Flask(__name__) # Here app is object
dbo=Database()
@app.route('/') #this is a decorator and entry point of the webpage and as soon as the person hits the entrypoint of the webpage the index fun will run and print the output
def index():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('Register.html')

@app.route('/perform_registration',methods=['post']) #since we used method=post in <form action="/perform_registration" method="post"> so we have to write here also
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response=dbo.insert(name,email,password)

    if response:
        return "Registration Successful"
    else:
        return "email already exists"
    return name+" "+email+" "+password



app.run(debug=True) # run is a function in flask class and debug=true is written because if further we modifies anything then no need to run again and again the file