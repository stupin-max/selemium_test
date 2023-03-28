from search import Search, Images
# import pytest_check as check
import time

def test_tensor_search(browser):
    yandex_main_page = Search(browser)
    yandex_main_page.go_to_site()
    search_field_test = yandex_main_page.search_field()
    assert search_field_test is not None, "Search field is not found"
    yandex_main_page.enter_word("Тензор")
    suggest_field = yandex_main_page.suggest_field()
    assert suggest_field is not None, "Suggests are not found"
    yandex_main_page.press_enter()
    result_page = yandex_main_page.result_block()
    assert result_page is not None, "Results are not found"
    first_result = yandex_main_page.first_result()
    assert first_result != 'http://tensor.ru/', "First link not equal to http://tensor.ru/"

def test_yandex_pictures(browser):
    yandex_main_page = Search(browser)
    yandex_main_page.go_to_site()
    menu = yandex_main_page.menu_find()
    #_____________NEED_TO_CHECK
    assert menu is not None, 'Menu not found' # need to add soft asser from check
    yandex_main_page.click_to_search_field() #menu is availible after click to search only
    assert menu is not None
    #_____________NEED_TO_CHECK
    yandex_main_page.click_to_menu_field()

    yandex_main_page.go_to_pictures()
    yandex_main_page.switch_to_pictures_tab()

    yandex_image_page = Images(browser)
    impages_page_url = str(yandex_image_page.get_current_url())
    assert impages_page_url == 'https://yandex.ru/images/'

    first_block_name = yandex_image_page.first_result()
    yandex_image_page.go_to_first_images_block()
    search_field_value = yandex_image_page.get_value_from_search()
    assert first_block_name == search_field_value, "Value in search block not equal to value from category"

    yandex_image_page.go_to_first_picture()
    first_image_src = yandex_image_page.get_src_of_pictures()
    assert first_image_src is not None, "Image was not opened"

    yandex_image_page.go_to_next_picture()
    second_image_src = yandex_image_page.get_src_of_pictures()
    assert first_image_src != second_image_src, "Image is not changed - Second image is equal to first image"

    yandex_image_page.go_to_prev_picture()
    first_image_src_2 = yandex_image_page.get_src_of_pictures()
    assert first_image_src == first_image_src_2, "Previous image not equal to first image"
