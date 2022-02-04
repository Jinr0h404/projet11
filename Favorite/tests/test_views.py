import pytest
from django.urls import reverse
from django.test import Client
from User.models import CustomUser
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_purBeurre_view_cases():
    """Creates a test client. Make a request on the URL retrieved using the reverse () function.
    Check that the HTTP status code is 302 if user not connected and 200 if user is connected.
    Check that the template used is the expected one"""
    client = Client()
    path = reverse("favorite-index")
    response = client.get(path)
    if response.status_code == 302:
        username = "test_user"
        email = "troubadour@gmail.com"
        password = "Troubadour"
        CustomUser.objects.create_user(username=username, email=email, password=password)
        client.login(username=email, password=password)
        new_response = client.get(path)
        assert new_response.status_code == 200
        assertTemplateUsed(new_response, "Favorite/index_favoris.html")
