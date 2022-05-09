from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # update the below path with the path where Chromedriver is located in your local environment
    context.browser = webdriver.Chrome("D:\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    context.base_url = ' http://127.0.0.1:8000/'
    context.browser.maximize_window()
    context.browser.implicitly_wait(2)


def after_all(context):
    context.browser.close()
