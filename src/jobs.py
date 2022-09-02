import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r", encoding="utf-8") as job_list:
        all_jobs = []
        file_reader = csv.DictReader(job_list, delimiter=",", quotechar='"')

        for job in file_reader:
            all_jobs.append(job)
        return all_jobs
