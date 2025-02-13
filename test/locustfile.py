from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(0.1, 0.2)  # 每个用户请求间隔时间，模拟真实用户行为

    @task
    def post_json(self):
        # 定义 JSON 请求体
        payload = {
            "model": "deepseek-r1:8b",
            "message": "what is 2 plus 2"
        }

        # 设置请求头，指定 JSON 格式
        headers = {'Content-Type': 'application/json'}

        # 发送 POST 请求（HTTPS）
        response = self.client.post("/chat", json=payload, headers=headers)

        # 监测响应状态码
        if response.status_code == 200:
            print(response.json())
        else:
            print(f"请求失败，状态码: {response.status_code}")