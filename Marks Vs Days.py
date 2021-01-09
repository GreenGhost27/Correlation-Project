import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="Days Present", y="Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Marks = []
    Days = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Days.append(float(row["Days Present"]))
    return{"x": Marks, "y":Days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("The correlation of this graph is:", correlation[1,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()