import pytest
from Favorite.models import Favorites
from Product.models import Product, Store, Category
from User.models import CustomUser
from Product.tests.test_models import product_fixture


@pytest.mark.django_db
def test_favorite_model(product_fixture):
    """test that the favorite model records the user, product and substitute information in the database"""
    product = Product.objects.get(pk=2)
    substitute = Product.objects.get(pk=1)
    username = "test_user"
    email = "troubadour@gmail.com"
    password = "Troubadour"
    user = CustomUser.objects.create_user(
        username=username, email=email, password=password
    )
    favorite = Favorites.objects.create(
        substitute_id=product, product_id=substitute, user_id=user
    )
    expected_value = "lightella | nutella | test_user | troubadour@gmail.com"
    assert str(favorite) == expected_value
