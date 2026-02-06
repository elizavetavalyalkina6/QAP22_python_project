from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"
SUBSCRIPTION = f"{BASE_URL}/automation-lab/subscription"


def test_open_subscription():
    opts = Options()

    opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    driver = webdriver.Chrome(options=opts)

    driver.get(SUBSCRIPTION)

    assert driver.title == "Task Management Board"
    assert driver.current_url == SUBSCRIPTION

    element_summary_title = driver.find_element(By.CSS_SELECTOR, ".summary-title")
    assert element_summary_title.is_displayed()
