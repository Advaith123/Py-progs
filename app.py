from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, render_template, redirect, url_for


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/employee'

app.debug = True
db = SQLAlchemy(app)

class APdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    status = db.Column(db.String(20), unique=True)

    def __init__(self, username, status):
        self.username = username
        self.status = status

    def __repr__(self):
        return '<APdata %r>' % self.username

@app.route('/')
def index():
    return render_template('add_user.html')

@app.route('/post_user', methods=['POST'])
def post_user():
    apdata = APdata(request.form['username'], request.form['status'])
    db.session.add(apdata)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/drop_user', methods=['POST'])
def drop_user():
    apdata =

if __name__ == "__main__":
    app.run()