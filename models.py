""" API Models"""

from app import db

class Video(db.Model):
    __tablename__ = 'tasks'
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
