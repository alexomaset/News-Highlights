import os


class Config:


    SOURCE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apikey={}'
    ARTICLE_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


#    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
#    ARTICLE_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e0894a72d22c4b0fabb51d657e320c14'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}