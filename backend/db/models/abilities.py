from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.database import Base

class Ability(Base):
    __tablename__ = 'abilities'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'), nullable=False)
    name = Column(String, nullable=False)
    tags = Column(String, nullable=True)
    cover = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    type = Column(String, nullable=True)

    world = relationship("World", backref="abilities")
