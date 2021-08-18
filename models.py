""" API Models"""

from app import db

class Task(db.Model):
    """
    Easy model example
    """
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    done = db.Column(db.Boolean)

    def __init__(self, content, done):
        self.content = content
        self.done = done

    def __repr__(self):
        return f'<content {self.content}>'
