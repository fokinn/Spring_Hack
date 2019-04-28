import requests
from flask import Flask, redirect, request, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)

@app.route('/springhack')
def main_page():
    return redirect("/springhack/login")

@app.route('/springhack/login')
def login():
    return render_template('login_page.html')

@app.route('/springhack/account', methods=["POST"])
def account_with_posting():
    data = request.form
    session["username"] = data.get('username')
    return render_template("account_page.html")

@app.route('/springhack/team')
def team():
    return render_template("team_page.html")

@app.route('/springhack/account')
def account_without_posting():
    return render_template("account_page.html")

@app.route('/springhack/leaderboard')
def leaderboard():
    return render_template("leaderboard_page.html")

if __name__ == '__main__':
    app.run()