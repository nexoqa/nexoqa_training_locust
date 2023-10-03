from locust import HttpUser, constant, task

class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "http://localhost:8081"

    @task
    def get_users(self):
        res = self.client.get("/songs")
        print(res.status_code)