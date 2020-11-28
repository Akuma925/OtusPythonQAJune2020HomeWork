import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://10.10.42.110/", help="choose endpoint")
    parser.addoption("--run", "-R", action="store", default="remote", help="choose endpoint")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def run(request):
    return request.config.getoption("--run")

@pytest.fixture
def browser(request, url, run):
    # """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_option = Options()
        chrome_option.add_argument('--no-sandbox')
        chrome_option.add_argument('--disable-dev-shm-usage')
        chrome_option.add_argument('start-maximized')
        chrome_option.add_argument('ignore-certificate-errors')
        if run == "remote":
            capabilities = {
                "browserName": "chrome",
                "browserVersion": "85.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            driver = webdriver.Remote(
                command_executor='http://10.10.18.159:4444/wd/hub',
                desired_capabilities=capabilities, options=chrome_option
            )
        elif run == "local":
         driver = webdriver.Chrome(options=chrome_option)
    elif browser == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.DEFAULT_PREFERENCES['frozen']['marionette.contentListener'] = True
        profile.DEFAULT_PREFERENCES['frozen']['network.stricttransportsecurity.preloadlist'] = False
        profile.DEFAULT_PREFERENCES['frozen']['security.cert_pinning.enforcement_level'] = 0
        profile.set_preference('webdriver_assume_untrusted_issuer', True)
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        # profile.set_preference("browser.download.dir", temp_folder)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "text/plain, image/png")
        if run == "remote":
            capabilities = {
                "browserName": "firefox",
                "browserVersion": "80.0",
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": False
                }
            }
            driver = webdriver.Remote(
                command_executor='http://10.10.18.159:4444/wd/hub',
                desired_capabilities=capabilities, firefox_profile=profile)
        elif run == "local":
            driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    elif browser == "opera":
        driver = webdriver.Chrome()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(10)
    request.addfinalizer(driver.close)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
