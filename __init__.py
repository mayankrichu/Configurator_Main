from flask import Flask
from Mayank.Configurator_Homepage.routes import configurator_homepage
from Mayank.Configurator.routes import configurator

def create_app():
    app = Flask(__name__)
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')
    app.register_blueprint(configurator_homepage)
    app.register_blueprint(configurator)

    return app
