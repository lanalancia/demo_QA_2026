


# pages/secure_page.py
class SecurePage:
	URL = "https://the-internet.herokuapp.com/basic_auth"

	def __init__(self, page):
		self.page = page

	def open(self):
		self.page.goto(self.URL)

	def success_message(self):
		return self.page.get_by_text("Congratulations!")