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
        page.goto("https://moodle-trebesin.cz")
        page.click("span.login.pl-2")
        page.fill("input#username", login)
        page.fill("input#password", password)
        page.click("#loginbtn")
        
        page.click("text=PRG - 4G - 26/27")
        page.click("#module-25311 > div > div.activity-grid > div.activity-name-area.activity-instance.d-flex.flex-column.me-2 > div > div > a > span")
        page.click("#region-main > div:nth-child(4) > div.container-fluid.tertiary-navigation > div > div:nth-child(2) > a")
        page.fill("#id_subject", "Chci jedničku")
        page.frame_locator("#id_message_ifr").locator("body").click()
        page.keyboard.type("Děkuji")
        page.click("#id_submitbutton")
        
        konec = input("konec? ")
        print(konec)

if __name__ == "__main__":
    main()
    