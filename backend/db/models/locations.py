from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
import json
from backend.db.database import Base


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True, index=True)
    world_id = Column(Integer, ForeignKey('worlds.id'), nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(Text)
    type = Column(String)
    tags = Column(String)
    images_json = Column(Text, default='[]')
    parent_location_id = Column(Integer, ForeignKey('locations.id'), nullable=True)

    world = relationship("World", backref="locations")
    parent_location = relationship("Location", remote_side=[id], backref="sublocations")

    @property
    def images(self):
        return json.loads(self.images_json)

    @images.setter
    def images(self, value):
        self.images_json = json.dumps(value)

    def __repr__(self):
        return f"<Location(name={self.name}, world_id={self.world_id})>"
