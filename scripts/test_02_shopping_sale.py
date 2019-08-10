'''
活动商品都买流程 测试用例

author:llj
'''
from time import sleep

from page.shopping_goods_page import ShoppingPage
from page.shopping_order_page import ShoppingOrderPage
from page.evaluate_page import EvaluatePage
import pytest
import allure

class TestshoppingSale:
    '''购买活动商品'''

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='使用余额购活动商品')
    def test_shopping_sale(self,open_mobil):
        #选择活动商品
        driver  = open_mobil
        allure.attach("选择活动商品", "选择一款活动商品,立即购买不,加入购物车")
        ShoppingPage(driver).click_sales()
        sleep(3)
        ShoppingPage(driver).choice_sale_good(4)
        sleep(3)
        ShoppingPage(driver).buy_first()
        sleep(3)
        # 进入订单详情页
        allure.attach("下订单", "订单详情页面")
        ShoppingOrderPage(driver).choice_use_balance()  #选择使用余额
        before_balance = ShoppingOrderPage(driver).get_balance()  #使用前余额值
        allure.attach("使用前余额", f"使用前余额:{before_balance}")
        use_balance= ShoppingOrderPage(driver).get_use_balance()  # 获取使用的额度
        allure.attach("使用额度", f"使用额度:{use_balance}")
        sleep(3)
        ShoppingOrderPage(driver).click_place_order() # 提交订单
        ShoppingOrderPage(driver).send_pay_ps() # 输入支付密码
        ShoppingOrderPage(driver).click_pay() # 点击确定
        sleep(3)
        order_num = ShoppingOrderPage(driver).get_order_nu() # 获取生成的定单号
        allure.attach("获取订单号", f"生成的订单号:{order_num}")
        sleep(3)
        # 进入个人中心  获取 使用过后的余额值
        allure.attach("个人中心", "获取验证")
        driver.back()
        driver.back()
        driver.back() #三次返回首页
        sleep(3)
        EvaluatePage(driver).click_my()
        now_balance = EvaluatePage(driver).get_cuser_balance()
        allure.attach("使用后余额", f"使用后余额:{now_balance}")
        # 断言 使用的额度+剩余的余额=使用前的余额
        assert(before_balance,now_balance+use_balance)