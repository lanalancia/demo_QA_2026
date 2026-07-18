import pytest
from playwright.sync_api import Browser
from pages.basic_auth import SecurePage


"""
Pytest fixtures
"""

## A fixture for HTTP Auth
@pytest.fixture
def secure_page(browser: Browser):
	context = browser.new_context(
		http_credentials={"username": "admin", "password": "admin"},
	)
	page = context.new_page()
	yield SecurePage(page)
	context.close()