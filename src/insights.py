from jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)

    job_types = set()

    for job in jobs_list:
        job_types.add(job["job_type"])

    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = read(jobs)

    jobs_filtered_by_type = list()

    for job in jobs_list:
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
    jobs_list = read(jobs)

    jobs_filtered_by_industry = list()

    for job in jobs_list:
        if job["industry"] == industry:
            jobs_filtered_by_industry.append(job)

    return jobs_filtered_by_industry


def get_max_salary(path):
    jobs_list = read(path)

    max_salary_list = list()

    for job in jobs_list:
        if job["max_salary"] != '':
            max_salary_list.append(int(job["max_salary"]))

    highest_salary = max(max_salary_list)

    return highest_salary


def get_min_salary(path):
    jobs_list = read(path)

    min_salary_list = list()

    for job in jobs_list:
        if job["min_salary"] != '':
            min_salary_list.append(int(job["min_salary"]))

    lowest_salary = min(min_salary_list)

    return lowest_salary


def matches_salary_range(job, salary):
    max_is_int = type(job["max_salary"]) is not int
    min_is_int = type(job["min_salary"]) is not int

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Sálario mínimo e máximo precisam ser informados")

    if max_is_int or min_is_int:
        ValueError("max_salary e min_salary precisa ser números")

    if job["min_salary"] > job["max_salary"]:
        ValueError("O valor mínimo precisa ser menor que o máximo")

    if type(salary) is not int:
        ValueError("O sálario precisa ser um número")

    return True if job["min_salary"] <= salary <= job["max_salary"] else False


def filter_by_salary_range(jobs, salary):
    jobs_list = read(jobs)

    jobs_filtered_by_salary_range = list()

    for job in jobs_list:
        try:
            check_salary_in_range = matches_salary_range(job, salary)
            if check_salary_in_range:
                jobs_filtered_by_salary_range.append(job)
        except ValueError:
            pass

    return jobs_filtered_by_salary_range
