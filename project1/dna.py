#Author：Wenrui Zhang wkz5094@psu.edu
from sys import argv
import csv
import time


def match_seq(seq, crime):
  for s in crime:
    if s == 'CrimeID':
      continue
    if (s*int(crime[s]) not in seq) or (s*(int(crime[s])+1) in seq):
      return False
  return True


def run():
  suspects = {}
  crimes = {}
  result = {}

  # with open('crime.csv','r') as f:
  with open(argv[1],'r') as f:
    crimes = list(csv.DictReader(f))

  # with open('suspect.csv','r') as f:
  with open(argv[2], 'r') as f:
    suspects = list(csv.DictReader(f))



  for s in suspects:
    for c in crimes:
      if s['Suspect'] not in result:
        result[s['Suspect']] = []
      if match_seq(s['Sequence'], c):
        result[s['Suspect']].append(c['CrimeID'])

  result = [[r,','.join(result[r])] for r in result]


  # with open('res.csv', 'w', newline='') as f:
  with open(argv[3], 'w', newline='') as f:
    r=csv.writer(f)
    r.writerow(['Suspect', 'Crimes'])
    r.writerows(result)

  return

if __name__ == "__main__":
  start = time.perf_counter()
  run()
  end = time.perf_counter()
  print(f"Time used: {end-start} seconds")