import pytest

from ads.serializers import AdsSerializer
from factories import AdsFactory


@pytest.mark.django_db
def test_list_ads(client):
    ads = AdsFactory.create_batch(10)

    response = client.get("/ads/")
    ads_list = []
    for ad in ads:
        ads.append(
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.first_name,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "image": ad.image.url,
                "category_id": ad.category_id
            }
        )

    expected_response = {
        "items": ads_list,
        "num_page": 1,
        "total": 10
    }

    assert response.status_code == 200
    assert response.json() == expected_response
