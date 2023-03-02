from flask import Blueprint, render_template


configurator_homepage = Blueprint('configurator_homepage', __name__)


###################################################
################ All Deviation ##################

#Display all the deviations which occured
@configurator_homepage.route('/')
def Configurator_Homepage():


    return render_template('Configurator_Homepage.html')