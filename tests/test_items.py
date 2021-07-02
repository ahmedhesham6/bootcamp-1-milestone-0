from . import client


def test_create_item():
    response = client.post(
        "/items/",
        json={
            "name": "Item1",
            "cost": 22.19,
            "available_quantity": 18
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item Created Successfully",
        "data": {"id": 1, "name": "Item1", "cost": 22.19, "available_quantity": 18}
    }

    response = client.post(
        "/items/",
        json={
            "name": "Item2",
            "cost": 130.12,
            "available_quantity": 5
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item Created Successfully",
        "data": {"id": 2, "name": "Item2", "cost": 130.12, "available_quantity": 5}
    }


def test_read_item():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Items Fetched Successfully",
        "data": [
            {
                "id": 1,
                "name": "Item1",
                "cost": 22.19,
                "available_quantity": 18
            },
            {
                "id": 2,
                "name": "Item2",
                "cost": 130.12,
                "available_quantity": 5
            }
        ]
    }


def test_update_item():
    response = client.patch(
        "/items/3",
        json={"name": "Item2 Tested"})
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }

    response = client.patch(
        "/items/1",
        json={"name": "Item1 Tested"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item Updated Successfully",
        "data": {
            "id": 1,
            "name": "Item1 Tested",
            "cost": 22.19,
            "available_quantity": 18
        }
    }


def test_delete_item():
    response = client.delete("/items/3")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Item not found"
    }

    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item Deleted Successfully"
    }
