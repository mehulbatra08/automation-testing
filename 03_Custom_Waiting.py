from playwright.sync_api import sync_playwright
from time import perf_counter

with sync_playwright() as playwright:


    #Launch a Browser
    browser = playwright.chromium.launch(headless=False,slow_mo=500)
    #Create a new page
    page = browser.new_page()

    page.goto("https://www.scrapethissite.com/pages/ajax-javascript/")

    link = page.get_by_role("link", name="2015").click()
    print("Page loading...")
    start = perf_counter()
    first_table_data = page.locator("td.film-title").first
    first_table_data.click()
    time_taken = perf_counter() - start
    print(f"Time taken by the table is {round(time_taken,2)}")

    browser.close()