from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class AddToCart:
    def search_item(self, favorite_item):
        with step(f'Search item {favorite_item.kind}'):
            browser.element((AppiumBy.ID, 'ru.tsum.app:id/search_query_edit')).click()
            browser.element((AppiumBy.ID, 'ru.tsum.app:id/search_query_edit')).type(f'{favorite_item.kind}')
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="the tote bag"]')).click()

    def open_items_page(self, favorite_item):
        with step(f'Open item page with name {favorite_item.name}'):
            browser.element((AppiumBy.XPATH, f'//android.widget.TextView[@text={favorite_item.name}]')).click()

    def add_to_cart(self):
        with step(f'Add item to cart'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/buy_button")).click()

    def go_to_cart(self):
        with step(f'Add item to cart'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/go_to_cart_button")).click()
            browser.element((AppiumBy.ID, "ru.tsum.app:id/close_button")).click()

    def check_added_items(self, favorite_item):
        with step(f'Check added item {favorite_item.name}'):
            browser.element((AppiumBy.ID, f"ru.tsum.app:id/description_text")).should(have.text('{favorite_item.name}'))


add_to_cart = AddToCart()
