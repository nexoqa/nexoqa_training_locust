from locust import SequentialTaskSet, constant, task, HttpUser
import random


class SequentialTaskSetExample(SequentialTaskSet):
    @task
    def get(self):
        self.client.get("/songs")
        print("Get Songs")

    @task
    def get_random_songs(self):
        songs = [1, 2, 3, 4, 5]
        id = str(random.choice(songs))
        random_url = "/songs/" + id
        res = self.client.get(random_url)
        print(f"Random songs {id}")


class MyLoadTest(HttpUser):
    host = "http://localhost:8081"
    tasks = [SequentialTaskSetExample]
    wait_time = constant(1)
