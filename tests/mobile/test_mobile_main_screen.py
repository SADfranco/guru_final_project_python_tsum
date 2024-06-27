import allure
from allure_commons.types import Severity
from tsum_tests.pages.mobile.main_screen_page import main_screen
from tsum_tests.data.menu import MobileTabName


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Check New In tab')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Main screen tabs")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_new_in_tab():
    test_tab_name = MobileTabName(
        tab_name='new_in',
        title_name='Новые поступления'
    )

    main_screen.skip_first_notifications()

    main_screen.open_tab(test_tab_name)

    main_screen.check_bar_menu_title(test_tab_name)


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Check Brands tab')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Main screen tabs")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_brands_tab():
    test_tab_name = MobileTabName(
        tab_name='brands',
        title_name='A'
    )

    main_screen.skip_first_notifications()

    main_screen.open_tab(test_tab_name)

    main_screen.check_bar_menu_title(test_tab_name)


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Check Catalog tab')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Main screen tabs")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_catalog_tab():
    test_tab_name = MobileTabName(
        tab_name='catalog',
        title_name='Каталог'
    )

    main_screen.skip_first_notifications()

    main_screen.open_tab(test_tab_name)

    main_screen.check_bar_menu_title(test_tab_name)


@allure.tag('Mobile')
@allure.tag('Android')
@allure.tag('regress')
@allure.title('Check Favorites tab')
@allure.severity(Severity.NORMAL)
@allure.label("owner", "SADfranco")
@allure.feature("Main screen tabs")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_favorites_tab():
    test_tab_name = MobileTabName(
        tab_name='favorites_tab',
        title_name='Избранное'
    )

    main_screen.skip_first_notifications()

    main_screen.open_tab(test_tab_name)

    main_screen.check_bar_menu_title(test_tab_name)
