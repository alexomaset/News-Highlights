import urllib.request,json
from .models import Articles,Sources


#Getting api key
api_key = 'e0894a72d22c4b0fabb51d657e320c14'

#Getting the news base url
# base_article_url = None
# base_source_url ='https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}'

source_url = 'https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def configure_request(app):
    global base_article_url,base_source_url
    api_key = app.config['NEWS_API_KEY']
    base_article_url = app.config['ARTICLE_URL']
    base_source_url = app.config['SOURCE_URL']



def get_article(category): 
        '''
        Function that gets the json response to our url request
        '''
        get_article_url = article_url.format(category,api_key)

        # with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f80d5dfbac424cbb9ebffcc23c378ffd") as url:
        with urllib.request.urlopen(get_article_url) as url:
            
            get_article_data = url.read()
            get_article_response = json.loads(get_article_data)

            article_results = []
            if get_article_response['articles']:
                news_list = get_article_response['articles']
                article_results = process_sources(news_list)
            
            # article_results_list = get_article_response['articles']
            # article_results = process_articles(article_results_list)

        return article_results 

def process_sources(article_results):
        '''
        Function  that processes the article result and transform them to a list of Objects
        Args:
        article_list: A list of dictionaries that contain article details
        Returns :
        article_results: A list of movie objects
        '''
        article_results = [] 
        for article_item in article_results:
           
            id = article_item.get("id")  
            name = article_item.get("source")
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
           
            if urlToImage:
                article_object = Articles(id,source,author,title,description,url,urlToImage,publishedAt) 
                article_results.append(article_object) 

        print(article_results)
        return article_results 





def get_sources(category): 
        '''
        Function that gets the json response to our url request 
        '''
        get_source_url =  source_url.format(category,api_key) 
        # with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}") as url: 
        with urllib.request.urlopen(get_source_url) as url: 
            get_source_data = url.read() 
            get_source_response = json.loads(get_source_data.decode()) 

            sources_results = []

            if get_source_response['sources']:

                source_results_list = get_source_response['sources']
                source_results = process_sources(source_results_list) 

            # source_results_list = get_source_response['articles']
            # source_results_list = get_source_response['sources']
           
        return source_results 

def process_sources(source_results):
        '''
        Function  that processes the source result and transform them to a list of Objects
        Args:
        article_list: A list of dictionaries that contain source details
        Returns :
        source_results: A list of movie objects
        '''

        processed_results = [] 
        for source_item in processed_results:
            id = source_item.get('id')
            name = source_item.get('name')
            description = source_item.get('description')
            url = source_item.get('url')
            category = source_item.get('category')
            language = source_item.get('language')
            # title= source_item.get('title')
            # urlToImage =source_item.get('urlToImage')
            country = source_item.get('country')

            source = Sources(id,name,description,url,category,language,country)
            source_results.append(source)

        return source_results