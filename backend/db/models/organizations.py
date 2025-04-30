from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from backend.db.database import Base


class Organization(Base):
    __tablename__ = 'organizations'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Boolean, default=True)
    tags = Column(String, nullable=True)
    logo_image_path = Column(String, nullable=True)

    world = relationship("World", backref="organizations")
