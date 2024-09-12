from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Авторизация
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Выбор товара
    page.click('text=Sauce Labs Backpack')
    page.click('.btn_inventory')

    # Оформление покупки
    page.click('.shopping_cart_link')
    page.click('#checkout')
    page.fill('#first-name', 'John')
    page.fill('#last-name', 'Doe')
    page.fill('#postal-code', '12345')
    page.click('#continue')
    page.click('#finish')

    # Проверка завершения покупки
    success_message = page.locator('.complete-header').inner_text()
    assert "THANK YOU FOR YOUR ORDER" in success_message

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
