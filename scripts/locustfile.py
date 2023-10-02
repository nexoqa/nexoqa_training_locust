import datetime
import json
import random
from locust import HttpUser, constant, task
from locust import events


def timestring():
    now = datetime.datetime.now()
    return datetime.datetime.strftime(now, "%m:%S.%f")[:-5]


class MyUser(HttpUser):
    host = "http://localhost:8081"
    wait_time = constant(1)
    first_start = True

    def get_data(self):
        return json.dumps(self.client.get("http://localhost:8081/songs").json())

    @task
    def test(self):
        data = self.get_data()
        print(f"{data}")
        songs = json.loads(data)
        print(f"{data}")
        id = songs[random.randint(0, len(songs) - 1)]["id"]
        print(f"id={id}")
        self.client.get(f"/songs/:{id}")

    def on_stop(self):
        print("Stopped")
