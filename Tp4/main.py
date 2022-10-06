import pandas as pd
import csv
data = pd.read_csv("LondonAir_Ozone.csv")
count = count25 = count50 = count75 = count100 = count_plus = countdiff =0
valsupp = []
testeur = 0
sites = data["Site"].unique()

'''remplacement des valeurs manquante par des ?'''

for i, ligne in  enumerate(data.iterrows()):

    if ( pd.isnull(data["Value"][i]) ):
        data["Value"][i] = "?"

    if ( data["Value"][i] != "?" ):
        countdiff += 1
        #print(float(data["Value"][i]))
        if ( float(data["Value"][i])< 0 ):
            count += 1
        elif ( float(data["Value"][i])< 25 ):
            count25 += 1
        elif(float(data["Value"][i])<50):
            count50 += 1
        elif(float(data["Value"][i])<75):
            count75 += 1
        elif(float(data["Value"][i])<100):
            count100 += 1
        elif(float(data["Value"][i])>99):
            count_plus += 1

# affichage nombre valeur
f = open('AIGLE_TP4_1.csv', 'w')
entetes = ["inf à 0", "inf à 25", "inf à 50", "inf à 75", "inf à 100","sup à 99"]
ligneEntete = ",".join(entetes) + "\n"
f.write(ligneEntete)
ligne = str(count) +"," + str(count25) +"," + str(count50) +"," + str(count75) +"," + str(count100) +"," + str(count_plus) + "\n"
f.write(ligne)
f.close()



new = dict(tuple(data.groupby("Site")))
f = open('Site.csv', 'w')
entetes = ["Site","inf à 0", "inf à 25", "inf à 50", "inf à 75", "inf à 100","sup à 99"]
ligneEntete = ",".join(entetes) + "\n"
f.write(ligneEntete)
''' recherche distribution par lieu '''

for site in sites:
    df = data.loc[(data["Site"] == site) & (data["Value"] != "?")]
    print("taille ",site," : ",len(df))
    nbinf0 = len(df.loc[df["Value"] < 0])
    nbinf25 = len(df.loc[(df["Value"] < 25) & (df["Value"] > 0)])
    nbinf50 = len(df.loc[(df["Value"] < 50) & (df["Value"] > 24)])
    nbinf75 = len(df.loc[(df["Value"] < 75) & (df["Value"] > 49)])
    nbinf100 = len(df.loc[(df["Value"] < 100) & (df["Value"] > 74)])
    nbsup = len(df.loc[df["Value"] > 99])
    print(str(nbinf0) +"," + str(nbinf25) +"," + str(nbinf50) +"," + str(nbinf75) +"," +str(nbinf100) +"," + str(nbsup))
    ligne = site + "," + str(nbinf0) +"," + str(nbinf25) +"," + str(nbinf50) +"," + str(nbinf75) +"," +str(nbinf100) +"," + str(nbsup) + "\n"
    f.write(ligne)
f.close()

with open('AIGLE_TP4_1.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

tailledeb = len(data)
print("taille de la data : ",len(data))

for i in range(len(data)):
    if str(data["Value"][i]) != '?':
        val = float(data["Value"][i])
        if val > 74 or val < 0:
            valsupp.append(i)

for j  in range(len(valsupp)) :
    data["Value"][j] = "?"
print("taille de la data : ",len(data))
print( "Nombre de valeur supprimé : ", tailledeb-len(data))

data.to_csv("AIGLE_tp4.csv", index=False)

''' transformation Mesure '''
tailleboucle = len(data)/len(sites)
print(tailleboucle)
f = open('AIGLE_TP4_2.csv', 'w')
entetes = ["Date"]
for site in sites :
    entetes.append(site)
#print(entetes)
ligneEntete = ",".join(entetes) + "\n"
f.write(ligneEntete)
for i in range(0,int(tailleboucle)-1):
    ligne =  str(data["ReadingDateTime"][i]) + "," + str(data["Value"][i]) + "," + str(data["Value"][i+(35040)]) +"," + str(data["Value"][i+(35040*2)]) +"," + str(data["Value"][i+(35040*3)]) +"," + str(data["Value"][i+(35040*4)])   + "\n"
    f.write(ligne)