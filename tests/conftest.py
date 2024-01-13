import pytest
from test_data.links import MainPageLinks


@pytest.fixture()
def main_page_open(driver):
    driver.get(MainPageLinks.URL_MAIN_PAGE)

@pytest.fixture()
def description_page_open(driver):
    driver.get(MainPageLinks.URL_DESCRIPTION_PAGE)