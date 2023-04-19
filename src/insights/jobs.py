from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as csv_file:
        csv_converted = csv.DictReader(csv_file)
        return [linha for linha in csv_converted]


def get_unique_job_types(path: str) -> List[str]:
    jobs_data = read(path)
    set_of_jobs_types = {linha["job_type"] for linha in jobs_data}
    return [jobs_types for jobs_types in set_of_jobs_types]


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
