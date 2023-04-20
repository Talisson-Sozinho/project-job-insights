from src.pre_built.sorting import sort_by
import pytest


jobs = [
    {
        "title": "Front End",
        "min_salary": 4000,
        "max_salary": 15000,
        "date_posted": "2022-01-01",
    },
    {
        "title": "Back End",
        "min_salary": 8000,
        "max_salary": 18000,
        "date_posted": "2022-01-04",
    },
    {
        "title": "Full stack",
        "min_salary": 10000,
        "max_salary": 20000,
        "date_posted": "2022-01-02",
    },
    {
        "title": "Data Science",
        "min_salary": 5000,
        "max_salary": 12000,
        "date_posted": "2022-01-03",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "date_posted")
    assert [job["title"] for job in jobs] == [
        "Back End",
        "Data Science",
        "Full stack",
        "Front End",
    ]
    sort_by(jobs, "max_salary")
    assert [job["title"] for job in jobs] == [
        "Full stack",
        "Back End",
        "Front End",
        "Data Science",
    ]

    sort_by(jobs, "min_salary")
    assert [job["title"] for job in jobs] == [
        "Front End",
        "Data Science",
        "Back End",
        "Full stack",
    ]
    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
