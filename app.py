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
        return f'<Browser data: {self.browser_data}>'

class VideoSchema(ma.Schema):
    """ Video Schema """
    class Meta:
        fields = ('url', 'duration', 'quality')

video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)

# Views:
@app.route('/')
def index():
    """ Index view """
    return "<h1 style='color': red>Hello from flask!</h1>"

@app.route('/video', methods=['POST'])
def create_video():
    url = request.json['url']
    duration = request.json['duration']
    quality = request.json['quality']
    broser_data = str(request.headers.get('User-Agent')) # Not remote_user xD
    new_video = Video(url, duration, quality, broser_data)
    db.session.add(new_video)
    db.session.commit()
    return video_schema.jsonify(new_video)

@app.route('/videos/<id>', methods=['GET'])
def get_video(id):
    """ Get video view """
    video = Video.query.get(id)
    return video_schema.jsonify(video)

@app.route('/videos', methods=['GET'])
def get_videos():
    all_videos = Video.query.all()
    result = videos_schema.dump(all_videos)
    return videos_schema.jsonify(result)

@app.route('/videos/<id>', methods=['PUT'])
def update_video(id):
    video = Video.query.get(id)
    url = request.json['url']
    duration = request.json['duration']
    quality = request.json['quality']
    video.url = url
    video.duration = duration
    video.quality = quality
    db.session.commit()
    return video_schema.jsonify(video)

@app.route('/videos/<id>', methods=['DELETE'])
def delete_video(id):
    video = Video.query.get(id)
    db.session.delete(video)
    db.session.commit()
    return video_schema.jsonify(video)

if __name__ == '__main__':
    app.run(debug=True)
