from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)


def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs"
  browser.get(f"{base_url}?q={keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", class_="css-jbuxu0 ecydgvn0")
  pages = pagination.find_all("div", recursive=False)
  count = len(pages)
  if count == 0:
    return 1
  else:
    return count - 1


def extract_indeed_jobs(keyword):
  base_url = "https://kr.indeed.com/jobs"
  pages = get_page_count(keyword)
  print("Found", pages, "pages")

  results = []

  for page in range(pages):
    final_url = f"{base_url}?q={keyword}&start={page*10}"
    print("Requesting", final_url)
    browser.get(final_url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    job_list = soup.find("ul", class_="css-zu9cdh eu4oa1w0")
    jobs = job_list.find_all('li', recursive=False)

    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone is None:
        anchor = job.select_one("h2 a")
        title = anchor["aria-label"]
        link = anchor["href"]
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
            "title": title,
            "link": f"https://kr.indeed.com{link}",
            "company": company.string,
            "location": location.string,
        }
        results.append(job_data)

  return results
