import requests
import pandas as pd
from dotenv import load_dotenv


OEC_URL = "https://api-v2.oec.world/tesseract"

class OECClient:
    def __init__(self):
        print("This class interacts with the OEC API")
        self._cubes = self.set_cube_names()

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


if __name__ == "__main__":
    oec = OECClient()

    print(oec.get_cube_names())
