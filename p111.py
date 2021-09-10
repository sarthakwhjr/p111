import csv
import pandas as pd
import plotly.graph_objects as pgo
import plotly.figure_factory as pff
import random
import statistics
df=pd.read_csv("c111/mathdata.csv")
data=df["Math_score"].tolist()
def randomdata(counter):
    dataset=[]
    for i in range(0,counter):
        randomdata=random.randint(0,len(data)-1)
        value=data[randomdata]
        dataset.append(value)
    mean=statistics.mean(dataset) 
    return mean
meanlist=[] 
for i in range(0,1000):
    allmean=randomdata(100)
    meanlist.append(allmean)
stdev=statistics.stdev(meanlist)
mean2=statistics.mean(meanlist)
print("mean = ",mean2)
print("stdev = ",stdev)
'''
graph=pff.create_distplot([meanlist],["avg score"],show_hist=False)
graph.add_trace(pgo.Scatter(x=[mean2,mean2],y=[0,0.20],mode="lines",name="name"))
graph.show()'''
 
first_std_deviation_start, first_std_deviation_end = mean2-stdev, mean2+stdev
second_std_deviation_start, second_std_deviation_end = mean2-(2*stdev), mean2+(2*stdev)
third_std_deviation_start, third_std_deviation_end = mean2-(3*stdev), mean2+(3*stdev)
 
df = pd.read_csv("c111/ipad.csv")
data = df["Math_score"].tolist()
mean_of_sample1 = statistics.mean(data)
print("Mean of sample1:- ",mean_of_sample1)
fig = pff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[mean_of_sample1, mean_of_sample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(pgo.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(pgo.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


df = pd.read_csv("c111/extraclass.csv")
data = df["Math_score"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of sample2:- ",mean_of_sample1)
fig = pff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="extraclass"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(pgo.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(pgo.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


df = pd.read_csv("c111/funsheet.csv")
data = df["Math_score"].tolist()
mean_of_sample3 = statistics.mean(data)
print("Mean of sample3:- ",mean_of_sample1)
fig = pff.create_distplot([meanlist], ["student marks"], show_hist=False)
fig.add_trace(pgo.Scatter(x=[mean2, mean2], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(pgo.Scatter(x=[mean_of_sample3, mean_of_sample3], y=[0, 0.17], mode="lines", name="funsheet"))
fig.add_trace(pgo.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(pgo.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(pgo.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()


