import requests
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "super secret key"
Bootstrap(app)

@app.route('/springhack')
def springhack():
    return redirect("/springhack/login")

@app.route('/springhack/login')
def springhack_login():
    return render_template('login_page.html')

@app.route('/springhack/account', methods = ['POST'])
def springhack_account():
    return render_template("account_page.html")



if __name__ == '__main__':
    app.run()