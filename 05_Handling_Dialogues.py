from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)

    page = browser.new_page()
    page.goto("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    alert_btn = page.get_by_text("Show Alert Box")
    #here we can observe that the playwright automatically clicks the "OK" button to close the alert Dialogue
    alert_btn.click()

    browser.close()