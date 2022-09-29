import csv
import pandas
df = pandas.read_csv("AIGLE_tp3_1.csv")
f = open('AIGLE_tp2_2d.csv', 'w')
entetes = ["pm2.5", "pm2.5_3", "pm2.5_4", "pm2.5_5"]
ligneEntete = ",".join(entetes) + "\n"
f.write(ligneEntete)
with open('AIGLE_tp3_1.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
            if(int(row["No"])>30 ):
                pm_3 = df.loc[df["No"] == (int(row["No"]) - 3)]
                pm_4 = df.loc[df["No"] == (int(row["No"]) - 4)]
                pm_5 = df.loc[df["No"] == (int(row["No"]) - 5)]
                ligne = ""
                if ("?" in str(row["pm2.5"])):
                    ligne += "?,"
                else:
                    ligne += str(float(row["pm2.5"])) + ","

                if("?" in str(pm_3["pm2.5"])):
                    ligne += "?,"
                else :
                    ligne += str(float(pm_3["pm2.5"])) + ","

                if("?" in str(pm_4["pm2.5"])):
                    ligne += "?,"
                else :
                    ligne += str(float(pm_4["pm2.5"])) + ","

                if("?" in str(pm_5["pm2.5"])):
                    ligne += "?,"
                else :
                    ligne += str(float(pm_5["pm2.5"])) + ","
                ligne += "\n"
                f.write(ligne)

f.close()



