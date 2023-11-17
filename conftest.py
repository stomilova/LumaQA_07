from os import environ
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=2880,1800')
    if environ.get('PYTHONDONTWRITEBYTECODE') == '1':
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    return options 


@pytest.fixture
def driver(options, request):
    driver = webdriver.Chrome(options=options)
    screenshots_directory = "screenshots" 
    failed_before = request.session.testsfailed
    yield driver
    if request.session.testsfailed != failed_before:
        test_name = request.node.name
        time_string = time.asctime().replace(":", "_")[3:-5]
        run_directory = os.path.join(screenshots_directory, f"run_{request.session.testscollected}")
        os.makedirs(run_directory, exist_ok=True)
        file_name = f"{time_string}_{test_name}.png"
        full_file_path = os.path.join(run_directory, file_name)
        driver.get_screenshot_as_file(full_file_path)
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait
