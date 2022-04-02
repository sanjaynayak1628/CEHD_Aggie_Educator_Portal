from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    context.browser = webdriver.Chrome("D:\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    context.base_url = 'https://enigmatic-waters-43189.herokuapp.com/'
    context.browser.implicitly_wait(2)


def after_all(context):
    context.browser.close()


def before_feature(context, feature):
    pass
