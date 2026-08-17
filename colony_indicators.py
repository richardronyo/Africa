from oec import OECClient

if __name__ == "__main__":
    oec_client = OECClient()

    oec_client.set_cube_data(
        25, 
        'Country Official,Indicator,Year',
        'Measure',
        include = 'Country Official:fra,dza,mar,tun,sen,mli,gin,civ,ner,bfa,ben,mrt,tgo,cmr,tcd,caf,gab,cog,dji,mdg,com;Indicator:NY.GDP.MKTP.CD,NY.GDP.PCAP.CD,SP.POP.TOTL,TT.PRI.MRCH.XD.WD,TX.VAL.MANF.ZS.UN,TM.VAL.MANF.ZS.UN,TX.VAL.AGRI.ZS.UN,TX.VAL.MMTL.ZS.UN,TX.VAL.FUEL.ZS.UN,TX.VAL.TECH.MF.ZS,TX.VAL.MRCH.HI.ZS,DC.DAC.FRAL.CD,DT.ODA.ODAT.CD,GC.TAX.INTT.RV.ZS,TM.TAX.MRCH.WM.AR.ZS;Year:1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024'
    )

    indicators = oec_client.dataset_to_df()

    indicators.to_csv("data/neocolonialism/indicator_values.csv")
