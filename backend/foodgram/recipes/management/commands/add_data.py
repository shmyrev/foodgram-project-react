from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from recipes.management.commands.data import (
    ingredients_data,
    users_data,
    tags_data,
    recipes_data
)
from recipes.models import Ingredient, Recipe, Tag

User = get_user_model()


class Command(BaseCommand):
    help = 'Наполнить БД тестовыми данными'

    def handle(self, *args, **options):
        for ingredient in ingredients_data:
            Ingredient.objects.get_or_create(
                name=ingredient.get("name"),
                measurement_unit=ingredient.get("measurement_unit")
            )
        for user_data in users_data:
            User.objects.get_or_create(
                email=user_data[0],
                username=user_data[1],
                first_name=user_data[2],
                last_name=user_data[3],
                password=make_password(user_data[4])
            )
        for tag_data in tags_data:
            Tag.objects.get_or_create(
                name=tag_data.get("name"),
                color=tag_data.get("color"),
                slug=tag_data.get("slug")
            )
        for recipe_data in recipes_data:
            Recipe.objects.get_or_create(
                name=recipe_data.get("name"),
                text=recipe_data.get("text"),
                # image=recipe_data.get("image"),
                # tags=recipe_data.get("tags"),
                cooking_time=recipe_data.get("cooking_time"),
                # author=recipe_data.get("author")
            )
