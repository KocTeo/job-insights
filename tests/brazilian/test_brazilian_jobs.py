from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    keys_expect = {("title", "salary", "type")}

    job_keys = set()

    for job in jobs:
        job_keys.add(tuple(job.keys()))

    assert keys_expect == job_keys
