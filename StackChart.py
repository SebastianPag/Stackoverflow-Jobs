import matplotlib.pyplot as plt
import pandas as pd
import re

####Plotting####
file = open("stackoverflow.txt", "r")


listoflists = []

#prep for plotting, 
for line in file:
	if re.search("^[0-9]+\s+", line):
		listoflists.extend([re.findall("\S+", line)])

numberList = [int(x[0]) for x in listoflists]
nameList = [x[1] for x in listoflists]

pdSeries = pd.Series(numberList, index=nameList)

ax = pdSeries[:30].plot.bar()
fig = ax.get_figure()
fig.savefig("17.04.18.png")


file.close()
            