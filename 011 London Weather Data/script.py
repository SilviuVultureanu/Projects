import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.columns)
print(london_data.head(40000))

temp=london_data['TemperatureC']
average_temp = round(np.mean(temp),2)
temperature_var = round(np.var(temp),2)
print(average_temp)
print(temperature_var)

temperature_standard_deviation = round(np.std(temp),2)
print('London StDev: ', temperature_standard_deviation)

june = london_data.loc[london_data['month']==6]['TemperatureC']
july = london_data.loc[london_data['month']==7]['TemperatureC']
june_mean = np.mean(june)
june_StDev = np.std(june)
july_mean = np.mean(july)
july_StDev = np.std(july)

print('June mean:', round(june_mean,2))
print('June StDev:', round(june_StDev,2))
print('July mean:', round(july_mean,2))
print('July StDev:', round(july_StDev,2))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

