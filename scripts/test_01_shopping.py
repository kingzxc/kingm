'''
非活动商品都买流程
author:llj
'''
from time import sleep

from page.shopping_goods_page import ShoppingPage
from page.shopping_order_page import ShoppingOrderPage
from page.evaluate_page import EvaluatePage
import pytest
import allure

class Testshopping:
    '''购买非活动商品'''

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='使用余额购普通商品')
    def test_shopping(self,open_mobil):
        #选择非活动商品--分类
        driver  = open_mobil
        ShoppingPage(driver).click_classify()
        ShoppingPage(driver).click_shoes()
        ShoppingPage(driver).click_kinds()
        ShoppingPage(driver).choice(2)
        sleep(3)
        allure.attach("选择商品", "将商品加入购物车,从购物车下单")
        # ShoppingPage(driver).choice_good() #向上滑动
        # 将商品加入购物车进行购买
        ShoppingPage(driver).click_car()
        ShoppingPage(driver).click_incar()
        ShoppingPage(driver).buy()
        sleep(3)
        allure.attach("下订单", "订单详情页面")
        # 立即购买进入订单详情页
        sleep(3)
        ShoppingOrderPage(driver).choice_use_balance()  #选择使用余额
        before_balance = ShoppingOrderPage(driver).get_balance()  #使用前余额值
        allure.attach("使用前余额", f"使用前余额:{before_balance}")
        use_balance= ShoppingOrderPage(driver).get_use_balance()  # 获取使用的额度
        allure.attach("使用额度", f"使用额度:{use_balance}")
        sleep(3)
        ShoppingOrderPage(driver).click_place_order() # 提交订单
        ShoppingOrderPage(driver).send_pay_ps() # 输入支付密码
        ShoppingOrderPage(driver).click_pay() # 点击确定
        order_num = ShoppingOrderPage(driver).get_order_nu() # 获取生成的定单号
        allure.attach("获取订单号", f"生成的订单号:{order_num}")
        sleep(3)
        # 进入个人中心  获取 使用过后的余额值
        allure.attach("个人中心", "获取验证")
        driver.back()
        driver.back()
        EvaluatePage(driver).click_my()
        now_balance = EvaluatePage(driver).get_cuser_balance()
        allure.attach("使用后余额", f"使用后余额:{now_balance}")
        # 断言 使用的额度+剩余的余额=使用前的余额
        assert(before_balance,now_balance+use_balance)
