from oec import OECClient

def country_trade(oec_client, country_name):
    """
    This function gets all of the exports from a specific country from 2019 - 2022 
    """

    COLUMNS = "Exporter Country Official,Importer Country Official,Section,HS2,HS4,HS6,Year"
    MEASURES = "Trade+Value,Quantity"

    cube_name = oec_client.get_cube_names()[61]
    print("Getting data from:", cube_name)

    #Mapping the natural languag Country Name to Country Key
    country_raw = oec_client.get_cube_members(62, 'Exporter Country Official')['members']
    COUNTRY_MAP = {country['caption']: country['key'] for country in country_raw}
    country_key = COUNTRY_MAP[country_name]

    #Getting all the exports from the requested country from 2019 - 2022
    print(f'Getting all exports from {country_name}')

    oec_client.set_cube_data(62, COLUMNS, MEASURES, f'Exporter Country Official:{country_key}', properties = 'Exporter Country trade blocs')
    df = oec_client.dataset_to_df()
    print(df.head(20))
    df.to_csv(f'data/neocolonialism/{country_name}.csv')

if __name__ == "__main__":
    french_colonies = []
    with open("data/france_colonies.txt") as f:
        for line in f:
            french_colonies.append(line.strip())

    oec_client = OECClient()

    for country in french_colonies:
        country_trade(oec_client, country)