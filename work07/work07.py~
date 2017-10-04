from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def root():
    response = None
    if request.method == "POST":
        response = request.form['username']
    return render_template('echo.html', request_method = request.method, post_request = response)

if __name__ == "__main__":
    app.debug = True
    app.run()