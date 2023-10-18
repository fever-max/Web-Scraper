from requests import get
from bs4 import BeautifulSoup


def exfract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website!")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all("li")
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all("a")
        anchors = anchors[1]
        link = anchors["href"]
        company, kind, region = anchors.find_all("span", class_="company")
        title = anchors.find("span", class_="title")
        job_data = {
            "title": title.string.replace(",", " "),
            "link": f"https://weworkremotely.com{link}",
            "company": company.string.replace(",", " "),
            "location": region.string.replace(",", " "),
        }
        results.append(job_data)
    return results
