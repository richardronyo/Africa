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

    def get_cube_columns(self, cube_number):
        cube_name = self._cubes[cube_number]
        response = requests.get(f'{OEC_URL}/cubes/{cube_name}')

        if response.status_code != 200:
            print('Request failed')
            print('Status: ', response.status_code)
            print('Response: ', response.text)
            return

        return response.json()

    def print_cubes(self):
        count = 0
        for cube_name in self._cubes:
            print(f'\t{count + 1}. {cube_name}')
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

    def get_cube_members(self, cube_number, level):
        cube_name = self._cubes[cube_number - 1]
        parameters = {
            'cube': cube_name,
            'level': level
        }

        response = requests.get(f'{OEC_URL}/members', params = parameters)

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        members = response.json()

        return members
        
    def set_cube_data(self, cube_number, drilldowns, measures, include = None, properties = None, cube_type = 'jsonrecords'):
        cube_name = self._cubes[cube_number]
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

        if properties:
            parameters['properties'] = properties
        response = requests.get(f'{OEC_URL}/data.{cube_type}', params = parameters)

        if response.status_code != 200:
            print("Request failed")
            print("Status: ", response.status_code)
            print("Response: ", response.text)

            return

        self._dataset = response.json()['data']
        return    

    def dataset_to_df(self):
        if self._dataset:
            df = pd.DataFrame(self._dataset)
            return df
        else:
            print("No dataset available")
            return None

def print_dic(dictionary):
    for key, value in dictionary.items():
        print(key)

        if type(value) == dict:
            print_dic(value)
        if type(value) == list:
            for entry in value:
                print_dic(entry)
        else:
            print(f'\t{value}')


def main():
    """
    This will act as the interface for the OEC API 
    """
    oec = OECClient()

    print("Welcome to the OEC API Inteface!")
    running = True
    while running:
        print("---------------------------------------------------------------------")
        option = input("Select an option\n\t1. View Available Datasets\n\t2. View Schema\n\t3. Get Dataset\n\t4. Get Members\n\t5. Save Dataset\n\t6. View Dataset Columns\n\t7. Exit\nEnter your choice: ") 
        if int(option) == 1:
            print("Available Datasets")
            oec.print_cubes()

        if int(option) == 2:
            cube = input("\tDataset Number: ")
            schema = oec.get_cube_schema(int(cube))
            print_dic(schema)

        if int(option) == 3:
            cube_number = input("Enter the cube number: ")
            cube_number = int(cube_number) - 1
            drilldowns = input("\tEnter Drilldowns: ")
            measures = input("\tEnter Measures: ")
            include = input("Enter Include: ")

            print(f'Getting dataset: {oec.get_cube_names()[cube_number]}')
            oec.set_cube_data(cube_number, drilldowns = drilldowns, measures = measures, include = include)

        if int(option) == 4:
            cube_number = input("Enter the cube number: ")
            cube_number = int(cube_number) - 1
            print(f'Accessing cube {oec.get_cube_names()[cube_number]}') 
            level = input("Enter the level: ")
            member = oec.get_cube_members(cube_number + 1, level)

            print(member)

        if int(option) == 5:
            filename = input("\tEnter the filename: ")
            dataset = oec.get_cube_data()
            dataset.to_csv(f'data/{filename}.csv')

        if int(option) == 6:
            cube_number = input('Enter the cube number: ')
            cube_number = int(cube_number) - 1
            columns = oec.get_cube_columns(cube_number)
            print_dic(columns)

        if int(option) == 7:
            print("Thank You!")
            running = False

    return 
if __name__ == "__main__":
    main()
