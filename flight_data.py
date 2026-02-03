from flight_search import FlightSearch
import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.url = "https://test.api.amadeus.com/v2"
        self.API_KEY = "xxx"
        self.API_SECRET = "xxx"
        self.origin_code = "VNO"

    def find_cheapest_flight(self):
        data = FlightSearch()
        token = data.token_generation()
        iata_data = data.city_codes()
        headers = {"Authorization": f"Bearer {token}"}
        for row in iata_data:
            iata_code = row['iataCode']
            params = {
                "originLocationCode": self.origin_code,
                "destinationLocationCode": iata_code,
                "departureDate": "2025-09-15",
                "adults": 2,
                "currencyCode": "EUR",
            }
            response = requests.get(url = f"{self.url}/shopping/flight-offers", headers = headers, params = params)
            response.raise_for_status()
            final_data = response.json()
            print(final_data)
