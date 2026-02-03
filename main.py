#This file will need to use the DataManager,FlightSearch, FlightData classes to achieve the program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

TOKEN = FlightSearch()
TOKEN.token_generation()

iata_data = TOKEN.city_codes()

sheety_data = DataManager()
sheet_data = sheety_data.get_rows()
print(sheet_data)
print(iata_data)
for row in sheet_data:
    if row['iataCode'] == "":
        for location in iata_data:
            if location['city'] == row['city']:
                row['iataCode'] = location['iataCode']
                break

sheety_data.update_rows(sheet_data)

flight_data = FlightData()
flight_data.find_cheapest_flight()
