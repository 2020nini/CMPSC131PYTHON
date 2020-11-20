# Author: Wenrui Zhang wkz5094@psu.edu
# Collaborator: Ruilan Sun rfs5748@psu.edu
# Collaborator: Prajnay Kataria pmk5429@psu.edu
# Collaborator: Shiao Zhuang sqz5328@psu.edu
# Section: 1
# Breakout: 5

import csv
from sys import argv
import pickle
def run():
  """
  This program should be run with the following command line arguments:

  python3 lab12.py input.pickle output.csv
  
  input.pickle file will be a binary file that contains pickle-dump'ed 
  data of a python list of dictionaries. Each dictionary will share
  the same key and corresponds to the csv file's header row. And each
  dictionary corresponds to a row in the csv file.

  Your program shall read in the data from input.pickle file; and then
  write to the output csv file including the header row.
  """
  if len(argv) < 3:
    print(f"Usage: python3 {argv[0]} input.pickle output.csv")
    return
  f=open(argv[1],'rb')
  ori=pickle.loaf(f)
  with open(argv[2], 'w') as f:
    temp_dict = ori[0]
    w = csv.Dictwriter(f, temp_dict.keys())
    w.writeheader()
    for dict in ori:
      w.writerow(dict)
if __name__ == "__main__":
  run()
