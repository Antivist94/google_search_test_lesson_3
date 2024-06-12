from selene import browser, be, have
import pytest

@pytest.fixture(scope="function",autouse=True)
def browser_manager():
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    browser.config.base_url = 'https://google.com'
    yield
    print("Тест закончен")
    browser.quit()


def test_google_search():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_search_no_results():
    browser.open('')
    browser.element('[name="q"]').should(be.blank).type('12345678o86543qwedasfdvbdfhartsuw7463yerh').press_enter()
    browser.element('.card-section').should(have.text('По запросу 12345678o86543qwedasfdvbdfhartsuw7463yerh ничего не найдено. '))

