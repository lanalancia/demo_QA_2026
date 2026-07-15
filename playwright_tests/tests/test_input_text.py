from playwright_tests.helpers.browsers import start_browser, stop_browser
from playwright_tests.pages.ti_input_page import InputsPage


def main():
	pw, browser, context, page = start_browser(headless=False)
	try:
		inputs = InputsPage(page)
		inputs.open()
		inputs.type_number("43")

		actual = inputs.get_value()
		assert actual == "42", f"expected 42, received {actual}"
		print("PASS: input text works")
	finally:
		page.wait_for_timeout(1000)
		stop_browser(pw, browser, context)


if __name__ == "__main__":
	main()