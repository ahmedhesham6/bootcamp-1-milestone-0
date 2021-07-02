from . import client


def test_create_order():
    response = client.post(
        "/orders/",
        json={
            "item_id": 3,
            "shopping_cart_id": 2,
            "requested_quantity": 20
        },
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }

    response = client.post(
        "/orders/",
        json={
            "item_id": 2,
            "shopping_cart_id": 2,
            "requested_quantity": 20
        },
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Items not sufficient"
    }

    response = client.post(
        "/orders/",
        json={
            "item_id": 2,
            "shopping_cart_id": 2,
            "requested_quantity": 1
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Order Created Successfully",
        "data": {
            "id": 1,
            "item_id": 2,
            "shopping_cart_id": 2,
            "requested_quantity": 1,
            "total_cost": 130.12,
        }
    }


def test_read_order():
    response = client.get("/orders")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Orders Fetched Successfully",
        "data": [
            {
                "id": 1,
                "item_id": 2,
                "shopping_cart_id": 2,
                "requested_quantity": 1,
                "total_cost": 130.12,
            }
        ]
    }


def test_update_order():
    response = client.patch(
        "/orders/1",
        json={
            "requested_quantity": 8
        }
    )
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Items not sufficient"
    }

    response = client.patch(
        "/orders/1",
        json={
            "requested_quantity": 2
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Order Updated Successfully",
        "data": {
            "id": 1,
            "item_id": 2,
            "shopping_cart_id": 2,
            "requested_quantity": 2,
            "total_cost": 130.12*2,
        }
    }


def test_delete_order():
    response = client.delete("/orders/3")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Order not found"
    }

    response = client.delete("/orders/1")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Order Deleted Successfully"
    }
