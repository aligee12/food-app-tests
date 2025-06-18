# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# def get_driver():
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--window-size=1920,1080')

#     service = Service(ChromeDriverManager().install())
#     return webdriver.Chrome(service=service, options=options)


import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')
    # Point to Chromium binary installed in container
    options.binary_location = "/usr/bin/chromium"

    # Auto-install the matching ChromeDriver for the installed Chromium
    chromedriver_autoinstaller.install()  # will download or use existing matching driver

    return webdriver.Chrome(options=options)
