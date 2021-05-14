#Importerar moduler för senare användning
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Läser in en csv fil med hjälp av pandas
df = pd.read_csv('csv_files/Regional_Totals_Data.csv')

#Skapar en fig och en subplot med två rader och två columner och titlar
fig = make_subplots(rows=2, cols=2, subplot_titles=("Totala fall", "Fall per 100k", "Totala intensivvård", "Totala dödsfall"))

#Lägger diagram till subplotten med olika x och y värden men även definar vilken rad och column de ska vara på
fig.add_trace(go.Scatter(name="Totala fall", x=df["Region"].values, y=df["Total_Cases"].values), row=1, col=1)
fig.add_trace(go.Scatter(name="Fall per 100k", x=df["Region"].values, y=df["Cases_per_100k_Pop"].values), row=1, col=2)
fig.add_trace(go.Scatter(name="Totala intensivvård",x=df["Region"].values, y=df["Total_ICU_Admissions"].values), row=2, col=1)
fig.add_trace(go.Scatter(name="Totala dödsfall",x=df["Region"].values, y=df["Total_Deaths"].values), row=2, col=2)

#Visar figuren
fig.show()


