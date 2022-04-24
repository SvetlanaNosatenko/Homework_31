import pytest


@pytest.mark.django_db
def test_create_ads(client, user, category):

    expected_response = {
        "id": 1,
        "name": "name",
        "author_id": user.id,
        "price": 20,
        "description": "description",
        "is_published": False,
        "image": None,
        "category_id": category.id,
    }
    data = {
        "name": "name",
        "author_id": user.id,
        "is_published": False,
        "price": 20,
        "description": "description",
        "category_id": category.id
    }

    response = client.post("/ads/create/",
                           data,
                           content_type="application/json"
                           )
    assert response.status_code == 201
    assert response.data == expected_response
