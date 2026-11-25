from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")

def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.moodle-trebesin.cz")
        
        page.click("span.login.pl-2")
        page.fill("input#username", login)
        page.fill("input#password", password)
        page.click("#loginbtn")
        page.click("#course-info-container-277-3 > div > div > a > span.multiline")
        page.click("#module-25311 > div > div.activity-grid > div.activity-name-area.activity-instance.d-flex.flex-column.me-2 > div > div > a")
        page.click("#region-main > div:nth-child(4) > div.container-fluid.tertiary-navigation > div > div:nth-child(2) > a")
        page.fill("#id_subject", "chci jednicku")
        page.fill("#id_message", "prosim jednicku :)")
        page.click("#fgroup_id_buttonar > div.col-md-9.d-flex.flex-wrap.align-items-start.felement > div.w-100.m-0.p-0.border-0 > div > div:nth-child(1) > span")

        input("Zmackni cokoli pro zavreni")
        browser.close()

if __name__ == "__main__":
    main()


