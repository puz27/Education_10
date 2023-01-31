import json
import os


def load_candidates(file_name: str) ->list :
    """
    load data from local file
    :param file_name: name of import file
    :return: list of dictionaries
    """
    path_file = os.path.join(os.getcwd(), file_name)
    file = open(path_file, 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    return data

data_of_candidats = load_candidates("candidates.json")
#print(data_of_candidats)

def get_all(data_of_candidats):
    for candidate in data_of_candidats:
        print(candidate["name"])

def get_by_pk(pk, data_of_candidats):
    for candidate in data_of_candidats:
        if candidate.get("pk") == pk:
            print(candidate)
    print("Такого кандидата нет")

def get_by_skill(skill_name, data_of_candidats):
    skill_needed = [skill_name]
    for candidate in data_of_candidats:
        skills_known = (set(candidate["skills"].split(", ")))
        #print(skills_known.intersection(set(skill_needed)))
        #print((set(skill_needed)).issubset(skills_known))
        if set(skill_needed).issubset(skills_known) is True:
            print(candidate)


print(get_by_skill('python', data_of_candidats))