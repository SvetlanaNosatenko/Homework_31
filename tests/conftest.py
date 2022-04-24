from pytest_factoryboy import register

from factories import AdsFactory, UserFactory, CategoryFactory

pytest_plugins = "fixture"


register(AdsFactory)
register(UserFactory)
register(CategoryFactory)