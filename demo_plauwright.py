import re
from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
    expect(page).to_have_title("The Internet")

def test_login_fail(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_role("textbox", name="Username").fill("wronguser")
    page.get_by_role("textbox", name="Password").fill("wrongpass")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("#flash")).to_contain_text("Your username is invalid!")

    print("https://the-internet.herokuapp.com/secure", page.url)
    print("The Internet", page.title())

