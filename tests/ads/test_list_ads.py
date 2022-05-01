import pytest
from factories import AdsFactory


@pytest.mark.django_db
def test_list_ads(client):
    ads = AdsFactory.create_batch(10)

    response = client.get("/ad/")

    ads_list = []
    for ad in ads:
        ads_list.append(
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id_id,
                "author": ad.author_id.first_name,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image,
                "category_id": ad.category_id_id,
                "price": ad.price
            }
        )

    expected_response = {
        "items": ads_list,
        "num_pages": 1,
        "total": 10
    }

    assert response.status_code == 200
    assert response.json() == expected_response
