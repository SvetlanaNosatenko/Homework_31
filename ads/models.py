from datetime import date

from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

AGE_USER = 9
EMAIL_DOMAIN = "rambler.ru"


def check_email(value: str):
    if EMAIL_DOMAIN in value:
        raise ValidationError(
            "Prohibiting registration from a mail address in the domain %(value)",
            params={"value": value},
        )


def check_birth_date(value: date):
    delta_date = relativedelta(date.today(), value).years
    if delta_date < AGE_USER:
        raise ValidationError(
            '%(value)s is small, there is no possibility to register',
            params={'value': value},
        )


class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=10, validators=[MinLengthValidator(5)], unique=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"

    ROLES = [
        ("member", "Пользователь"),
        ("moderator", "Модератор"),
        ("admin", "Админ"),
    ]

    role = models.CharField(max_length=9, choices=ROLES, default="member")
    age = models.IntegerField(blank=True, null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date], blank=True, null=True)
    email = models.EmailField(unique=True, validators=[check_email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def save(self, *args, **kwargs):
        self.set_password(self.password)

        super().save()

    def __str__(self):
        return self.username


class Ads(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(10)], blank=False, null=True)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    description = models.CharField(max_length=1000, blank=True, null=True)
    is_published = models.BooleanField(default=False, null=True)
    image = models.ImageField(upload_to="ad/", null=True, blank=True)
    category_id = models.ForeignKey(Categories, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name


class Selection(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=False)
    ad = models.ManyToManyField(Ads)

    def __str__(self):
        return self.name
