import pandas as pd 
import csv 
import plotly.figure_factory as pf
import plotly.graph_objs as go 
import statistics

df=pd.read_csv("data.csv")
data = df['reading score'].to_list()

mean=sum(data)/len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

reading_score_first_std_deviation_start,reading_score_first_std_deviation_end = mean-std_deviation, mean+std_deviation
reading_score_second_std_deviation_start,reading_score_second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
reading_score_third_std_deviation_start,reading_score_third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig=pf.create_distplot([data],["reading scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y = [0,0.20], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x=[reading_score_first_std_deviation_start,reading_score_first_std_deviation_start], y = [0,0.20],mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[reading_score_first_std_deviation_end,reading_score_first_std_deviation_end], y = [0,0.20],mode="lines", name="Standard Deviation 1"))
fig.add_trace(go.Scatter(x=[reading_score_second_std_deviation_start,reading_score_second_std_deviation_start], y = [0,0.20],mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[reading_score_second_std_deviation_end,reading_score_second_std_deviation_end], y = [0,0.20],mode="lines", name="Standard Deviation 2"))
fig.add_trace(go.Scatter(x=[reading_score_third_std_deviation_start,reading_score_second_std_deviation_start], y = [0,0.20],mode="lines", name="Standard Deviation 3"))
fig.add_trace(go.Scatter(x=[reading_score_third_std_deviation_end,reading_score_second_std_deviation_end], y = [0,0.20],mode="lines", name="Standard Deviation 3"))
fig.show()

list_of_data_within_1_std_deviation =[result for result in data if result>reading_score_first_std_deviation_start and result < reading_score_first_std_deviation_end]
list_of_data_within_2_std_deviation =[result for result in data if result>reading_score_second_std_deviation_start and result < reading_score_second_std_deviation_end]
list_of_data_within_3_std_deviation =[result for result in data if result>reading_score_third_std_deviation_start and result < reading_score_third_std_deviation_end]

print("Mean of data is {}".format(mean))
print("Median of data is {}".format(median))
print('Mode of data is {}'.format(mode))
print("Standard deviation of data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(data)))