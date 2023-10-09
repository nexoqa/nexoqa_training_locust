from locust import HttpUser, SequentialTaskSet, constant, task
import json
import random


class RegisterAndLogin(SequentialTaskSet):
    data = ""
    userToken = ""

    @task
    def register(self):
        id = str(random.randrange(1, 1000))
        name = f"/register/user{id}"
        self.data = '{"email":"user' + id + '@vtech.com", "password":"Ab12345678"}'
        headers = {"Content-Type": "application/json"}
        self.client.post(
            "/register", name=name, json=json.loads(self.data), headers=headers
        )

    @task
    def login(self):
        headers = {"Content-Type": "application/json"}
        with self.client.post(
            "/login", json=json.loads(self.data), headers=headers
        ) as response:
            responseJson = json.loads(response.text)
            self.userToken = responseJson["token"]

    @task
    def getBookmarks(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.userToken,
        }
        self.client.get("/bookmarks", headers=headers)


class RegisterHttpUser(HttpUser):
    host = "http://localhost:8081"
    wait_time = constant(1)
    tasks = [RegisterAndLogin]
