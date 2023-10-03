from locust import User, task, constant

class UseUserClass(User):
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the URL")

    @task
    def search(self):
        print("Searching")