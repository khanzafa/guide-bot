import base64
from app import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    file = db.Column(db.LargeBinary)
    created_at = db.Column(db.DateTime, index=True, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, index=True, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'file': base64.b64encode(self.file).decode('utf-8'),
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __repr__(self):
        return f'<Document {self.title}>'