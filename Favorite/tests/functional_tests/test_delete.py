import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from User.models import CustomUser
from Favorite.models import Favorites
from Product.models import Product, Store, Category
import time


class TestDelete(StaticLiveServerTestCase):
    @pytest.mark.django_db()
    def test_delete_saved_favorite(self):
        """tests the user's navigation when doing a delete favorite using the delete tool on the index
        favorite page"""
        username = "toto"
        email = "toto@gmail.com"
        password = "ewen12345"
        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        product_list = [
            {
                "name": "nutella",
                "store": "leclerc",
                "category": ["pate", "pate à tartiner", "petit déjeuner", "chocolat"],
                "nutriscore": "D",
                "description": "petit déjeuner",
                "fat": "0,145",
                "saturated_fat": "0,145",
                "salt": "0,145",
                "sugar": "0,145",
            },
            {
                "name": "lightella",
                "store": "leclerc",
                "category": ["pate"],
                "nutriscore": "B",
                "description": "petit déjeuner",
                "fat": "0,14",
                "saturated_fat": "0,04",
                "salt": "0,02",
                "sugar": "0,14",
            },
            {
                "name": "nutalla",
                "store": "leclerc",
                "category": ["pate à tartiner", "petit déjeuner", "chocolat"],
                "nutriscore": "B",
                "description": "petit déjeuner",
                "fat": "0,14",
                "saturated_fat": "0,04",
                "salt": "0,02",
                "sugar": "0,14",
            },
        ]
        for i in product_list:
            new_product = Product.objects.create(
                product_name=i["name"],
                nutriscore=i["nutriscore"],
                fat=str(i["fat"]),
                saturated_fat=str(i["saturated_fat"]),
                salt=str(i["salt"]),
                sugar=str(i["sugar"]),
            )
            last_product = Product.objects.last()
            prod_id = last_product.pk
            for category in i["category"]:
                """the value of the category key in the dictionary can contain
                several elements. I therefore loop on the category to fill my
                table with get_or_create function of peewee to haven't a
                duplicate"""
                category = category.strip()
                """ strip() remove spaces before and after item"""
                new_category, created = Category.objects.get_or_create(
                    category_name=category
                )
                cat_id = new_category.pk
                last_product.category.add(cat_id)
            for store in i["store"]:
                """like category, the value of the store key in the dictionary
                can contain several elements. loop to fill my table with the
                get_or_create function"""
                store = store.strip()
                new_store, created = Store.objects.get_or_create(store_name=store)
                store_id = new_store.pk
                last_product.store.add(store_id)
        prodTest = Product.objects.all()
        product_test = Product.objects.get(product_name='lightella')
        substitute = Product.objects.get(product_name='nutella')
        favorite = Favorites.objects.create(
            substitute_id=product_test, product_id=substitute, user_id=user
        )
        self.s = Service("Product/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("favorite-index"))
        email = self.browser.find_element(By.ID, "id_email")
        email.send_keys("toto@gmail.com")
        password = self.browser.find_element(By.ID, "id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element(By.NAME, "signin")
        signin.submit()
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        delete_submit = self.browser.find_element(By.NAME, "delete")
        delete_submit.click()
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "p").text, "Vous n'avez pas encore enregistré votre substitut préféré.")
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("favorite-index")
        )
        self.browser.close()
