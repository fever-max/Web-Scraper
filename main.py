from extractors.indeed import extract_indeed_jobs
from extractors.wwr import exfract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = exfract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
  print(job)
  print("\n")
