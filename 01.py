from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:


    #Launch a Browser
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    #Create a new page
    page = browser.new_page()
    #Visit the Playwright Website
    page.goto("https://playwright.dev/python")

    #Locator
    docs_button = page.get_by_role('link',name='Get Started')
    docs_button.click()

    print(page.url)
    browser.close()

    