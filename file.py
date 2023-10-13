from extractors.remoteok import extract_remoteok_jobs
from extractors.wwr import extract_wwr_jobs

def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")
    file.write("Title, Company, Location, URL \n")

    for job in jobs:
        file.write(
            f"{job['title']},{job['company']},{job['region']},{job['link']}\n"
        )
    file.close()