from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    

    page.locator("//input[@name='username']").fill("Admin")
    page.locator("//input[@name='password']").fill("admin123")
    page.locator("//button[@type='submit']").click()
    assert page.locator("//h6[normalize-space()='Dashboard'][1]").text_content() == "Dashboard"
    
    browser.close()