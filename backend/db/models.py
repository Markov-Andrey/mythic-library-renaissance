# backend/db/models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class World(Base):
    __tablename__ = 'worlds'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)  # Имя мира (обязательное поле)
    description = Column(String)  # Краткое описание
    visual_style = Column(String)  # Визуальный стиль (для рисовалки)
    tags = Column(String)  # Теги (для поиска, можно хранить как строку)
    cover_image_path = Column(String)  # Обложка

    def __repr__(self):
        return f"<World(name={self.name}, short_description={self.short_description})>"
