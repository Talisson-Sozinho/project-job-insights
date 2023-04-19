from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    salary_list = [
        int(job["max_salary"])
        for job in jobs_data
        if job["max_salary"] != "" and job["max_salary"] != "invalid"
    ]
    return max(salary_list)


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    salary_list = [
        int(job["min_salary"])
        for job in jobs_data
        if job["min_salary"] != "" and job["min_salary"] != "invalid"
    ]
    return min(salary_list)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (
        "max_salary" not in job
        or "min_salary" not in job
        or not str(job["max_salary"]).isnumeric()
        or not str(job["min_salary"]).isnumeric()
        or int(job["min_salary"]) > int(job["max_salary"])
        or not type(salary) in [int, str]
    ):
        raise ValueError

    return int(job["max_salary"]) >= int(salary) >= int(job["min_salary"])


def is_valid_and_in_range_job(job: Dict, salary: Union[str, int]) -> bool:
    try:
        return matches_salary_range(job, salary)
    except ValueError:
        return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    return [job for job in jobs if is_valid_and_in_range_job(job, salary)]
