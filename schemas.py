""" API Schemas/serializers"""
from app import ma

class VideoSchema(ma.Schema):
    class Meta:
        fields = ('url', 'duration', 'quality','browser_data')

task_schema = VideoSchema()
tasks_schema = VideoSchema(many=True)
