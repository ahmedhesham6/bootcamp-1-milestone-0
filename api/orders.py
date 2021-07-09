from . import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Order, Item
from schema import OrderBase, OrderUpdate

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def find(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    orders = db.query(Order).offset(skip).limit(limit).all()
    return {"message": "Orders Fetched Successfully", "data": orders}


@router.get("/{order_id}")
def find(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order Fetched Successfully", "data": order}


@router.post("/")
def create(order: OrderBase, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == order.item_id).one_or_none()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    check_avaliable_items(item, order.requested_quantity, db)
    db_order = Order(item_id=order.item_id,
                     shopping_cart_id=order.shopping_cart_id,
                     total_cost=calculate_total(
                         item, order.requested_quantity, db),
                     requested_quantity=order.requested_quantity)

    item = update_item_quantity(item, order.requested_quantity, db)
    db.add(item)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return {"message": "Order Created Successfully", "data": db_order}


@router.patch("/{id}")
def edit(id: int, order: OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).one_or_none()
    item = db.query(Item).filter(Item.id == db_order.item_id).one_or_none()
    check_avaliable_items(item, order.requested_quantity, db)

    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    for var, value in vars(order).items():
        setattr(db_order, var, value) if value else None
        if var == 'requested_quantity':
            item = update_item_quantity(
                item, order.requested_quantity - db_order.requested_quantity, db)

    setattr(db_order, 'total_cost', calculate_total(
        item, order.requested_quantity, db))

    db.add(item)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return {"message": "Order Updated Successfully", "data": db_order}


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == id).one_or_none()

    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    item = db.query(Item).filter(Item.id == order.item_id).one_or_none()
    item = update_item_quantity(item, -order.requested_quantity, db)

    db.add(item)
    db.delete(order)
    db.commit()
    return {"message": "Order Deleted Successfully"}


def check_avaliable_items(item: Item, requested_quantity: int, db: Session = Depends(get_db)):
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    if requested_quantity > item.available_quantity:
        raise HTTPException(status_code=404, detail="Items not sufficient")


def calculate_total(item: Item, requested_quantity: int, db: Session = Depends(get_db)):
    return requested_quantity * item.cost


def update_item_quantity(item: Item, requested_quantity: int, db: Session = Depends(get_db)):
    setattr(item, 'available_quantity',
            item.available_quantity - requested_quantity)
    return item
