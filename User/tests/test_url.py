from django.urls import resolve


def test_user_index_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/").view_name == "user-index"


def test_user_signup_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/signup").view_name == "user-signup"


def test_user_signin_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/signin").view_name == "user-signin"


def test_user_logout_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/logout").view_name == "user-logout"


def test_user_account_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/account").view_name == "user-account"

def test_user_changepassword_url():
    """Check if the name of the view is correct and that the URL matches the name of the view."""
    assert resolve("/user/changepassword").view_name == "user-change_password"