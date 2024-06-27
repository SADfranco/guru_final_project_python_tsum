from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class FavoriteItem:
    def search_item(self, favorite_item):
        with step(f'Search item {favorite_item.kind}'):
            browser.element((AppiumBy.ID, 'ru.tsum.app:id/search_query_edit')).click()
            browser.element((AppiumBy.ID, 'ru.tsum.app:id/search_query_edit')).type(f'{favorite_item.kind}')
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="the tote bag"]')).click()

    def add_to_favorite_list(self):
        with step(f'Add item to favorite list'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/favorite_image")).click()

    def go_to_favorite_tab(self):
        with step(f'Add item to favorite list'):
            browser.driver.back()
            browser.element((AppiumBy.ID, "ru.tsum.app:id/favorites_tab_graph")).click()
            browser.element((AppiumBy.ID, "ru.tsum.app:id/close_button")).click()

    def check_added_items_in_list(self, favorite_item):
        with step(f'Check added item {favorite_item.name}'):
            browser.element((AppiumBy.ID, "ru.tsum.app:id/title_text")).should(have.exact_text('Избранное'))
            browser.element((AppiumBy.ID, "ru.tsum.app:id/subtitle_text")).should(have.exact_text('1 товар'))
            browser.element((AppiumBy.ID, "ru.tsum.app:id/txt_name")).should(have.text(f'{favorite_item.name}'))


favorite_item = FavoriteItem()
