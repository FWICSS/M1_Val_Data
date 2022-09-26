import csv
import pandas
df = pandas.read_csv("PSRA.csv")
with open('PSRA.csv', newline='') as csvfile:
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
                        #print("Nombre de valeurs manquantes : " , nbVal)
                        if (nbVal < 15):
                            PrevTrou = int(row['No']) - int(nbVal+1)
                            PrevTrouData = df.loc[(df['No'] == PrevTrou)]
                            ValPrev = int(PrevTrouData['pm2.5'])
                            ValSuiv = int(row['pm2.5'])
                            #print("Début du trou "+ str(PrevTrou+1) + ": \n" +"Précédent : " + str(PrevTrou) +
                                  #" valeur : "+ str(ValPrev)+ "\n" + "Suivant : " + row['No'] + " valeur : "+ str(ValSuiv))
                            i = abs(ValSuiv-ValPrev)/nbVal+1
                            valI.append(i)
                            #print("valeur de i : " + str(i))
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
    print(" Trou  | Debut | Fin | ValM | Coeff")
    for i in range(len(valI)) :
        if (i < 9):
            print(" ",i+1,"   |",DebTrou[i]," |",FinTrou[i]," |",NbValManquante[i]," |",valI[i])
        elif (i > 8 & i < 99):
            print(" ", i + 1, "  |", DebTrou[i], " |", FinTrou[i], " |", NbValManquante[i], " |", valI[i])
        else :
            print(" ", i + 1, "|", DebTrou[i], " |", FinTrou[i], " |", NbValManquante[i], " |", valI[i])