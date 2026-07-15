from playwright.sync_api import sync_playwright


def start_browser(browser_name: str = "chromium", headless: bool = False):
	pw = sync_playwright().start()
	browser = pw.chromium.launch(headless=headless)
	context = browser.new_context()
	page = context.new_page()
	return pw, browser, context, page


def stop_browser(pw, browser, context):
    context.close()
    browser.close()
    pw.stop()