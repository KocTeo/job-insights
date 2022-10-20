from src.jobs import read


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

    all_salary = list()

    for job in jobs_list:
        if job["max_salary"] != '':
            all_salary.append(int(job["max_salary"]))

    highest_salary = max(all_salary)

    return highest_salary


def get_min_salary(path):
    jobs_list = read(path)

    all_salary = list()

    for job in jobs_list:
        if job["min_salary"] != '':
            all_salary.append(int(job["min_salary"]))

    lowest_salary = min(all_salary)

    return lowest_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
