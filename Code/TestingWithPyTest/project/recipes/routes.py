from flask import render_template

from . import recipes_blueprint


# ------
# Routes
# ------

@recipes_blueprint.route('/')
def index():
    return render_template('recipes/index.html')
