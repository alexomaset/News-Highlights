class Config:
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    DEBUG = True