import requests
import pandas as pd
from dotenv import load_dotenv


OEC_URL = "https://api-v2.oec.world/tesseract"

class OECClient:
    def __init__(self):
        print("This class interacts with the OEC API")
        self._cubes = self.set_cube_names()
        self._dataset = None

    def set_cube_names(self):
        response = requests.get(f'{OEC_URL}/cubes')

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        cubes = response.json()['cubes']

        names = [cube['name'] for cube in cubes]

        return names

    def get_cube_names(self):
        return self._cubes

    def print_cubes(self):
        count = 0
        for cube_name in self._cubes:
            print(f'{count + 1}.\t{cube_name}')
            count += 1

    def get_cube_schema(self, cube_number):
        cube_name = self._cubes[cube_number - 1]
        response = requests.get(f'{OEC_URL}/cubes/{cube_name}')

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        schema = response.json()

        return schema

    def set_cube_data(self, cube_number, drilldowns, measures, include = None, cube_type = 'jsonrecords'):
        cube_name = self._cubes[cube_number - 1]
        if include:
            parameters = {
                    'cube': cube_name,
                    'drilldowns': drilldowns,
                    'measures': measures,
                    'include': include
            }
        else:
            parameters = {
                    'cube': cube_name,
                    'drilldowns': drilldowns,
                    'measures': measures,
            }

        response = requests.get(f'{OEC_URL}/data.{cube_type}', params = parameters)

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        dataset = response.json()
        self._dataset = pd.DataFrame(dataset['data'])
        return    

    def get_cube_data(self):
        return self._dataset


if __name__ == "__main__":
    oec = OECClient()
    print(oec.get_cube_names())
    oec.set_cube_data(2, "Time,Currency", "Rate")
    data = oec.get_cube_data()
    print(data.head(20))
