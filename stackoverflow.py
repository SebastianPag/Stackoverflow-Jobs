import urllib.request
import re

#File to write data to later on
file = open("stackoverflow.txt", "a")


#Get URL and create handle, the provided url will go through all job offers.
#Just copy paste the Url for whatever Searchfilter and you should be good to go
url = input("Enter Url:")
if len(url) < 1: url = "https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab"
fhand = urllib.request.urlopen(url)

#List to store skills & page count
skl = list()
page = 0

#Enter date to store in file and number of pages to iterate
date = str(input("Enter date: "))
pages = int(input("Number of pages: "))


###Crawling all pages with job-offers###
while page <= pages:
	for line in fhand:
		clean = line.decode().strip()
		
		#skip the part of the website before the job-offers
		if not clean.startswith('<a href="/jobs/developer-jobs-using-'): continue
		
		#find all tags which where used to determine which skills are sought after most
		skl.extend(re.findall(">(\S+)?</a>", clean))
	
	#Keep track & update URL
	if page%10 == 0:print(page)
	page += 1
	url = "https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab"+"&pg="+str(page)
	fhand = urllib.request.urlopen(url)


#dictionary to store skill and count	
times = dict()

#some data cleaning
for skill in skl:
	if skill == "angular": skill = "angularjs"
	if skill == "html": skill = "html5"
	if skill == "react": skill = "reactjs"
	if skill == "c++11": skill = "c++"
	if skill == "c++14": skill = "c++"
	if skill == "mysql": skill = "sql"
	if skill == "css3": skill = "css"
	if skill == "node": skill = "node.js"
	times[skill] = times.get(skill, 0) + 1


#sorting	
valu = list()
for val, key in times.items():
 	valu.append((key, val))
i = 0
valu.sort(reverse = True)

#write to file. To get more items of the list just change the if-statement
file.write(date +"\n" + "Number of jobs: " + str(pages*25) + "\n")
for val in valu:
	i += 1
	file.write(str(val[0]) + "\t\t\t\t" + str(val[1]) + "\n" )
	if i == 40: break
file.write("\n\n\n")	
file.close()
