import pandas as pd
from oec import OECClient
"""
This script gets all of the Economics Indicators available on the OECD API
"""
if __name__ == "__main__":
    oec_client = OECClient()

    indicator_dict = oec_client.get_cube_members(25, "Indicator")['members']

    indicator_df = pd.DataFrame(indicator_dict)

    indicator_df = indicator_df.rename(columns = {
        'key': 'Indicator',
        'caption': 'Description'
    })

    indicator_df.to_csv("data/neocolonialism/indicators.csv") 