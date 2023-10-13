from bs4 import BeautifulSoup
import requests

def extract_remoteok_jobs(term):
  base_url = f"https://remoteok.com/remote-{term}-jobs"
  print(base_url)
  request = requests.get(base_url, headers={"User-Agent":"hello"})
  print(request.status_code)
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    results = []
    jobs = soup.find_all('tr', class_='job')
    for job_posts in jobs:
      job_post = job_posts.find_all('td', class_='company')
      for post in job_post:
        anchor = post.find_all('a')
        for titles in anchor:
          title = titles.find('h2')
        anchors = post.find('a')
        link = anchors['href']
        company_names = post.find_all('span', class_='companyLink')
        for company_name in company_names:
          company = company_name.find('h3')
        region = post.find('div', class_='location')
        job_data = {
          'title': title.string.strip('\n').replace(","," "),
          'company': company.string.strip('\n').replace(","," "),
          'region': region.string.replace(","," "),
          'link': f'https://remoteok.com/{link}'
        }
        results.append(job_data)
    return results
    # for result in results:
    #   print(result)
    #   print('======================================================')
  else:
    print("Can't get jobs.")

# term = input("what keyword do you want to search?")
# extract_remoteok_jobs("python")
# print(base_url)