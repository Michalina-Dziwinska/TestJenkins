from selenium import webdriver


def test_open_kiwi():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)  # Implicit wait of 10 seconds

    try:

        driver.get("https://www.kiwi.com")

        print("Page title is:", driver.title)

        assert "Kiwi" in driver.title, "Title does not contain 'Kiwi'"

    finally:
        # Close the browser
        driver.quit()


# Run the test
test_open_kiwi()
