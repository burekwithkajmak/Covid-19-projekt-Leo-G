#Importerar moduler för senare användning
import dash
import dash_core_components as dcc
from dash_core_components.Graph import Graph
import dash_html_components as html
from dash_html_components import Title
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

#App
app = dash.Dash(__name__)

#Läser in olika csv filer med hjälp av panda (olika datatyper)
df_regional = pd.read_csv('csv_files/Regional_Totals_Data.csv')
df_pie = pd.read_csv('csv_files/Gender_Data.csv')
df_deaths = pd.read_csv('csv_files/National_Daily_Deaths.csv')
df_age_group = pd.read_csv('csv_files/National_Total_Deaths_by_Age_Group.csv')
df_icus = pd.read_csv('csv_files/National_Daily_ICU_Admissions.csv')
#OBBS egengjord csv fil för att även få lat och lon kordinater för varje län
df_sweden_info = pd.read_csv('csv_files/coords.csv')


#Funktion för att skapa ett linje diagram som har många olika inparametrar för att man även ska kunna stylea diagrammet.
def CreateLineChart(df_file, x_value, y_value, title, plotColor, paperColor, fontColor, line_color):
    fig = px.line(df_file,x = x_value,y = y_value, title = title)
    fig.update_layout(
    plot_bgcolor=plotColor,
    paper_bgcolor=paperColor,
    font_color=fontColor
    )
    fig.update_traces(line_color=line_color)
    return fig

#Funktion för att skapa ett stapel diagram som har många olika inparametrar för att man även ska kunna stylea diagrammet.
def CreateBarChart(df_file, x_value, y_value, title, plotColor, paperColor, fontColor, text):
    fig = px.bar(df_file,x = x_value,y = y_value,title = title, text=text)
    fig.update_layout(
    plot_bgcolor=plotColor,
    paper_bgcolor=paperColor,
    font_color=fontColor
    )
    return fig

#Definar listor för senare användning
total_case = df_regional["Total_Cases"].sum()
total_deaths = df_regional["Total_Deaths"].sum()
total_icus = df_regional["Total_ICU_Admissions"].sum()

#HTML
app.layout = html.Div(children=[
    #Skapar en h1 div med en class som sedan används i cssen
    html.H1("Covid-19 - Översikt över fall", className="wrapper-header"),

    #Skapar en div med flera divs inuti
    html.Div([
        #Divs för att visa olika värden som exempelivs totala dödsfall osv med olika classer för att sedan kunna referera till cssen. 
        html.Div([
            html.P("Totala fall", className="wrapper-info-div-label"),
            html.P(total_case, className="wrapper-info-div-value cases"),
        ],className="wrapper-info-div"),

        html.Div([
            html.P("Totala intensivvårds fall", className="wrapper-info-div-label"),
            html.P(total_icus, className="wrapper-info-div-value icus"),
        ],className="wrapper-info-div"),

        html.Div([
            html.P("Totala dödsfall", className="wrapper-info-div-label"),
            html.P(total_deaths, className="wrapper-info-div-value deaths"),
        ],className="wrapper-info-div"),
    ],className="wrapper-info"),


    #Skapar en graph med ett id och även kör funktionen som skapades innan.
    dcc.Graph(
        id="wrapper-graph-line",
        figure= CreateLineChart(df_deaths, "Date", "National_Daily_Deaths", "Antal dödsfall/dag", "#546E7A", "#546E7A", "white" , "red")
    ),

    html.Div([
        html.Div([
            #Dropdownmeny
            dcc.Dropdown(
            #Id på elementet
            id='wrapper-line-dropdown',
            #Data man kan välja mellan
            options=[
                {'label': 'Totala fall/åldersgrupp', 'value': 'Total_Cases'},
                {'label': 'Totala intensivvård/åldersgrupp', 'value': 'Total_ICU_Admissions'},
                {'label': 'Totala dödsfall/åldersgrupp', 'value': 'Total_Deaths'}
            ],
            #Standard värdet 
            value="Total_Cases",
            ),
            dcc.Graph(id='wrapper-line-graph')
        ], className="wrapper-graph-bar"),

        html.Div([
            dcc.Dropdown(
            id='wrapper-bubble-dropdown',
            options=[
                {'label': 'Totala fall', 'value': 'Total_Cases'},
                {'label': 'Fall per 100k människor', 'value': 'Cases_per_100k_Pop'},
                {'label': 'Totala intensivvård', 'value': 'Total_ICU_Admissions'},
                {'label': 'Totala dödsfall', 'value': 'Total_Deaths'}
            ],
            #Standard värdet 
            value="Total_Cases",
            ),
            dcc.Graph(id='wrapper-bubble-graph')
        ], className="wrapper-graph-bubble"),

    ], className="wrapper-graphs-middle"),



    #En div som innehåller en graf och en dropdown för att interaktivt kunna välja vilken data man vill visualera i diagrammet. 
    html.Div([
        dcc.Graph(
            id='wrapper-graph-region',
            figure= CreateLineChart(df_icus, "Date", "National_Daily_ICU_Admissions", "Antal intensivvårds fall/dag", "#546E7A", "#546E7A", "white" , "orange")
        ),
        #En div som innehåller en dropdown menu
        html.Div([
            #Dropdownmeny
            dcc.Dropdown(
            #Id på elementet
            id='values', 
            #Standard värde på grafen
            value='Total_Cases', 
            #Data man kan välja mellan
            options=[
                {'label': 'Totala fall/kön', 'value': 'Total_Cases'},
                {'label': 'Totala intensivvård/kön', 'value': 'Total_ICU_Admissions'},
                {'label': 'Totala dödsfall/kön', 'value': 'Total_Deaths'}],
            ),
            dcc.Graph(id="wrapper-pie"),
        ],id="wrapper-graph-pie"),
    ],className="wrapper-graphs"),




])

#Callback för att grafen ska ändras beroende på vad man väljer i dropdown menyn
@app.callback(Output("wrapper-pie", "figure"), [Input("values", "value")],)

#Funktion för att skapa detta diagrammet genom callbacken
def CreateGenderPieChart(values):
    fig = px.pie(df_pie, values=values, names="Gender", hole=.7, title="Kön")
    fig.update_layout(
    plot_bgcolor="#546E7A",
    paper_bgcolor="#546E7A",
    font_color="white"
    )
    return fig

#Callback för att grafen ska ändras beroende på vad man väljer i dropdown menyn
@app.callback(
    dash.dependencies.Output('wrapper-line-graph', 'figure'),
    [dash.dependencies.Input('wrapper-line-dropdown', 'value')])

#Funktion för att skapa detta diagrammet genom callbacken
def CreateAgeGroupBarChart(value):
    fig = px.bar(df_age_group, x="Age_Group", y=value,title="Antal fall i olika åldersgrupper", text=value)
    fig.update_layout(
    plot_bgcolor="#546E7A",
    paper_bgcolor="#546E7A",
    font_color="white"
    )
    return fig

#Callback för att grafen ska ändras beroende på vad man väljer i dropdown menyn
@app.callback(
    dash.dependencies.Output('wrapper-bubble-graph', 'figure'),
    [dash.dependencies.Input('wrapper-bubble-dropdown', 'value')])

#Funktion för att skapa detta diagrammet genom callbacken
def CreateBubbleChart(value):
    #Skapar en egen dataframe för att kunna kombinera flera olika datatyper i en och samma dataframe.
    bubblemap = dict(region = df_regional["Region"], size = df_regional[value], lat = df_sweden_info["Lat"], lon = df_sweden_info["Lon"])
    df_bubblemap = pd.DataFrame(bubblemap)
    fig = px.scatter_geo(df_bubblemap, scope="europe", color="region", hover_name="region", size="size", lat="lat", lon="lon", fitbounds="locations", title = f"Antal {value}/län")
    fig.update_geos(
        showocean=True,  oceancolor="LightBlue",
    )
    return fig

#Här körs allt.
if __name__ == '__main__':
    app.run_server(debug=True)