from App_Motion_Detector import df
from bokeh.plotting import show, output_file, figure
import pandas


p = figure(x_axis_type='datetime', height=300,
           width=1000, title="Motion Graph")

graph = p.quad(left=df["Start"], right=df["End"],
               bottom=0, top=1, color="green")

output_file("Graph.html")
show(p)
