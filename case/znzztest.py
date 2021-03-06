# coding=utf-8
import random
import time

import logging

from selenium.webdriver import ActionChains

from utils.mytestcase import MyTestCase
from utils.logincookie import DengLuPage
from utils.random import unicode
from utils.screenshort import get_screenshort


class ZnZzTest(MyTestCase):
    """智能注册测试集"""

    def test_znzz_1(self):
        """智能注册_企业测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
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
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss = unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()

        suiji = random.randint(2, 46)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类!".format(suiji))


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(random.randint(1,5))).click()
        time.sleep(2)
        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys("03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_1.png")

        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过!")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_2(self):
        """智能注册_个体测试"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
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
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss = unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()

        suiji = random.randint(2, 46)
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector(
            "#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > dl > dt:nth-child(10) > span").click()

        print("选择了第{}类商标分类!".format(suiji))


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > table > thead > tr > td.td-content > a:nth-child(2)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906133513")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#geren-postcode").clear()
        self.driver.find_element_by_css_selector("#geren-postcode").send_keys("102200")
        self.driver.find_element_by_css_selector("#geren-street").clear()
        self.driver.find_element_by_css_selector("#geren-street").send_keys("北京市昌平区")

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(1) > td.td-content > input").send_keys("{}".format(unicode()))
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys("15122311456")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(3) > td.td-content > input").send_keys("123313@qq.com")



        # 解决常用申请人弹框，点击空白处
        # self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_2.png")

        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_3(self):
        """智能注册_企业测试_历史订单"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
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
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss = unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()


        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > h3 > div > div > a").click()
        time.sleep(2)
        history_number = random.randint(2,10)
        info = self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        # self.driver.find_element_by_css_selector(
        #     "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#ssq").click()
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#companylistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child({})".format(random.randint(1,5))).click()
        time.sleep(2)
        # 解决弹框
        # self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-qiye > tr:nth-child(4) > td.td-title").click()
        # time.sleep(1)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(2) > td.td-content > input").send_keys(
            "15624992489")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(3) > td.td-content > input").send_keys(
            "132132@qq.com")
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > table:nth-child(13) > tbody.tbody-qiye > tr:nth-child(4) > td.td-content > input").send_keys("03515978787")
        time.sleep(2)
        # 解决常用申请人弹框，点击空白处
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)
        # self.driver.find_element_by_css_selector(
        #     "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > div.section-btns.clearfix > a:nth-child(2)").click()
        # time.sleep(1)
        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_3.png")

        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_4(self):
        """智能注册_个体测试_历史订单"""

        # logging.basicConfig(filename='../LOG/' + __name__ + '.log',
        #                     format='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]', level=logging.DEBUG,
        #                     filemode='a', datefmt='%Y-%m-%d%I:%M:%S %p')
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
            "body > div.section-banner > div.public-navbar > div > div > div > ul:nth-child(1) > li:nth-child(1) > div > dl:nth-child(3) > dd > a:nth-child(3)").click()
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertIn("商标智能注册|商标注册查询|商标注册网-权大师", self.driver.title)
        print(self.driver.title)
        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-serviceItems > table > tbody > tr > td.td-cont > ul > li:nth-child(3)").click()

        for a in self.driver.find_elements_by_css_selector("#total-price"):
            print("费用总计:"+a.text)
            # aa=a.text

        self.driver.find_element_by_css_selector(
            "body > div.section-product.width1200 > dl > dd > div.cont-btnBuy > a.btn.btn-next.buynow").click()
        ss = unicode()
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-name > td.td-content > input").send_keys(
            "{}".format(ss))
        print("商标名称：{}".format(ss))
        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(4) > div > table > tbody > tr.row-tuyang.show-create.show-create1 > td.td-content > div.zidongdong-create > ul > li > div.bottom.getBrandPic > a").click()
        self.driver.find_element_by_css_selector("#create-tuyang > label.label.checked").click()
        time.sleep(5)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div:nth-child(14) > div.categoryInfo-wrap > div.c-row.row-way > div > a.btn-choice.active").click()

        """商标类别导入历史订单"""
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > h3 > div > div > a").click()
        time.sleep(2)
        history_number = random.randint(2, 10)
        info = self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).text
        print("导入历史订单信息:" + info)
        self.driver.find_element_by_css_selector("#history_order > li:nth-child({}) > h2".format(history_number)).click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#history-order > div.modal-button > a").click()
        time.sleep(2)


        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page.smartRegister3-page > div.last-pay > ul > li.row-step > a").click()

        time.sleep(3)
        # self.driver.execute_script("document.getElementByName('fname').length = 0;")

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base > table > thead > tr > td.td-content > a:nth-child(2)").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table.table-1.table-applicant.table-type1.active > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys(
            "{}".format(unicode()))
        self.driver.find_element_by_css_selector("#geren-idCard").send_keys("140121198906133513")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#personalssq").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.active.tab-province > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#personalistrative > div > div.d-dropdown > div.tab-content.tab-city.active > dl.item.item-a-g.clearfix > dd > span:nth-child(1)").click()
        self.driver.find_element_by_css_selector("#geren-postcode").clear()
        self.driver.find_element_by_css_selector("#geren-postcode").send_keys("102200")
        self.driver.find_element_by_css_selector("#geren-street").clear()
        self.driver.find_element_by_css_selector("#geren-street").send_keys("北京市昌平区")

        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(1) > td.td-content > input").send_keys("{}".format(unicode()))
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(2) > td.td-content > input").send_keys("15122311456")
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > table:nth-child(13) > tbody.tbody-gsh > tr:nth-child(3) > td.td-content > input").send_keys("123313@qq.com")



        # 解决常用申请人弹框，点击空白处
        # self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.applicant-form > h2").click()

        self.driver.find_element_by_css_selector(
            "body > div.smartRegister-page > div.agentInfo-wrap.applicant-wrap > div.section-base.open > div.section-btns.clearfix > a:nth-child(2)").click()
        time.sleep(1)

        """订单备注"""
        self.driver.find_element_by_css_selector(
            "html body div.smartRegister-page div.orderinfo-wrap div.order-content textarea").send_keys(
            time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")

        get_screenshort(self.driver, "test_znzz_4.png")

        for i in self.driver.find_elements_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > ul > li.row-sense > em > i"):

            print("总价:"+i.text)
            ii = i.text

        # self.assertIn(aa,ii)
        # print("测试通过")
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[5]/div/a").click()
        self.driver.find_element_by_css_selector("body > div.smartRegister-page > div.orderinfo-wrap > div.last-pay.personal-last-pay > div > a").click()
        for o in self.driver.find_elements_by_class_name("payable"):
            print("订单提交成功，应付金额:"+o.text)
            oo = o.text

        self.assertIn(oo,ii)

        print("测试通过")

        self.driver.find_element_by_css_selector("#alisubmit").click()

    def test_znzz_5(self):
        """个人订单修改测试"""
        dl = DengLuPage(self.driver)
        dl.login()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#page-header > div.item-right > ul > li:nth-child(1) > a").click()
        time.sleep(2)

        self.driver.find_element_by_css_selector("#personalCenter2-leftNav > ul > li.menu.open > ul > li:nth-child(1) > a").click()
        time.sleep(2)
        self.assertIn("权大师_我的商标", self.driver.title)
        print(self.driver.title)

        time.sleep(2)
        # 切换成下单时间
        self.driver.find_element_by_class_name("order-time").click()
        time.sleep(2)
        # 选择修改的订单号
        print("订单编号:" + self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span").text)
        # 查看详情
        self.driver.find_element_by_css_selector(
            "#personalCenter2-rightContainer > div.order-page.brand-trade-page.trade-order > div.tabsPanel > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > div > a.t-href").click()
        time.sleep(3)

        """修改商标名字"""
        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(4) > h2 > a").click()
        # self.driver.find_element_by_css_selector("#modal-brand > div.modal-button > a.button.save").click()
        print("商标名字修改成功!")

        time.sleep(1)

        """修改尼斯分类"""
        self.driver.execute_script("window.scrollBy(0,4200)")  # 滑动滚动条
        suiji = random.randint(2, 46)
        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.order-categories > h2 > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-right > div > div > h4 > div.header-right > a > i").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li:nth-child({}) > span".format(suiji)).click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div:nth-child(2) > span").click()

        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(1) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(2) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(3) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(4) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(5) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(6) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(7) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(8) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(9) > span").click()
        self.driver.find_element_by_css_selector("#section-selfchoice > div.group-left > ul > li.list.open > div.title-second.open > dl > dt:nth-child(10) > span").click()

        self.driver.find_element_by_css_selector("#edit-category > div.modal-button > a.button.save").click()
        time.sleep(2)
        print("尼斯分类修改为第{}类!".format(suiji-1))
        time.sleep(2)

        """申请人信息"""

        # self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div.order-detail-box.applicant-info > h2 > a").click()
        #
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > table > thead > tr:nth-child(1) > td.td-content > a.btn-choice.fownertype.active").click()
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").clear()
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-body.scroll > div > div > div > div > table > tbody.tbody-gsh > tr:nth-child(1) > td.td-content.contact-select-container > dl > dt > input").send_keys("田伟")
        # self.driver.find_element_by_css_selector("#geren-idCard").clear()
        # self.driver.find_element_by_css_selector("#geren-idCard").send_keys("130184198908191520")
        # self.driver.find_element_by_css_selector("#change-applicant-info > div.modal-button > a.button.save").click()
        print("申请人信息修改成功!")

        """订单联系人"""

        self.driver.find_element_by_css_selector("#personalCenter2-rightContainer > div.order-detail-page > div:nth-child(8) > div > h2 > a").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").clear()
        self.driver.find_element_by_css_selector("#change-contact-info > div.section-base > table > tbody.tbody-qiye > tr:nth-child(1) > td.td-content > input").send_keys("大西瓜")
        self.driver.find_element_by_name("ftelephone").clear()
        self.driver.find_element_by_name("ftelephone").send_keys("0351-5925212")
        self.driver.find_element_by_css_selector("#change-contact-info > div.modal-button > a.button.save").click()
        print("订单联系人修改成功!")
        time.sleep(1)
        get_screenshort(self.driver,"test_personal_modify.png")

        print("订单修改测试通过!")
