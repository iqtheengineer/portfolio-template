from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

name="Iman Crooks"
role="Cloud Engineer"
phone="555-555-5555"
email="recruitimancrooks@gmail.com"
location="Charlotte, NC"


@app.route("/")
def index():
    return render_template("index.html", 
    name=name,
    role=role,
    phone=phone,
    email=email
    )

if __name__ == "__main__":
    app.run(debug=True)