from flask import Blueprint, render_template

"""
    some arguements are specified when creating the blueprint
    the first arguement 'site' is the blueprint name
    which is used by flask to route

    the second arg __name__ is the import name
    this is what flask uses to locate resources
"""

site = Blueprint('site',__name__,template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')