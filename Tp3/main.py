import csv
import pandas
df = pandas.read_csv("PRSA.csv")
with open('PRSA.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    trou  = False
    nbVal = 0
    ListTrou = []
    NbValManquante =[]
    valI = []
    DebTrou = []
    FinTrou = []
    for row in reader :
                if(row['pm2.5'] == 'NA'):
                    nbVal+=1
                else :
                    if (nbVal > 0):
                        NbValManquante.append(nbVal)
                        if (nbVal < 15):
                            PrevTrou = int(row['No']) - int(nbVal+1)
                            PrevTrouData = df.loc[(df['No'] == PrevTrou)]
                            ValPrev = int(PrevTrouData['pm2.5'])
                            ValSuiv = int(row['pm2.5'])
                            i = abs(ValSuiv-ValPrev)/nbVal+1
                            valI.append(i)
                        else :
                            valI.append(0)

                    nbVal=0
                if (row['pm2.5'] == 'NA' and trou == False):
                    DebTrou.append(int(row['No']))
                    trou = True
                elif  (row['pm2.5'] !='NA' and trou == True):
                    a = int(row['No'])-1
                    FinTrou.append(a)
                    trou = False
    print(" Trou  | Debut | Fin | ValM | Incrément")
    for i in range(len(valI)) :
        if (i < 9):
            print(" ",i+1,"   |",DebTrou[i]," |",FinTrou[i]," |",NbValManquante[i]," |",valI[i])
        elif (i > 8 & i < 99):
            print(" ", i + 1, "  |", DebTrou[i], " |", FinTrou[i], " |", NbValManquante[i], " |", valI[i])
        else :
            print(" ", i + 1, "|", DebTrou[i], " |", FinTrou[i], " |", NbValManquante[i], " |", valI[i])
    for inc in range(len(valI)) :
        if (NbValManquante[inc]>15):
            testeur = 0
            for j in range(NbValManquante[inc]):
                df.loc[df["No"] == DebTrou[inc]+j , "pm2.5"] = "?"
        else:
            for j in range(NbValManquante[inc]):
                #print(valI[inc]*j+1)
                df.loc[df["No"] == DebTrou[inc] + j, "pm2.5"] = valI[inc]*j+1
    df.to_csv("tp2_1.csv", index=False)
    print("Save on file tp2_1.csv")
    nbNA = 0
    with open('tp2_1.csv', newline='') as tpfile:
        tpReader = csv.DictReader(tpfile)
        for row in tpReader:
            print(nbNA)
            if (row['pm2.5'] == 'NA'):
                nbNA += 1


    if(nbNA == 0):
        print("plus aucune trou de plus de 15 valeurs")
    else:
        print("il existe des trou toujours")