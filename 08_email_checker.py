from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=300)

    page = browser.new_page()
    page.goto("https://mail.google.com/mail/u/0/#inbox")
    email = page.get_by_label("Email or phone")
    email.fill("02917711921_ds@vips.edu")

    next_button = page.get_by_role("button", name="Next").click()
    password = page.get_by_label("Enter your password")
    password.type("Mehul@123")
    next_button = page.get_by_role("button", name="Next").click()
    page.wait_for_selector('div[role="listitem"]')
    
    browser.wait_for_context_closing()
    