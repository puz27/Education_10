import json
import os


def load_candidates(file_name: str) -> list:
    """
    load data from local file
    :param file_name: name of import file
    :return: list of dictionaries
    """
    path_file = os.path.join(os.getcwd(), "data", file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data


def get_all(candidates: list) -> list:
    """
    load all candidates
    :param candidates: list with candidates
    :return: list
    """
    needed_candidates = []
    for candidate in candidates:
        needed_candidates.append(candidate["name"])
    return needed_candidates


def get_by_pk(pk: int, candidates: list) -> str:
    """
    :param pk: number that need to find
    :param candidates: list with candidates
    :return: information about candidate
    """
    for candidate in candidates:
        if candidate.get("pk") == pk:
            return candidate
    return "Такого кандидата нет"


def get_by_skill(skill_name: str, candidates: list) -> list:
    """
    :param skill_name: skill that need to find
    :param candidates: list with candidates
    :return: list on users with needed skills
    """
    candidates_with_needed_skills = []
    skill_needed = [skill_name.lower()]
    for candidate in candidates:
        skills_known = (set(candidate["skills"].lower().split(", ")))
        if set(skill_needed).issubset(skills_known) is True:
            candidates_with_needed_skills.append(candidate)
    return candidates_with_needed_skills


data_of_candidats = load_candidates("candidates.json")
print(get_all(data_of_candidats))
print(get_by_pk(2, data_of_candidats))
print(get_by_skill("Python", data_of_candidats))
