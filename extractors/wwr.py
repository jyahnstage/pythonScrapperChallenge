from bs4 import BeautifulSoup
import requests

def extract_wwr_jobs(term):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="
    request = requests.get(base_url+term)

    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        results = []
        jobs = soup.find_all('section', class_='jobs')
        for job in jobs:
            lists = job.find_all('li')
            lists.pop(-1)
            # print(lists)
            # print('////////////')
            for list in lists:
                anchors = list.find_all('a', recursive=False)
                # print(anchors)
                anchor = anchors[0]['href']
                # print(anchor)
                link = f"https://weworkremotely.com{anchor}"
                # print(link)
                for _a in anchors:
                    company, time, region = _a.find_all('span', class_='company')
                    # print(company, region)
                    title = _a.find('span', class_='title')
                    # print(title.string)
                    job_data = {
                        'title': title.string.strip().replace(","," "),
                        'company': company.string.strip().replace(","," "),
                        'region': region.string.strip().replace(","," "),
                        'link': link
                    }
                    results.append(job_data)
        return results
    else:
        print("Can't connect to website")

# extract_wwr_jobs("python")