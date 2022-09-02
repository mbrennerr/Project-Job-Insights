from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = []

    for job in all_jobs:
        job_types.append(job["job_type"])
    return list(set(job_types))  # remove duplicates from list of job types


def filter_by_job_type(jobs, job_type):

    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    all_jobs = read(path)
    industries = []

    for job in all_jobs:
        if job["industry"] != "":
            industries.append(job["industry"])
    return list(set(industries))  # remove duplicates from list of industries


def filter_by_industry(jobs, industry):

    job_list = []
    for job in jobs:
        if job["industry"] == industry:
            job_list.append(job)
    return job_list


def get_max_salary(path):

    all_jobs = read(path)
    list_salaries = []

    for job in all_jobs:
        if job["max_salary"] != "" and job["max_salary"].isnumeric():
            list_salaries.append(int(job["max_salary"]))
    return max(list_salaries)


def get_min_salary(path):
    all_jobs = read(path)
    list_salaries = []

    for job in all_jobs:
        if job["min_salary"] != "" and job["min_salary"].isnumeric():
            list_salaries.append(int(job["min_salary"]))
    return min(list_salaries)


def matches_salary_range(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("min_salary or max_salary not in job")

    elif (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary.append(job)
        except ValueError:
            pass
    return filtered_salary
