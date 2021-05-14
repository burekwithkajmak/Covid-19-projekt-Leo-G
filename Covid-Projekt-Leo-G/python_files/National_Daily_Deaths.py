#Importerar moduler för senare användning
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


#Läser in en csv fil med hjälp av pandas
df = pd.read_csv('csv_files/National_Daily_Deaths.csv')


#Funktion för att skapa diagram som har inparametrarna x = x-värdet, y = y-värdet, n = hur ofta på datumet i x-axeln, xlabel = namn på x-axeln, ylabel = namn på y-axeln, title = Titeln
def CreateDiagram(x,y,n,xlabel,ylabel,title):
    #Skapar en variabel för att x-axeln ska se bra ut och inte visa alla datum utan istället exempelvis varje 15 dag
    x_ticks = np.arange(0, len(df), n)
    #Sätter xticksen med en rotation för att det ska synas bättre
    plt.xticks(x_ticks, rotation = 45)
    #Plottar grafen
    plt.plot(x,y)
    #Lägger till en titel för x-axeln
    plt.xlabel(xlabel)
    #Lägger till en titel för y-axeln
    plt.ylabel(ylabel)
    #Lägger till en titel för hela grafen
    plt.title(title)
    #Lägger till ett rutnät
    plt.grid()

#Skapar ett diagram med hjälp av funktionen över
CreateDiagram(df["Date"],df["National_Daily_Deaths"],15,"Datum","Antal döda av covid-19 per dag","Covid-19 - antal döda per dag")

#Visar allt
plt.show()

