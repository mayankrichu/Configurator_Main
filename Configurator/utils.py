import json


def get_skills(file_location):
    f = open(file_location)
    data = json.load(f)
    task_dependent_skills = []

    for idx, element in enumerate(data[0]['Subtasks']):
        task_dependent_skills.append(element['Name'])
# Closing file
    f.close()
    return task_dependent_skills

