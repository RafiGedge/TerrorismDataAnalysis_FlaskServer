from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.models.base import Base


class Gname(Base):
    __tablename__ = 'gnames'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    events = relationship("Event", back_populates="gnames")