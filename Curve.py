import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("C:/Users/Asus/Desktop/whj/project 108/Amazon.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Name"], show_hist=True)
fig.show()