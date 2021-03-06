# coding=utf-8
import random
import re
import time
from selenium.webdriver import ActionChains
from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class CxZcTest(MyTestCase):
    """查询注册测试集"""

    def test_free_search(self):
        """免费商标查询测试"""

        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(2) > dd > a:nth-child(1)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        self.assertIn("注册商标查询_中国商标查询_权大师官网",self.driver.title)
        print(self.driver.title)
        get_screenshort(self.driver, "test_free_search.png")

    def test_domestic_trademark(self):
        """国内商标查询测试"""

        dl = DengLuPage(self.driver)
        # 官方推荐有find_element(By.*(""))代替find_element_by_*("")
        # self.driver.find_element_by_id()
        # self.driver.find_element()
        dl.login()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > h3 > span")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_css_selector(
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(2) > dd > a:nth-child(2)").click()
        time.sleep(3)

        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("国内商标查询|国内商标查询报告|中国商标查询网-权大师",self.driver.title)
        print(self.driver.title)

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            aa = a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        self.driver.find_element_by_name("ownerContactPerson").send_keys("{}".format(unicode()))
        self.driver.find_element_by_name("ownerContactPhone").send_keys("15624992498")
        self.driver.find_element_by_name("contactMail").send_keys("145647@qq.com")
        self.driver.find_element_by_css_selector("#remark").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_domestic_trademark.png")

        for i in self.driver.find_elements_by_css_selector(
                "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):
            print("总价:" + i.text)
            ii = i.text

        self.assertIn(aa, ii)
        print("价格一致")

        self.driver.find_element_by_css_selector(
            "body > div.section-myorder.orderinfo-wrap.width1200 > div:nth-child(6) > div.btns > a.btn-next.submitOrder").click()

        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:" + o.text)
            oo = o.text

        self.assertIn(oo, ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_TrademarkSearchScreeningConditions(self):
        """商标搜索筛选条件测试"""

        dl = DengLuPage(self.driver)
        time.sleep(2)
        self.driver.get("https://so.quandashi.com")
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.title)
        dl.refresh()
        self.driver.find_element_by_name("key").send_keys("大王")
        print("商标名称:大王")
        self.driver.find_element_by_css_selector("#btnSearchkey").click()
        time.sleep(5)
        result_1 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
        print(str(result_1))
        sl_1 = int(re.sub("\D", "", result_1))

        """筛选条件"""
        self.driver.find_element_by_css_selector("#searchList > div.page-form.w-center > ul > li:nth-child(1) > a").click()
        number = random.randint(1,45)
        lb = self.driver.find_element_by_css_selector("#searchList > div.page-form.w-center > ul > li.search-category.open > div.category-show-box.select-show-category > a:nth-child({})".format(number)).text
        self.driver.find_element_by_css_selector("#searchList > div.page-form.w-center > ul > li.search-category.open > div.category-show-box.select-show-category > a:nth-child({})".format(number)).click()
        print("选择申请类别:" + lb)
        time.sleep(5)

        result_2 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
        print(str(result_2))
        sl_2 = int(re.sub("\D", "", result_2))

        if sl_1 > sl_2:
            print("商标搜索筛选申请类别测试通过!")
        else:
            self.assertEqual(sl_1,sl_2,"筛选条件异常请及时查看!")

    def test_TrademarkSearchFollow(self):
        """商标搜索点击关注测试"""

        dl = DengLuPage(self.driver)
        time.sleep(2)
        self.driver.get("https://so.quandashi.com")
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.title)
        dl.refresh()
        self.driver.find_element_by_name("key").send_keys("大王")
        print("商标名称:大王")
        self.driver.find_element_by_css_selector("#btnSearchkey").click()
        time.sleep(5)
        result_1 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
        print(str(result_1))
        info = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href").text
        print(str(info).replace("\n"," "))

        """点击关注"""
        self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.brand-status > div:nth-child(1) > span").click()
        time.sleep(2)
        # 确定弹框
        self.driver.find_element_by_link_text("确 定").click()
        # 跳转到商标监控页面

        # windows = self.driver.window_handles
        # self.driver.switch_to.window(windows[-1])
        # time.sleep(2)
        # self.driver.set_window_size(1920, 1080)
        # dl.refresh()
        # jk = self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr").text
        # print(str(jk).replace("删除",""))
        #
        # # 删除监控
        # self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr > td:nth-child(4) > a").click()
        # time.sleep(1)
        # self.driver.find_element_by_css_selector("#addSuccessModal > div > div > table > tbody > tr.tr-2 > td > div > a.mybtn.mybtn-inverse.btn-sure").click()
        # time.sleep(2)
        # print(self.driver.find_element_by_css_selector("body > div.brandMonitor-wrap > div > div > div.myPanel-bodyer.brandMonitor-all > div > table > tbody > tr > td").text)

        print("关注商标测试通过!")

    def test_TrademarkSearchBusiness(self):
        """商标搜索后续业务测试"""

        dl = DengLuPage(self.driver)
        time.sleep(2)
        self.driver.get("https://so.quandashi.com")
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        print(self.driver.title)
        dl.refresh()
        self.driver.find_element_by_name("key").send_keys("大王")
        print("商标名称:大王")
        self.driver.find_element_by_css_selector("#btnSearchkey").click()
        time.sleep(5)
        result_1 = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > div.search-top").text
        print(str(result_1))
        info = self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.result-href").text
        print("商标信息:" + str(info).replace("\n"," "))

        """点击后续业务"""
        self.driver.find_element_by_css_selector("#searchList > div.page-content.w-center > div.page-content-left > ul > li:nth-child(1) > div.brand-status > div:nth-child(2) > a:nth-child(1)").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        print("后续业务:" + self.driver.title)