from apis.api_client import APIClient


class AuthClient(APIClient):
    def login(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        return self.post("/auth/login", json_data=payload)
