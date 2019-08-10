'''
我的评价 测试用例

author:llj
'''
from time import sleep

from page.evaluate_page import EvaluatePage
import pytest
import allure
class TestEvaluate:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)  # 设置用例等级为CRITICAL
    @allure.step(title='我的评价')
    def test_evaluate(self,open_mobil):
        driver = open_mobil
        allure.attach("进入个人中心", "进入个人中心,点击收货,获取商品名称")
        EvaluatePage(driver).click_my()
        sleep(3)
        EvaluatePage(driver).wait_received()
        EvaluatePage(driver).received_goods(0)
        EvaluatePage(driver).click_ok()
        sleep(3)
        allure.attach("返回个人中心", "返回个人中心,点击我的评价,对刚收货的商品进行评价")
        EvaluatePage(driver).back()
        sleep(3)
        EvaluatePage(driver).click_evaluate()
        goodsname = EvaluatePage(driver).get_evaluate_goodsname(0)
        sleep(3)
        allure.attach("获取商品名称", f"点击评价晒图,获取评价的商品名称{goodsname}")
        EvaluatePage(driver).evaluate_goods(0)
        sleep(3)
        EvaluatePage(driver).input_evaluate("值得购买")
        # 商品等级0
        EvaluatePage(driver).start_5(0)
        # 物流等级1
        EvaluatePage(driver).start_5(1)
        # 服务等级2
        EvaluatePage(driver).start_5(2)
        # 商品评价3
        EvaluatePage(driver).start_5(3)
        sleep(3)
        # 提交评价
        EvaluatePage(driver).Submission()
        # 获取toast
        data = EvaluatePage(driver).get_toast("评价成功")
        allure.attach("评价成功", f"提交成功，显示toast信息{data}")
        allure.attach("断言", "收货商品和刚生成已评价商品名称一致")
        EvaluatePage(driver).click_evaluated()
        evaluateds = EvaluatePage(driver).evaluated_name()
        if goodsname in evaluateds:
            print("评价成功")
            assert (1,1)
        else:
            assert False








