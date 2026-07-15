

"""
Page object for Inputs page of The Internet website:
https://the-internet.herokuapp.com/inputs
"""

class InputsPage:
	URL = "https://the-internet.herokuapp.com/inputs"

	def __init__(self, page):
		self.page = page
		self.number_input = (
			page.get_by_text("Number", exact=True)
			.locator("xpath=..")
			.locator("input[type='number']")
		)

	def open(self):
		self.page.goto(self.URL)

	def type_number(self, value: str):
		self.number_input.fill(value)

	def get_value(self) -> str:
		return self.number_input.input_value()