import pandas as pd

from oec import OECClient

if __name__ == "__main__":
    oec_client = OECClient()
    COLUMNS = 'Exporter Continent Official,Exporter Country Official,Importer Continent Official,Importer Country Official,Section,HS2,HS4,HS6,Year' 
    MEASURES = 'Trade+Value,Quantity'

    #Getting all Africa to Africa trade data
    print("Getting all Africa to Africa trade data from 2022") 
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:af;Year:2022')
    oec_client.dataset_to_csv('africa_to_africa_trade_2022')

    #Getting all Africa to Asia trade data
    print("Getting all Africa to Asia trade data from 2022")
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:as;Year:2022')
    oec_client.dataset_to_csv('africa_to_asia_trade_2022')

    #Getting all Africa to Europe trade data
    print("Getting all Africa to Europe trade data from 2022")
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:eu;Year:2022')
    oec_client.dataset_to_csv('africa_to_europe_trade_2022')

    #Getting all Africa to North America trade data
    print("Getting all Africa to North America trade data from 2022")
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:na;Year:2022')
    oec_client.dataset_to_csv('africa_to_north_america_trade_2022')

    #Getting all Africa to South America trade data
    print("Getting all Africa to South America trade data from 2022")
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:sa;Year:2022')
    oec_client.dataset_to_csv('africa_to_south_america_trade_2022')

    #Getting all Africa to Oceania trade data
    print("Getting all Africa to Oceania trade data from 2022")
    oec_client.set_cube_data(35, COLUMNS, MEASURES, 'Exporter Continent Official:af;Importer Continent Official:oc;Year:2022')
    oec_client.dataset_to_csv('africa_to_oceania_trade_2022')


