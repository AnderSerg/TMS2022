from selenium.webdriver.common.by import By


class MainPageLoc:

    login_loc = (By.CSS_SELECTOR, ".header_user_info")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')
    dresses_loc = (By.XPATH, '//a[@href="http://automationpractice.com/index.php?id_category=8&controller=category"]')
    contact_us_loc = (By.XPATH, '//*[@id="center_column"]/h1')
