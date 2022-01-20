import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    sleep = []
    coffee = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            sleep.append(float(row["sleep"]))
            coffee.append(float(row["Coffee"]))
    return {"x":sleep, "y":coffee}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between coffee vs sleep: \n--->",correlation[0,1])
        



def setup():
    data_path = "cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()