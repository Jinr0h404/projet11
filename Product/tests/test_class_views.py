import pytest
from django.urls import reverse
from django.test import TestCase, Client
from User.models import CustomUser
from Favorite.models import Favorites
from pytest_django.asserts import assertTemplateUsed
from Product.tests.test_models import product_fixture


@pytest.mark.django_db(reset_sequences=True)
class ProductViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.client = Client()

    def test_search_view(self, product_fixture):
        """Creates a test client. Make a request on the URL retrieved using the reverse () function.
        Check that the HTTP status code is 200. Check that the template used is the expected one"""
        path = reverse("product-search")
        response = self.client.get(path, {"query": "pizza saison"})
        send_query = "pizza saison"
        keep_query = response.context["query"]
        assert send_query == keep_query
        assert response.status_code == 200
        assert all([a == b for a, b in zip(
            keep_query, send_query)])
        assertTemplateUsed(response, "Product/search.html")

    def test_search_substitute_view(self, product_fixture):
        """Creates a test client. Make a request on the URL retrieved using the reverse () function.
            Check that the HTTP status code is 200. Check that the template used is the expected one"""
        path = reverse("product-search_substitute")
        response = self.client.get(path, {"query": "1"})
        assert response.status_code == 200
        assertTemplateUsed(response, "Product/search_substitute.html")

    def test_product_view(self, product_fixture):
        """Creates a test client. Make a request on the URL retrieved using the reverse () function.
            Check that the HTTP status code is 200. Check that the template used is the expected one"""
        path = reverse("product-product_info", args=["1"])
        response = self.client.get(path)
        assert response.status_code == 200
        assertTemplateUsed(response, "Product/product_info.html")

    def test_save_substitute_view(self, product_fixture):
        """Creates a test client. Make a post request on the URL retrieved using the reverse () function.
            Check that the new favorite is register. Check that the HTTP status code is 302 due to the redirect."""
        username = "test_user"
        email = "troubadour@gmail.com"
        password = "Troubadour"
        CustomUser.objects.create_user(username=username, email=email, password=password)
        self.client.login(username=email, password=password)
        old_favorite = Favorites.objects.count()
        path = reverse("product-save_substitute")
        response = self.client.post(path, {"save": "1,1"})
        new_favorite = Favorites.objects.count()
        assert new_favorite == old_favorite + 1
        assert response.status_code == 302
