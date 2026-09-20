from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    

    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    assert page.to_be_visible("text=Dashboard")
    browser.close()