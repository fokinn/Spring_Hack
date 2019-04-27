import requests
from flask import Flask, request, render_template, json

app = Flask(__name__)
app.secret_key = "super secret key"
#r = requests.request("/")
#json = json.loads(r)

@app.route('/springhack')
def springhack():
    return render_template('add_new_member.html')

@app.route('/springhack/add_member', methods=['POST'])
def proceed_registration():
    register_data = request.form
    first_name = register_data.get('first_name')
    #last_name = register_data.get('last_name')
    return first_name

@app.route('/springhack/login', methods = ['POST'])
def proceed_login():
    login_data = request.form
    member_id = login_data.get('member_id')
    return member_id

if __name__ == '__main__':
    app.run()