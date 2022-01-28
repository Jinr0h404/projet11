import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.webdriver.common.by import By
from User.models import CustomUser

class TestChangePassword(StaticLiveServerTestCase):
    """class containing methods to check the authentication part of the application"""
    @pytest.mark.django_db
    def test_changepassword(self):
        """functional test with selenium to verify the user change password scenario."""
        username = "toto"
        email = "toto@gmail.com"
        password = "ewen12345"
        CustomUser.objects.create_user(username=username, email=email, password=password)
        self.s = Service("User/tests/functional_tests/chromedriver")
        self.browser = webdriver.Chrome(service=self.s)
        self.browser.get(self.live_server_url + reverse("user-change_password"))
        email = self.browser.find_element(By.ID, "id_email")
        email.send_keys("toto@gmail.com")
        password = self.browser.find_element(By.ID, "id_password")
        password.send_keys("ewen12345")
        signin = self.browser.find_element(By.NAME, "signin")
        signin.submit()
        old_password = self.browser.find_element(By.ID, "id_old_password")
        old_password.send_keys("ewen12345")
        new_password1 = self.browser.find_element(By.ID, "id_new_password1")
        new_password1.send_keys("toto12345")
        new_password2 = self.browser.find_element(By.ID, "id_new_password2")
        new_password2.send_keys("toto12345")
        change = self.browser.find_element(By.NAME, "password_change")
        change.submit()
        self.assertEqual(
            self.browser.current_url, self.live_server_url + reverse("user-account")
        )
        self.assertEqual(self.browser.find_element(By.TAG_NAME, "h2").text, "toto")
        self.browser.close()
