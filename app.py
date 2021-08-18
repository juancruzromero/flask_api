""" API initialization script """

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    """ Index view """
    return "<h1 style='color': red>Hello from flask!</h1>"

@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    """ Get task view """
    from models import Task
    from schemas import task_schema
    task = Task.query.get(id)
    return task_schema.jsonify(task)

if __name__ == '__main__':
    app.run(debug=True)
