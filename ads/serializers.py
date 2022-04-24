from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from ads.models import Ads, Selection, Categories, check_birth_date


class NotIsPublished:
    def __call__(self, value):
        if value:
            raise serializers.ValidationError("New ad can not be published")


class AdsSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[NotIsPublished()])

    class Meta:
        model = Ads
        fields = '__all__'


class SelectionDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id"]


class SelectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionDetailSerializer(serializers.ModelSerializer):
    ad = AdsSerializer(many=True, read_only=True)

    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Selection
        fields = ["name", "owner", "ad"]


class SelectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["name", "owner", "ad"]


class CategoriesListSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(
        validators=[UniqueValidator(queryset=Categories.objects.all())]
    )

    class Meta:
        model = Categories
        fields = '__all__'
