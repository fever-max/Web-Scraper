from extractors.indeed import extract_indeed_jobs
from extractors.wwr import exfract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = exfract_wwr_jobs(keyword)
jobs = indeed + wwr


file = open(f"{keyword}.csv", "w", encoding="utf-8-sig")
file.write("title, location, company, link,\n")

for job in jobs:
  file.write(f"{job['title']}, {job['location']}, {job['company']}, {job['link']}\n")

file.close()
