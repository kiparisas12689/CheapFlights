import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/xxxx/flightDealsForMe/prices"

    def get_rows(self):
        response = requests.get(url = self.url)
        data = response.json()
        return data['prices']

    def update_rows(self, sheet_data):
        for row in sheet_data:
            if row['iataCode']:
                update_url = f"{self.url}/{row['id']}"
                params = {
                    "price": {
                        "iataCode": row['iataCode']
                    }
                }
                response = requests.put(url = update_url, json = params)
