#Importerar moduler för senare användning
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

#Läser in en csv fil med hjälp av pandas
df = pd.read_csv('csv_files/National_Total_Deaths_by_Age_Group.csv')

#Definar listor för olika typer av värden
labels = df["Age_Group"].values
y_cases = df["Total_Cases"].values
y_icus = df["Total_ICU_Admissions"].values
y_deaths = df["Total_Deaths"].values


#Funktion för att skapa diagrammen som har inparametrarna x = x-värdet, y = y-värdet, row = rad för subploten, place = plats för grafen i subploten, column = vilka column den ligger på, title = titel på grafen
def CreateBarChart(x,y,row,place,column,title):
    #Skapar subplot
    plt.subplot(row, place, column)
    #Plottar grafen 
    plt.bar(x, y)
    #Sätter titeln
    plt.title(title)
    #Här loopar jag två saker samtidigt för att kunna visa värden över varje graf så det blir tydligare.
    for a,b in zip(labels, y): 
        #Lägger till texten över barsen
        plt.text(a, b, str(b), ha="center", fontsize=9)
    
#Här skapar jag diagrammen med hjälp av funktionen som jag skapade innan
CreateBarChart(labels,y_cases, 2, 2, 1, "Antal covid-19 fall per åldersgrupp")
CreateBarChart(labels,y_icus,2, 2, 2, "Antal intensivvård fall per åldersgrupp")
CreateBarChart(labels,y_deaths,2, 2, 3, "Antal dödsfall per åldersgrupp")

#Här visar jag allt.
plt.show()
