from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")

def main():

    with sync_playwright() as p :

        browser = p.chromium.launch(headless=False)

        page =  browser.new_page()

        # page.goto("https://www.trebesin.cz/")

        # page.click("#fav-nav > div > div > div.moduletable > div > div > a:nth-child(2) > img")

        page.goto("https://www.moodle-trebesin.cz")

        page.click("span.login.pl-2")
        page.fill("input#username", login)
        page.fill("input#password", password)
        page.click("#loginbtn")
        page.click("#course-info-container-277-3 > div > div > a > span.multiline")
        page.click("#module-25311 > div > div.activity-grid > div.activity-name-area.activity-instance.d-flex.flex-column.me-2 > div > div > a")
        page.click("#region-main > div:nth-child(4) > div.container-fluid.tertiary-navigation > div > div:nth-child(2) > a")
        page.fill("#id_subject", "Jednička")
        page.fill("#id_message", "Chci jedničku :D")
        page.click("#id_submitbutton")


        input("Zmackni cokoliv pro zavreni")
        browser.close()


        

        browser = p.chromium.launch(headless=False)
        

if __name__ == "__main__":
    main()