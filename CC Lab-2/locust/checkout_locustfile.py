from locust import HttpUser, between, task


class CheckoutUser(HttpUser):
    host = "http://localhost:8000"
    wait_time = between(1, 2)

    @task
    def checkout(self):
        self.client.get("/checkout")
