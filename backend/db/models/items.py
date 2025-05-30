from sqlalchemy import Column, Integer, String, Boolean, Text, Float, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.database import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'), nullable=False)
    name = Column(String, nullable=False)
    tags = Column(String, nullable=True)
    cover = Column(String)
    description = Column(Text, nullable=True)
    value = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    type = Column(String, nullable=False)

    world = relationship("World", backref="items")
