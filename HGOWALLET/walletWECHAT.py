# @Time    : 19-4-16
# @Author  : 欧阳
# @File    : walletWECHAT.py
from selenium import webdriver
import time, os
from HGOCOMMON import uitestlog

testlog = uitestlog.uilog()

class Wallet(object):
    """初始化浏览器"""
    def startup(self, url, driver_name='Chrome'):
        if driver_name == "Chrome":
            self.driver = webdriver.Chrome()
            # chromepath = "./Browser/chromedriver"
            # self.driver = webdriver.Chrome(executable_path=chromepath)
        else:
            self.driver = webdriver.Firefox()
            # firefoxpath = "./Browser/geckodriver"
            # self.driver = webdriver.Firefox(executable_path=firefoxpath)
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    """截图"""
    def screenshots(self, image='WALLET-' + str(time.time()).replace('.', '') + '.png'):
        # if not os.path.exists('../Image'):
        #     os.makedirs('../Image')
        # image_name = os.path.join('../Image', image)
        if not os.path.exists('./Images'):
            os.makedirs('./Images')
        image_name = os.path.join('./Images', image)
        try:
            self.driver.get_screenshot_as_file(image_name)
            testlog.info('截图保存成功' + "-" * 20 + ">" * 2 + " %s", image_name)
        except Exception as e:
            testlog.info('截图保存失败' + "-" * 20 + ">" * 2 + " %s", e)

    """购卡UI自动化"""
    def walletgk(self):
        try:
            self.driver.find_element_by_xpath(
                "//img[@src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABJCAYAAACqyKH+AAABoklEQVR4Ae3cJZSVQQBH8cEh4g79kJB+SLj2sL0QqUjFvo4mEq4Nh4Q7VNwWyroMN8wrz33t/s/5rba7LjPBjdE555xzbue2bfnmYg+u4RsGECeogdTgWmoyt1zAmTiIHkQV1ZMazcwPOB9PDFS1J5ifCzgF9xDz9OIeTiCboE6kBr2Iee5hSuBBR94r+rEfcxAgWqQm/XmtOgIPHiImQ9hssJI2p0YxeRDy3j2vIKisK4hJb8h7l8wQVFaGmGNAAxrQgE1jQAO+xZmy9LZcwOrJgAYchQGfIZSlZwY0YEsY0IAGNGA3npelbr8P9Bvp0RvwF56XpV/+OsvfBxrQgOOAAQ1oQAMa0IAGXIZ7WI9Qpd24Df5vz4BL8Q/d2IVQxmTsxRA+w4DJOnxHxFmsynv9FGzEI0S8xEoEGDBZjPOIyUfcxG38QkQ/DmOWnwNLW4MMz/ATX/AQ+7HcLyKjnwENaEADyoAGNKABZUADjvKADZ7W9LRmg+eFPS/c4Il1T6w3eGeCdyY0cGuHt3Y0cG+M98Y0cHORNxeNgznnnHPO/Qebj0g868LslgAAAABJRU5ErkJggg==']").click()
            self.driver.find_element_by_xpath("//a[@href='/valuecard/buycard/page']").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div/div[2]/div/div[2]/div/div[3]").click()
            self.screenshots()
            self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div/div/div/div[2]/div/div[6]/div[2]/div[3]").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div/div/div/div[2]").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[5]/button").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"error\"]/div/div[2]/div[3]/a").click()
            self.screenshots()
        except BaseException as e:
            testlog.info('页面元素定位失败' + "-" * 20 + ">" * 2 + " %s", e)

    """充值UI自动化"""
    def walletcz(self):
        try:
            self.driver.find_element_by_xpath(
                "//img[@src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABJCAYAAACqyKH+AAABoklEQVR4Ae3cJZSVQQBH8cEh4g79kJB+SLj2sL0QqUjFvo4mEq4Nh4Q7VNwWyroMN8wrz33t/s/5rba7LjPBjdE555xzbue2bfnmYg+u4RsGECeogdTgWmoyt1zAmTiIHkQV1ZMazcwPOB9PDFS1J5ifCzgF9xDz9OIeTiCboE6kBr2Iee5hSuBBR94r+rEfcxAgWqQm/XmtOgIPHiImQ9hssJI2p0YxeRDy3j2vIKisK4hJb8h7l8wQVFaGmGNAAxrQgE1jQAO+xZmy9LZcwOrJgAYchQGfIZSlZwY0YEsY0IAGNGA3npelbr8P9Bvp0RvwF56XpV/+OsvfBxrQgOOAAQ1oQAMa0IAGXIZ7WI9Qpd24Df5vz4BL8Q/d2IVQxmTsxRA+w4DJOnxHxFmsynv9FGzEI0S8xEoEGDBZjPOIyUfcxG38QkQ/DmOWnwNLW4MMz/ATX/AQ+7HcLyKjnwENaEADyoAGNKABZUADjvKADZ7W9LRmg+eFPS/c4Il1T6w3eGeCdyY0cGuHt3Y0cG+M98Y0cHORNxeNgznnnHPO/Qebj0g868LslgAAAABJRU5ErkJggg==']").click()
            self.driver.find_element_by_xpath("//a[@href='/valuecard/recharge/chargepage']").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div/div/div[2]/a/button").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div/div/div[2]/a/div").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//input[@type='number']").send_keys("100")
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div/div[3]/div[2]/button").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div/div[2]/div[5]/button").click()
            self.screenshots()
            self.driver.find_element_by_xpath("//*[@id=\"error\"]/div/div[2]/div[3]/a").click()
            self.screenshots()
        except BaseException as e:
            testlog.info('页面元素定位失败' + "-" * 20 + ">" * 2 + " %s", e)

    def quit(self):
        time.sleep(2)
        self.driver.quit()

Autotest = Wallet()
if __name__ == '__main__':
    # 谷歌浏览器购卡
    Autotest.startup('http://172.17.13.74/omw-wxui/?state=gh_f79e23f74622&code=believe_limin')
    Autotest.walletgk()
    Autotest.quit()
    # 谷歌浏览器充值
    Autotest.startup('http://172.17.13.74/omw-wxui/?state=gh_f79e23f74622&code=believe_limin')
    Autotest.walletcz()
    Autotest.quit()
    # 火狐浏览器购卡
    # Autotest.startup('Firefox', 'http://172.17.13.74/omw-wxui/?state=gh_f79e23f74622&code=believe_limin')
    # Autotest.walletgk()
    # Autotest.quit()
    # 火狐浏览器充值
    # Autotest.startup('Firefox', 'http://172.17.13.74/omw-wxui/?state=gh_f79e23f74622&code=believe_limin')
    # Autotest.walletcz()
    # Autotest.quit()
