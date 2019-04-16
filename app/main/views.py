from flask import render_template,redirect,url_for,request
from . import main
from ..models import Sources
from ..requests import get_sources, get_article


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    cat_general = get_article('general')
    cat_business = get_article('business')
    cat_entertainment = get_article('entertainment')
    cat_sports = get_article('sports')
    cat_tech = get_article('technology')
    cat_science = get_article('science')
    cat_health = get_article('health')

    title = 'Home | Best News Update Site'
    
    return render_template('index.html',title=title, general=cat_general, business = cat_business, entertainment = cat_entertainment, sports = cat_sports, tech = cat_tech, science = cat_science, health = cat_health)

@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id,per_page):
    

    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id, news = news_source)

@main.route('/topheadlines&<int:per_page>')
def headlines(per_page):
    '''
    Function that returns top headlines articles
    '''
    # per_page = 40
    topheadlines_news = topheadlines(per_page)
    title = 'Top Headlines'
    return render_template('topheadlines.html',title=title, name='Top Headlines' ,news=topheadlines_news)

@main.route('/everything&<int:per_page>')
def all_news(per_page):
    '''
    Function that returns top headlines articles
    '''
    # per_page = 40
    everything_news = everything(per_page)
    title = 'All News'
    
    search_articles = request.args.get('search_query')

    if search_articles:
        return redirect(url_for('main.search',topic=search_articles))
    else:
        return render_template('topheadlines.html', title=title, name='All News', news=everything_news)

