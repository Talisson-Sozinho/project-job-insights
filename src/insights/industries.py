from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    set_of_industries = {linha["industry"] for linha in jobs_data}
    return [industry for industry in set_of_industries if industry != ""]


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
