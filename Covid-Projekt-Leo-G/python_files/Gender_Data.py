#Importerar moduler för senare användning
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


#Läser in en csv fil med hjälp av pandas
df = pd.read_csv('csv_files/Gender_Data.csv')

#Definar listor som har värderna för olika typer av data
value_cases = df["Total_Cases"].values
value_icus = df["Total_ICU_Admissions"].values
value_deaths = df["Total_Deaths"].values

#Definar en lista för titlarna för cirkeldiagramen
labels = ["Män", "Kvinnor"]

#Funktion för att skapa cirkeldiagram som har inparametrarna values = värderna, row = rad, column = vilken column i subplotten, place = plats i subplotten, title = titel, shadow = Skugga eller inte.
def CreatePieChartDiagram(values,row,column,place,title,shadow):
    #Skapar en subplot
    plt.subplot(row, column, place)
    #Skapar en pie chart
    plt.pie(values, labels=labels, autopct='%1.2f%%', shadow=shadow)
    #Lägger till en title
    plt.title(title)
    #Lägger till en legend
    plt.legend()

#Skapar diagram med hjälp av funktionen över
CreatePieChartDiagram(value_cases, 2, 3, 1,"Antal fall/kön", True)
CreatePieChartDiagram(value_icus, 2, 3, 2,"Antal intensivvård/kön", True)
CreatePieChartDiagram(value_deaths, 2, 3, 3,"Antal dödsfall/kön", True)

#Visar hela
plt.show()

