from datetime import datetime, timezone;  # type: ignore
from sqlalchemy.orm import Mapped, mapped_column, relationship; # type: ignore
from flaskblog import db;

class User(db.Model):
    id: Mapped['int'] = mapped_column(primary_key=True)
    
    username: Mapped['str'] = mapped_column(db.String(20), nullable=False, unique=True)
    
    email: Mapped['str'] = mapped_column(db.String(120), nullable=False, unique=True)
    
    password: Mapped['str'] = mapped_column(db.String(20), nullable=False)
    
    image_file_path: Mapped['str'] = mapped_column(db.Text, nullable=False, default='default.jpg')

    posts: Mapped[list['Post']] = relationship(backref='author', lazy=True)

    def __repr__(self):
        return f'{self.username}, {self.id}, {self.image_file_path}'

class Post(db.Model):
    id: Mapped['int'] = mapped_column(primary_key=True)

    post_title: Mapped['str'] = mapped_column(db.Text, nullable=False, default='Default Blog Post Title')

    post_content: Mapped['str'] = mapped_column(db.Text, nullable=False, default='Default Blog Post Content')

    date_posted: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    user_id: Mapped['int'] = mapped_column(db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'{self.post_title}, {self.date_posted}, {self.id}'
