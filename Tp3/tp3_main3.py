import pandas
df = pandas.read_csv("AIGLE_tp3_1.csv")

df["pm2.5_3"] = ['?'] * len(df)
df["pm2.5_4"] = ['?'] * len(df)
df["pm2.5_5"] = ['?'] * len(df)


for i, ligne in  enumerate(df.iterrows()):
        if(int(df["No"][i])>29):
                df["pm2.5_3"][i] = df["pm2.5"][i-3]
                df["pm2.5_4"][i] = df["pm2.5"][i-4]
                df["pm2.5_5"][i] = df["pm2.5"][i-5]
df = df.drop(range(0,5))

df.to_csv("AIGLE_tp3_2c.csv", index=False)



