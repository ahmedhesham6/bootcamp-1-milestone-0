from sqlalchemy import Column, Numeric, Integer, String
from sqlalchemy.orm import relationship

from db.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    cost = Column(Numeric(10, 2))
    available_quantity = Column(Integer)
