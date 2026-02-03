import requests
from data_manager import DataManager

class FlightSearch:
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v1"
        self.API_KEY = "xxx"
        self.API_SECRET = "xxx"

    def token_generation(self):
        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": self.API_KEY,
            "client_secret": self.API_SECRET
        }
        response = requests.post(url = f"{self.url}/security/oauth2/token", headers = header, data = data)
        data = response.json()
        token = data["access_token"]
        return token

    def city_codes(self):
        token = self.token_generation()
        data_manager = DataManager()
        rows = data_manager.get_rows()

        results = []

        for row in rows:
            params = {
                "keyword": row['city']
            }
            headers = {
                "Authorization": f"Bearer {token}"
            }
            response = requests.get(url = f"{self.url}/reference-data/locations/cities", params = params, headers = headers)
            data = response.json()
            results.append({
                "city": row['city'],
                "iataCode": data['data'][0]['iataCode'] if data["meta"]["count"] > 0 else None
            })
        return results
