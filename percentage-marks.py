import plotly.express as px
import csv 
import numpy as np

def getDataSource(data_path):
    day_present = []
    marks = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            day_present.append(float(row["Days"]))
            marks.append(float(row["Marks"]))
    return {"x":day_present, "y":marks}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation between marks vs days present: \n--->",correlation[0,1])
        



def setup():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setup()