import pytest


@pytest.mark.django_db
def test_create_selection(client, hr_token, user, ads):
    expected_response = {
        "id": 1,
        "name": "name",
        "owner": user.id,
        "ad": [ads.id]
    }
    data = {
        "name": "name",
        "owner": user.id,
        "ad": [ads.id]
    }

    response = client.post("/selection/create/",
                           data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION=f"Bearer {hr_token}"
                           )
    assert response.status_code == 201
    assert response.data == expected_response

