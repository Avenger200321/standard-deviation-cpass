import csv 
import pandas as pd
import plotly.express as px
with open('class1.csv', newline='') as f:
    read = csv.reader(f)
    data = list(read)
data.pop(0)
totalMarks = 0 
n = len(data)
for i in data :
    totalMarks = totalMarks + float(i[1]) 
mean = totalMarks/n
print(mean)
df = pd.read_csv('class1.csv')
graph = px.scatter(df, x= 'Student Number', y= 'Marks' )
graph.update_layout(shapes=[
    dict(
        type = 'line', 
        y0 = mean,
        y1 = mean,
        x0 = 0,
        x1 = n
    )
])
graph.update_yaxes(rangemode = 'tozero')
graph.show()