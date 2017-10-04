from flask import Flask, render_template, request, session

global USERNAME = "yes"
global PASSWORD = "no"



app = Flask(__name__)

@app.route("/")
           
def root():
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    response = None
    errormessage = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
    if(username == USERNAME):
        if(password == PASSWORD):
            redirect(url_for('welcome'))
        else:
            errormessage = "Incorrect password"
    else:
        errormessage = "Incorrect username and maybe password"
    return render_template('echo.html', errormessage)

@app.route("/welcome")
def welcome():
    

if __name__ == "__main__":
    app.debug = True
    app.run()
