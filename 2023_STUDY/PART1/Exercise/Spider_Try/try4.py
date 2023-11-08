import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



class AutoSpider:

    def __init__(self):
        # self.driver = webdriver.Chrome()  # 创建了一个Chrome浏览器的WebDriver实例
        self.driver = self.set_options()
        self.driver.maximize_window()  # 最大化窗口
        self.driver.implicitly_wait(2)  # 隐式等待,设置最大的等待时长,只对查找元素(find_elementXXX)生效

    @staticmethod
    def set_options():
        # ChromeOptions类提供了对Chrome浏览器各种选项进行配置的方法;
        # 在excludeSwitches参数中，将enable-logging指定为要排除的选项，表示不启用浏览器的日志功能
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default")
        options.add_experimental_option('useAutomationExtension', False)  # 去掉开发者警告
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # options.add_experimental_option('excludeSwitches', ['enable-logging'])
        return webdriver.Chrome(options=options)

    def method(self):
        """代码执行"""
        lst1 = []
        self.driver.get("https://www.sciencedirect.com/journal/the-crop-journal/vol/11/issue/5")

        elements_1 = self.driver.find_elements(By.CSS_SELECTOR, '[class="article-content"]')
        article_time_temp = self.driver.find_element(By.CSS_SELECTOR, '[class="js-issue-status"]').text
        article_time = re.match("\d\d\d\d", article_time_temp, re.S)
        print(article_time)
        for i in range(1, len(elements_1)):
            temp = elements_1[i]
            title = temp.find_element(By.CSS_SELECTOR, '[class="js-article-title"]').text
            article_url = temp.find_element(By.CSS_SELECTOR, '[class="article-content-title"]').get_attribute("href")
            article_writer = temp.find_element(By.CSS_SELECTOR, '[class="js-article__item__authors"]').text
            lst1.append([title, article_url, article_writer, article_time])
        print(lst1)
        time.sleep(5)
        input('等待回车键结束程序')

    # def generate_url(self):
    #     for i in range(10, 0, -1):
    #         for j in range(1, 10):

    def sign_out(self) -> None:
        """
        退出浏览器:
        关闭当前浏览器窗口或标签页。如果只有一个窗口或标签页被打开，调用driver.close()将会关闭整个浏览器会话。
        如果有多个窗口或标签页存在，调用driver.close()将关闭当前活动窗口或标签页，并切换到上一个窗口或标签页。
        """

        self.driver.close()
        self.driver.quit()  # 关闭浏览器，调用driver.quit()会终止WebDriver对象的相关进程和资源，及时清理测试环境。


if __name__ == "__main__":
    AutoSpider().method()
