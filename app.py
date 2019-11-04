from flask import Flask, render_template, request

app = Flask(__name__)

#!-----!Base Page!-----!#
@app.route('/')
def index():
    """Renders the home page with links to Fortune and Weather."""
    return render_template('index.html')

#!-----!Fortune Form!-----!#
@app.route('/fortune_form')
def fortune_form():
    """Displays the fortune form sheet."""

    return render_template('/fortune_form.html')


#!-----!Fortune Teller Results Page!-----!#
@app.route('/fortune_results')
def fortune_results():
    """Shows the User their fortune"""
    users_name = request.args.get('name')
    users_gender = request.args.get('gender')


    return render_template('fortune_results.html')
