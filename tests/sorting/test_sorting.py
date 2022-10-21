from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "max_salary": 65042,
            "min_salary": 44520,
            "date_posted": "2020-05-12"
        },
        {
            "max_salary": 32000,
            "min_salary": 15000,
            "date_posted": "2020-02-11"
        },
        {
            "max_salary": 18250,
            "min_salary": 10500,
            "date_posted": "2020-11-03"
        },
    ]


def test_sort_by_criteria(jobs):
    args = ["min_salary", "max_salary", "date_posted"]

    for criteria in args:
        sort_by(jobs, criteria)

        if criteria == "min_salary":
            assert jobs[0][criteria] <= jobs[1][criteria]
        else:
            assert jobs[0][criteria] > jobs[1][criteria]
