from selenium import webdriver


def create_remote_driver(browser_name, platform):
    capabilities = {"browserName": browser_name, "platform": platform}
    return webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities="capabilities",
    )
