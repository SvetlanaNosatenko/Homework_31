import pytest
from ads.models import User


@pytest.fixture()
@pytest.mark.django_db
def hr_token(client):
    username = "username"
    password = "password"

    User.objects.create(username=username, password=password,
                        role="admin")

    response = client.post(
        "/user/token/",
        {"username": username, "password": password}, format="json"
    )
    return response.data["access"]
