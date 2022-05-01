import pytest


@pytest.mark.django_db
def test_create_ads(client, user, categories, hr_token):

    expected_response = {
        "id": 1,
        "name": "name_number_1",
        "author_id": user.id,
        "price": 20,
        "description": "description",
        "is_published": False,
        "image": None,
        "category_id": categories.id,
    }
    data = {
        "name": "name_number_1",
        "author_id": user.id,
        "is_published": False,
        "price": 20,
        "description": "description",
        "category_id": categories.id,
    }

    response = client.post("/ad/create/",
                           data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION="Bearer " + hr_token
                           )
    assert response.status_code == 201
    assert response.data == expected_response
