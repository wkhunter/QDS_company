import time


class DengLuPage:
    url = "https://pre-www.quandashi.com/"
    # url = "https://www.quandashi.com/"


    cookie=({'name': 'QDS_COOKIE',
             # 'value': '116b79bb072221f47477b4c5980a685f0b4fa2d1',
             'value': 'b170b5f78c3daff5c6133f74356cf834926187b0',#fafce34b93de56ac1bf12c9cd47b003215ef7074
              'Domain': '.quandashi.com'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def dengLu(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)

    def refresh(self):

        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
