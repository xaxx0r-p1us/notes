from flask import Flask, render_template, request, session, redirect
from json import load
ba = bytearray

app = Flask(__name__)

def get_notes():
    with open("notes.json", "r") as f:
        return load(f)
        
def check_pw(login, password):
    with open("users.json", "r") as f:
        users = load(f)
        return users.get(login, None) == password

@app.route('/', methods=["GET", "POST"])
def page():
    if request.method == "POST":
        login = request.form.get("login", None)
        password = request.form.get("password", None)
        if check_pw(login, password):
            session["login"] = login
            return redirect("/")
        else:
            return render_template("login.html", wrong=True)
            
    if session.get("login", None) is not None:
        return render_template("panel.html", notes=get_notes())
    
    return render_template("login.html")

        
app.secret_key = b"supermegahacker" + ba([3, 1, 3, 3, 7]) * 3
if __name__ == '__main__':
    app.run()