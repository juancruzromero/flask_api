""" API initialization script """

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Video(db.Model):
    """ Video Model """
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    duration = db.Column(db.Integer)
    quality = db.Column(db.String(2)) # HD, 4K?
    browser_data = db.Column(db.String(200))

    def __init__(self, url, duration, quality, browser_data):
        self.url = url
        self.duration = duration
        self.quality = quality
        self.browser_data = browser_data

    def __repr__(self):
        return f'<Broser DATA {self.browser_data}>'

class VideoSchema(ma.Schema):
    """ Video Schema """
    class Meta:
        fields = ('url', 'duration', 'quality')

task_schema = VideoSchema()
tasks_schema = VideoSchema(many=True)

# Views:
@app.route('/')
def index():
    """ Index view """
    return "<h1 style='color': red>Hello from flask!</h1>"

@app.route('/videos/<id>', methods=['GET'])
def get_video(id):
    """ Get video view """
    task = Video.query.get(id)
    return task_schema.jsonify(task)

@app.route('/video', methods=['POST'])
def create():
    url = request.json['url']
    duration = request.json['duration']
    quality = request.json['quality']
    broser_data = str(request.headers.get('User-Agent')) # Not remote_user xD
    new_task = Video(url, duration, quality, broser_data)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)
    
if __name__ == '__main__':
    app.run(debug=True)
