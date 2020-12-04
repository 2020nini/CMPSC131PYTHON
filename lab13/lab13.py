# Author: Wenrui Zhang wkz5094@psu.edu
# Collaborator: Ruilan Sun rfs5748@psu.edu
# Collaborator: Prajnay Kataria pmk5429@psu.edu
# Collaborator: Shiao Zhuang sqz5328@psu.edu
# Section: 1
# Breakout: 5

from matplotlib import pyplot as plt
from sys import argv
import csv
# Retrieve a list of counties from argv[2]
counties =list(argv[2].split())

# Retrieve the number of days from argv[3]
days = int(argv[3])

plt.xticks(rotation=70, fontsize=6)
plt.ylabel('7-day Average New Cases per 100,000 population')
# Write code to read csv file (argv[1]) into a list of dictionaries
with open (argv[1],newline='') as ori_sample:
  ori_sample=list(csv.DictReader(ori_sample, dialect='excel'))
  

#print(ori_sample)
def get_date(days):
  date_data=[]
  for date in ori_sample:
    date_data.append(date['Date'])
  return date_data

dates=get_date(days)
def get_county(county):
  right_jur=[]
  county_data=[]
  mid=[]
  if days>30:
    mid=list(dates[-days::7])
  else:
    mid=list(dates[-days:])
  #print(mid)
  for temp in ori_sample:
    if temp['Jurisdiction']==county:
      right_jur.append(temp)
  for element in right_jur:
    if element['Date'] in mid:
      temp=float(element['7-Day Average New Case Rate'])
    #print(temp)
      county_data.append(temp)
  #print(county_data)
  return county_data
#get_county('Centre')
def get_county_2(days):
  right_jur=[]
  county_data=[]
  for temp in ori_sample:
    if temp['Jurisdiction']==county:
      right_jur.append(temp)
  for element in right_jur:
    if element['7-Day Average New Case Rate']!='':
      temp=float(element['7-Day Average New Case Rate'])
    else:
      temp=0.0
    #print(temp)
    county_data.append(temp)
  #print(county_data)
  return county_data

for county in counties: 
  # Retrieve from the csv file's data x/y data for a specific county 
  # The length of the data should match the number of days from argv[3]
  # It should be data for the most recent days. 
  county_ys=get_county(county)
  
  if days > 30:
    plt.plot(get_county_2(days)[-days::1], label = county)
    plt.xticks(range(0,days,7),dates[-days::7])
  else:
    plt.plot(county_ys, label = county)
    plt.xticks(range(days), dates[-days:])


plt.legend()
# Save figure to the file argv[4]
plt.savefig(argv[4])
plt.show()