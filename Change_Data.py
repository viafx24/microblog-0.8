from app import db
from app.models import User, Citation
import pickle
import pandas as pd

with open('Data','rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        Data=mon_depickler.load()




#Data[300].Historique.reset_index(["Date"],inplace=True)

#A=Data[300].Historique["Date"].astype('int64')//1e9
#print(A)

#print(pd.to_datetime(A[1], unit='s'))

#Data[300].Historique.Timestamp=Data[300].Historique.Timestamp(Data[300].Historique["Date"][1])

#print(Data[300].Historique.Timestamp)


#users = User.query.all()
#for u in users:
#    db.session.delete(u)

#citations = Citation.query.all()

#for c in citations:
#    db.session.delete(c)

#db.session.commit()












u = User.query.get(1)

for i in range(1,len(Data)):

    citation = Citation(text=Data[i].text,SRR=Data[i].SRR,TRT=Data[i].TRT,author=u)
    db.session.add(citation)
    db.session.commit()


print(Citation.query.all())












#db.session.commit()

#citations = Citation.query.all()
#for i in citations:
#    db.session.delete(i)

#db.session.commit()

#print(Citation.query.all())

##import csv
#import pickle
#from citation import citation

#from datetime import date
#import pandas as pd
#import matplotlib.pyplot as plt

#with open('Data_Old','rb') as fichier:
#        mon_depickler = pickle.Unpickler(fichier)
#        Data_Old=mon_depickler.load()


## creation of the main list of citation
#Data=list()
#Emphasis="Normal"

#Date=date(2018,12,1)


#for i in range(0,len(Data_Old)):

#     HistListe=[[Date,Data_Old[i].SRR,Data_Old[i].TRT]]
#     Historique=pd.DataFrame(HistListe, columns=['Date','SRR','TRT'])
#     Historique["Date"]=pd.to_datetime(Historique["Date"])
#     Historique.set_index(["Date"],inplace=True)

#     Data.append(citation(Data_Old[i].number,Data_Old[i].text,Data_Old[i].SRR,Data_Old[i].TRT,Emphasis,Historique))

#with open('Data','wb') as fichier:
#    mon_pickler = pickle.Pickler(fichier)
#    mon_pickler.dump(Data)

##show the result
#print(Data)

#print(Data[1].Historique)

#plt.plot(Data[1].Historique["TRT"],Data[1].Historique["SRR"],marker="x")
#plt.show()

#for i in 
## import the data from the csv
#with open('Seneque_Pour_Couleur_2.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file,delimiter='\t')

#    for line in csv_reader:
#        Data.append(citation(line[0],line[1]))
#        # print(Data[i].text)
#        if i<101:
#            Data[i].SRR=2

#        if i<201 and i>100:
#            Data[i].SRR=1
       
#        if i<301 and i>200:
#            Data[i].SRR=0
       

#        i+=1

# chechinf for the place on the screen        
#Data[129].SRR=-1
#Data[119].SRR=-1
#Data[135].SRR=-1
#Data[197].SRR=-1
#Data[96].SRR=-1

# write on a file "Data"     
#with open('Data','wb') as fichier:
#    mon_pickler = pickle.Pickler(fichier)
#    mon_pickler.dump(Data)

##show the result
#print(Data)