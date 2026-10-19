from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def register():
    return render_template("index.html")

@app.route("/map")
def admin():
    return render_template("map.html")

# response = make_response(render_template('page.html'))
# response.set_cookie('sessionId', 'value', samesite='Lax')  # или 'Strict'
# return response

if __name__ == "__main__":
    app.run(debug=True)