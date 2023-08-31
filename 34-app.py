from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Create a new page within the context
    page = context.new_page()

    # Visit google accounts
    page.goto("https://accounts.google.com")

    # Enter email address
    email_input = page.locator('input[type="email"]')  # Locate the email input field by its type attribute
    email_input.fill('02917711921_ds@vips.edu')

    next_button = page.get_by_role("button", name="Next").click()  # Click the "Next" button

    # Enter password
    password_input = page.locator('input[type="password"]')  # Locate the password input field by its type attribute
    password_input.fill('Mehul@123')

    next_button = page.get_by_role("button", name="Next").click()  # Click the "Next" button

    # Pause if your account has two-factor authentication
    # then complete the same before resuming
    page.pause()

    # Save authentication state
    context.storage_state(
        path="playwright/.auth/storage_state.json",
        # make sure 👆 you've created the playwright/.auth directory
    )

    browser.close()
