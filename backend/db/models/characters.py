from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.database import Base


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'), nullable=False)
    name = Column(String, nullable=False)
    photo_path = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    type = Column(Text, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    race = Column(String, nullable=True)
    character_class = Column(String, nullable=True)
    status = Column(Boolean, default=True)

    world = relationship("World", backref="characters")
