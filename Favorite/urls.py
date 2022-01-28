from django.urls import path
from .views import index, delete_substitute
"""the url file is used to associate an url path to a view with path"""

urlpatterns = [
    path("", index, name="favorite-index"),
    path("delete_substitute", delete_substitute, name="favorite-delete_substitute"),
]
