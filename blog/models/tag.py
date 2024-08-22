from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import db

article_tag_association_table = Table(
    "article_tag_association",
    db.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tag.id'), nullable=False),
)


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, default="", server_default="")
    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')

    def __str__(self):
        return self.name
