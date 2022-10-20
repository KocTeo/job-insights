from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    jobs_dict = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert jobs_dict == dict