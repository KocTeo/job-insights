from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    job_types = set()

    for job in jobs_list:
        job_types.add(job["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_filtered_by_type = list()

    for job in jobs:
        if job["job_type"] == job_type:
            jobs_filtered_by_type.append(job)

    return jobs_filtered_by_type


def get_unique_industries(path):
    jobs_list = read(path)

    industries = set()

    for job in jobs_list:
        if job["industry"] != '':
            industries.add(job["industry"])

    return list(industries)


def filter_by_industry(jobs, industry):
    jobs_filtered_by_industry = list()

    for job in jobs:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)

    return jobs_filtered_by_industry


def get_max_salary(path):
    # usar isdigit antes do append
    # dúvida do Halister no Slack
    jobs_list = read(path)

    max_salary_list = list()

    for job in jobs_list:
        if job["max_salary"].isdigit():
            max_salary_list.append(int(job["max_salary"]))

    highest_salary = max(max_salary_list)

    return highest_salary


def get_min_salary(path):
    jobs_list = read(path)

    min_salary_list = list()

    for job in jobs_list:
        if job["min_salary"].isdigit():
            min_salary_list.append(int(job["min_salary"]))

    lowest_salary = min(min_salary_list)

    return lowest_salary


def matches_salary_range(job, salary):
    exist = "max_salary" in job and "min_salary" in job

    if not exist:
        raise ValueError("Sálario mínimo e máximo precisam ser informados")

    max_salary = str(job["max_salary"])
    min_salary = str(job["min_salary"])

    max_salary_is_number = max_salary.isdigit()
    min_salary_is_number = min_salary.isdigit()

    if not max_salary_is_number and min_salary_is_number:
        raise ValueError("max_salary e min_salary precisa ser números")

    if int(max_salary) < int(min_salary):
        raise ValueError("O valor mínimo precisa ser menor que o máximo")

    if type(salary) is not int:
        raise ValueError("O sálario precisa ser um número")

    return True if int(min_salary) <= salary <= int(max_salary) else False


def filter_by_salary_range(jobs, salary):
    jobs_filtered_by_salary_range = list()

    for job in jobs:
        data = {
            'min_salary': job["min_salary"], 'max_salary': job["max_salary"]
        }
        try:
            check_salary_in_range = matches_salary_range(data, salary)
            if check_salary_in_range:
                jobs_filtered_by_salary_range.append(job)
        except ValueError:
            pass

    return jobs_filtered_by_salary_range
