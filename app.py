import requests
from flask import Flask, request, render_template, json

app = Flask(__name__)
app.secret_key = "super secret key"
#r = requests.request("/")
#json = json.loads(r)

@app.route('/springhack')
def springhack():
    return render_template('member_login.html')

@app.route('/springhack/add_member', methods=['POST'])
def proceed_registration():
    register_data = request.form
    first_name = register_data.get('first_name')
    #last_name = register_data.get('last_name')
    return first_name

@app.route('/springhack/account', methods = ['POST'])
def account():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()