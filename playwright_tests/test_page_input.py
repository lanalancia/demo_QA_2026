import pytest
from playwright.sync_api import Page
from pages.input_page import InputsPage


"""
tests for "input" page

only testing the input. We den't test the spinbox increments and decrements because they are 
part of a browser engine, not a part of website
"""


# inputs the number, than looks at the field, the number should match
@pytest.mark.parametrize(
	"input_data", 
	[
		"42",
	]
)
def test_input_number_field_accepts_numbers(page: Page, input_data: str):
	inputs = InputsPage(page)
	inputs.open()
	inputs.type_number(input_data)
	assert inputs.get_value() == input_data, f"expected {input_data}, received > {inputs.get_value()} <"


# inputs the letter in a number field. A field should not accept wrong types
@pytest.mark.parametrize(
	"input_data", 
	[
		"a",
	]
)
def test_input_number_field_rejects_letters(page: Page, input_data: str):
	inputs = InputsPage(page)
	inputs.open()
	inputs.type_number(input_data)
	assert inputs.get_value() == "", f"expected empty string, received > {inputs.get_value()} <"

