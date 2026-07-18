from pages.basic_auth import SecurePage

"""
testing the https://the-internet.herokuapp.com/basic_auth
"""


def test_successful_login(secure_page: SecurePage):
	secure_page.open()
	assert secure_page.success_message().is_visible()