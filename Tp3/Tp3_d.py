import pandas
df = pandas.read_csv("AIGLE_tp3_2c.csv")
#Suprression de toute les colones sauf les pm2.5
df = df.drop(columns=["No","year","month","day","hour","DEWP","TEMP","PRES","cbwd","Iws","Is","Ir"])

df.to_csv("AIGLE_tp3_2d.csv", index=False)