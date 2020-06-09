import requests,unittest

from api.login import Login

# 创建测试类
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.session=requests.session()
        # 初始化封装登录api类
        self.login_api = Login()

    def tearDown(self) -> None:
        self.session.close()

    # 创建测试函数
    def test_login_success(self):
        # 调用登录接口
        response_login = self.login_api.login(self.session,{"mobile": "18598274082",
                                                            "password": "19ede66f218015fd9df85ac886488926",
                                                            "way": "0"})
        # 设置返回数据类型为字典
        jsonData = response_login.json()  # type:dict
        print("登录结果:", jsonData)
        # 断言响应状态码
        self.assertEqual(200, response_login.status_code)
        # 断言errorMessage数据
        self.assertEqual(None, jsonData.get("errorMessage"))
        pass
