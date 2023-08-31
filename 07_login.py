from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=300)

    page = browser.new_page()
    page.goto("https://accounts.google.com/v3/signin/identifier?flowEntry=ServiceLogin&flowName=GlifWebSignIn&ifkv=AXo7B7Wv3ANWYDjg2EfFlwc5NIlvhoz-oqAfCIV4wS7N6KlRWkcZSKQ1ZrzFsDDUUh3uMUH5oRATBA&dsh=S-1643692563%3A1693063845784729")
    email = page.locator("//input[@id='identifierId']")
    email.fill("02917711921_ds@vips.edu")

    # next_button = page.get_by_role("button", name="Next").click()
    next_button = page.locator("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b VfPpkd-ksKsZd-mWPk3d VfPpkd-ksKsZd-mWPk3d-OWXEXe-Tv8l5d-lJfZMc']//div[@class='VfPpkd-RLmnJb']")
    password = page.get_by_label("Enter your password")
    password.type("Mehul@123")
    next_button = page.get_by_role("button", name="Next").click()

    
    browser.close()
    