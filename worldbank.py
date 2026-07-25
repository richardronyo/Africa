import requests
import pandas as pd
"""
This is the backbones of a data pipeline for the World Bank API. It is capable of:
    1. Searching the API with natural language for a dataset
    2. Getting the database associated with a search result
    3. Storing the database as a Pandas DataFrame
"""

WORLDBANK_URL = "https://data360api.worldbank.org/data360"


class WorldBankClient:
    def __init__(self):
        print("This class interacts with the World Bank API")
        self._results = None
        self._dataset = None

    def search(self, search, limit = 10):
        parameters = {
                "count": True,
                "select": "series_description/idno, series_description/name, series_description/database_id",
                "search": search,
                "top": limit
                }

        response = requests.post(f"{WORLDBANK_URL}/searchv2", json = parameters)        

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        results = [result['series_description'] for result in response.json()['value']]
        self._results = results        
        self._db = None
   
    def print_results(self):
        count = 0
        for result in self._results:
            print(count + 1, ".\t", result)
            count += 1
    
    def set_data(self, index, timePeriodFrom = 2020, timePeriodTo = 2025):
        result = self._results[index - 1]
        result_name = result['name']
        result_dbid = result['database_id']
        result_idno = result['idno']
       
        print("Retrieving ", result_name)
        parameters = {"DATABASE_ID": result_dbid, "INDICATOR": result_idno, "timePeriodFrom": timePeriodFrom, "timePeriodTo": timePeriodTo}

        response = requests.get(f"{WORLDBANK_URL}/data", params = parameters)

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

        data = response.json()['value']
        df = pd.DataFrame(data)
        
        self._dataset = df

    def get_dataset(self):
        return self._dataset

if __name__ == "__main__":
    worldbank = WorldBankClient()
    worldbank.search("Nigeria oil", 10)
    worldbank.print_results() 
    worldbank.get_dataset(1)
