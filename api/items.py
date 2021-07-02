from sqlalchemy.sql.expression import true
from . import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Item
from schema import ItemBase, ItemUpdate

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def find(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    items = db.query(Item).offset(skip).limit(limit).all()
    return {"message": "Items Fetched Successfully", "data": items}


@router.post("/")
def create(item: ItemBase, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, cost=item.cost,
                   available_quantity=item.available_quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item Created Successfully", "data": db_item}


@router.patch("/{id}")
def edit(id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == id).one_or_none()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for var, value in vars(item).items():
        setattr(db_item, var, value) if value else None

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item Updated Successfully", "data": db_item}


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == id).one_or_none()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()
    return {"message": "Item Deleted Successfully"}
