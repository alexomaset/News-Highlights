from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_source,get_article
from ..models import Source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title
    message = 'Hello World'
    return render_template('index.html',message = message)