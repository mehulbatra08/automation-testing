from playwright.sync_api import sync_playwright

def on_load(page):
    print("Page Loaded: ",page)
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)

    page = browser.new_page()
    page.on("load", on_load)
    page.goto("https://bootswatch.com/default")
    
    browser.close()