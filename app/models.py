
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey


class Demo(Model):
    id = Column(Integer,primary_key=True)
    name = Column(String(50),nullable=False)
    description=Column(String(250),nullable=True)

    def __repr__(self):
        return self.name