import pandas as pd

from oec import OECClient

def continental_trade(oec_client, exporter_continent, importer_continent, year):
    """
    This function gets a CSV that includes trade data based on exporter continent and importer continent. It utilizes the  
    """
    COLUMNS = 'Exporter Continent Official,Exporter Country Official,Importer Continent Official,Importer Country Official,Section,HS2,HS4,HS6,Year' 
    MEASURES = 'Trade+Value,Quantity'

    cube_name = oec_client.get_cube_names()[35]
    print("Getting data from Cube: ", cube_name)

    #Mapping the natural language Continent Name to Continent Ky
    continents_raw = oec_client.get_cube_members(35, 'Exporter Continent')['members']
    CONTINENT_MAP = {continent['caption']: continent['key'] for continent in continents_raw}
    exporter_continent_key = CONTINENT_MAP[exporter_continent]
    importer_continent_key = CONTINENT_MAP[importer_continent]


    #Changing Continent name like North America -> north_america, Africa -> africa
    print(f'Getting all exports from {exporter_continent} to {importer_continent} from {year}')

    if len(exporter_continent.split()) == 2:
        exporter_continent = '_'.join(exporter_continent.split()).lower()
    else:
        exporter_continent = exporter_continent.lower()

    if len(importer_continent.split()) == 2:
        importer_continent = '_'.join(importer_continent.split()).lower()
    else:
        importer_continent = importer_continent.lower()

    #Getting the data
    oec_client.set_cube_data(35, COLUMNS, MEASURES, f'Exporter Continent Official:{exporter_continent_key};Importer Continent Official:{importer_continent_key};Year:{year}', properties = 'Exporter Country trade blocs,Exporter Country image link,Importer Country trade blocs,Importer Country image link')
    df = oec_client.dataset_to_df()
    print(df.head(20))
    df.to_csv(f'data/{exporter_continent.lower()}/{exporter_continent.lower()}_to_{importer_continent.lower()}_{year}.csv') 

    return

if __name__ == "__main__":
    oec_client = OECClient()
    continental_trade(oec_client, 'Africa', 'Africa', 2022)
    continental_trade(oec_client, 'Africa', 'Asia', 2022)
    continental_trade(oec_client, 'Africa', 'Europe', 2022)
    continental_trade(oec_client, 'Africa', 'North America', 2022)
    continental_trade(oec_client, 'Africa', 'South America', 2022)
    continental_trade(oec_client, 'Africa', 'Oceania', 2022)