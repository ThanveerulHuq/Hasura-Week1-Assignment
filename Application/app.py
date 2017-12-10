from flask import Flask, render_template, request, make_response
import requests
from wtforms import Form, validators, StringField


class ReusableForm(Form):
    name = StringField('Name:', validators=[validators.required()])


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World - Thanveer</h1>"


@app.route('/authors')
def authors():
    allposts = requests.get("https://jsonplaceholder.typicode.com/posts")
    postsJson = allposts.json()
    authorposts = {}
    for post in postsJson:
        userid = post["userId"]
        if userid in authorposts:
            authorposts[userid] = authorposts[userid]+ 1
        else:
            authorposts[userid] = 1
    allUsers = requests.get("https://jsonplaceholder.typicode.com/users")
    usersJson = allUsers.json()
    usernames = {}
    for usr in usersJson:
        usernames[usr["id"]] = usr["name"]
    authorswithcount = "<h3> Author<span style='margin-left: 40px;'>count</span></h3>"
    for key, value in authorposts.items():
        authorswithcount += '<p>' + usernames[key] + '      ' + str(authorposts[key]) + '</p>'
    return authorswithcount


@app.route('/setcookie')
def cookie_insertion():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    resp = make_response()
    if name is None:
        resp.set_cookie('name', 'thanveer')
    if age is None:
        resp.set_cookie('age', '23')
    return resp


@app.route('/getcookies')
def get_cookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    if name is not None and age is not None:
        return name + " " + age
    else:
        return "<h5>No cookie found<h5>"


@app.route('/deny')
def deny():
    return "<h1>Request Denied</h1>"

@app.route('/html')
def html():
    return render_template('index.html')


@app.route('/input', methods=['GET', 'POST'])
def input():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        name = request.form['name']
        print("Entered Name==> "+name)
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
