from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MarkdownFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    filename = db.Column(db.String(100), nullable=False)
