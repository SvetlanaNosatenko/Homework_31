import factory

from ads.models import Ads, User, Categories


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = "password"
    email = factory.Faker("email")


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categories

    slug = factory.Faker("color")


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ads

    name = "name_number_1"
    author_id = factory.SubFactory(UserFactory)
    category_id = factory.SubFactory(CategoryFactory)
    price = 20


