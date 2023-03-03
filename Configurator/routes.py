from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from Configurator.utils import get_skills

configurator = Blueprint('configurator', __name__)


@configurator.route('/configurator')
def Configurator():
    independent_skill_file_path = '/Users/mayank/Downloads/task.json'
    dependent_skill_file_path = '/Users/mayank/Downloads/task.json'
    task_independent_skills = get_skills(independent_skill_file_path)
    task_dependent_skills = get_skills(dependent_skill_file_path)
    return render_template('Configurator.html', task_independent_skills=task_independent_skills, task_dependent_skills = task_dependent_skills )

@configurator.route('/configurator_submit' ,methods=['POST'])
def Configurator_Submit():

    selected_configuration = request.form.get('values').split(',')
    print(selected_configuration)
    return render_template('Configurator.html')
