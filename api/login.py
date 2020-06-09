#封装接口
class Login:
    def __init__(self):
        self.login_url = "http://192.168.1.135:8082/api/user/login"

        # 封装登录函数
    def login(self, session, data):
            response_login = session.post(self.login_url, data=data)
            return response_login
