from sqlalchemy import Column, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey('items.id'))
    shopping_cart_id = Column(Integer)
    total_cost = Column(Numeric(10, 2))
    requested_quantity = Column(Integer)

    item = relationship("Item")
