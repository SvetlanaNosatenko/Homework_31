import pytest

from ads.serializers import AdsSerializer


@pytest.mark.django_db
def test_ads_detail(client, ads, hr_token):
    response = client.get(f"/ads/{ads.id}/",
                          content_type="application/json",
                          HTTP_AUTHORIZATION="Bearer " + hr_token
                          )

    assert response.status_code == 200
    assert response.data == AdsSerializer(ads).data

