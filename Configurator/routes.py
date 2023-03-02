from flask import Blueprint, render_template
from Configurator.utils import get_skills

configurator = Blueprint('configurator', __name__)


@configurator.route('/configurator')
def Configurator():
    independent_skill_file_path = '/Users/mayank/Downloads/task.json'
    dependent_skill_file_path = '/Users/mayank/Downloads/task.json'
    task_independent_skills = get_skills(independent_skill_file_path)
    task_dependent_skills = get_skills(dependent_skill_file_path)
    return render_template('Configurator.html', task_independent_skills=task_independent_skills, task_dependent_skills = task_dependent_skills )

