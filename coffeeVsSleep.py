import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Coffee in ml", y="sleep in hours")
        fig.show()

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))
    return{"x": Coffee, "y":Sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The correlation of this graph is:", correlation[-1,1])

def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()