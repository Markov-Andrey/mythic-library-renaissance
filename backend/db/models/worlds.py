from sqlalchemy import Column, Integer, String
from backend.db.database import Base


class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    visual_style = Column(String)
    tags = Column(String)
    cover = Column(String)
