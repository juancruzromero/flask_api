from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Models
# from models import Task


@app.route('/')
def index():
    return "<h1 style='color': red>Hello from flask!</h1>"

@app.route('/task', methods=['POST'])
def create():
    from models import Task
    content = request.json['content']
    new_task = Task(content, done=False)
    db.session.add(new_task)
    db.session.commit()
    return 'saved'

if __name__ == '__main__':
    app.run(debug=True)
