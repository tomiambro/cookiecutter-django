import logging
from locust import HttpUser, task

class WebsiteUser(HttpUser):
    @task
    def test_home_page(self):
        self.client.get("/")
    
    user_data = {"username": "locust", "password": "locust"}

    def on_start(self):
        # Create a new user
        response = self.client.post("/api/users/register/", self.user_data)
        if response.status_code == 201:
            logging.info("User created successfully")
        else:
            logging.error(response.json())
            raise Exception("Cannot create user")

        # Perform authentication
        response = self.client.post("/auth-token/", self.user_data)
        if response.status_code == 200:
            # Save the token in the session
            self.client.headers["Authorization"] = "Token " + response.json()["token"]
            logging.info("User authenticated successfully")
        else:
            # Authentication failed, raise an exception
            logging.error(response.json())
            raise Exception("Failed to authenticate")
        
    def on_stop(self):
        # Delete the recently created user
        response = self.client.delete("/api/users/locust/")
        if response.status_code == 204:
            logging.info("User deleted successfully")
        else:
            logging.error(response.json())
            raise Exception("Cannot delete user")
        